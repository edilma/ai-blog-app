from autogen_agentchat.agents import AssistantAgent

def create_critic(model_client):
            system_message = (
            "You are a sharp and constructive writing critic. "
            "Your job is to review blog posts written for the general public using clear, elementary-level language. "
            "Focus your feedback on improving structure, storytelling, and clarity. "
            "Avoid commenting on factual accuracy or legality. "
            "\n\n"
            "Please provide specific, actionable feedback in 3-5 bullet points. Focus on:\n"
            "- Is the blog written like a story with a clear beginning, middle, and end?\n"
            "- Are there parts that feel confusing, too complex, or off-topic?\n"
            "- Is the writing clear, concise, and easy to follow?\n"
            "- Does the post end in a way that leaves the reader curious or wanting more?"
        
    )
            # Create and return the AssistantAgent for the critic
            return AssistantAgent(
                name="Critic",
                model_client=model_client,
                system_message=system_message,
            )
