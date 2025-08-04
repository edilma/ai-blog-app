from typing import Optional
from .config import create_model_client
from .agents.writer import create_writer
from .agents.critic import create_critic
from .agents.reviewers import (
    create_content_marketer_reviewer,
    create_seo_reviewer,
    create_clarity_and_ethics_reviewer
)

# +++ NEW FUNCTION  +++
def _create_initial_writer_task(topic: str, context: Optional[str] = None) -> str:
    """
    Creates the initial task for the Writer agent, injecting the
    PDF context if it is provided.
    """
    context_instruction = ""
    if context:
        # This is the instruction that tells the agent to use the PDF content
        context_instruction = (
            "You MUST use the following text as the primary source and context for your article. "
            "Base your writing heavily on the information provided below.\n\n"
            "--- CONTEXT ---\n"
            f"{context}\n"
            "--- END CONTEXT ---\n\n"
        )

    # Combine the context instruction (if any) with the main topic task
    task = (
        f"{context_instruction}"
        f"Write a blog post about '{topic}'. Make sure the post is concise, engaging, and stays within 300 words."
    )
    return task



#function that will generate a blog post with reviews
async def generate_blog_post_with_review(
        topic: str, 
        model: Optional[str] = None, 
        provider: str = "openai", 
        context: Optional[str] = None 
        ) -> str:
    '''   
    Generates a blog post, using provided context if available.
    The process involves the Writer creating a draft, 
    which is then reviewed by multiple reviewers.
    '''
        # If no model is provided, use the default based on the provider
    if model is None:
        if provider == "openai":
            model = "gpt-3.5-turbo"
        elif provider == "gemini":
            model = "gemini-1.5-flash"
        # I  can add more defaults here for other providers

    model_client = create_model_client(provider=provider, model=model)
    writer = create_writer(model_client)
    critic = create_critic(model_client)
    seo_reviewer = create_seo_reviewer(model_client)
    content_marketer = create_content_marketer_reviewer(model_client)
    clarity_and_ethics_reviewer = create_clarity_and_ethics_reviewer(model_client)

    # create the initial task for the writer
    task= _create_initial_writer_task(topic, context)

    #2. writer creates the first draft of the blog post
    draft_result = await writer.run(task=task)
    if not draft_result or not draft_result.messages:
        return "The writer did not produce an initial draft."
    
    first_draft = draft_result.messages[-1].content

    #3. Reviewers provide feedback on the first draft
    reviews =[]
    reviewers = [
        content_marketer,
        clarity_and_ethics_reviewer,
        seo_reviewer
    ]
    for reviewer in reviewers:
        review_task = f"Review the following blog post draft:\n\n{first_draft}"
        review_result = await reviewer.run(task=review_task)
        if review_result and review_result.messages:
            reviews.append(f"Feedback from {reviewer.name}:\n{review_result.messages[-1].content}\n")

    #4.  The critic summarizes the feedback and delivers it to the writer
    all_reviews = "\n".join(reviews)
    critic_task = f"You are the critic. Your job is to summarize the following feedback and present a final, clear set of suggestions to the writer:\n\n{all_reviews}"
    final_feedback_result = await critic.run(task=critic_task)
    if final_feedback_result and final_feedback_result.messages:
        aggregated_feedback = final_feedback_result.messages[-1].content
    else:
        return "The critic did not provide feedback."
    
    # 5 Writer creates final version
    revision_task = f"Please revise your first draft based on the following feedback. Produce only the final, complete blog post.\n\nDraft:\n{first_draft}\n\nFeedback:\n{aggregated_feedback}"
    final_post_result = await writer.run(task=revision_task)

    # Check if the writer produced a final version
    if not final_post_result or not final_post_result.messages:
        return "The writer did not produce a final version."
    # The final version is the last message from the writer
    final_post = final_post_result.messages[-1].content
    return final_post
