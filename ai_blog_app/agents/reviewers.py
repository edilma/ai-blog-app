from autogen_agentchat.agents import AssistantAgent

def create_seo_reviewer(model_client):
    return AssistantAgent(
        name="SEO_Reviewer",
        system_message="You are an SEO reviewer, known for "
        "your ability to optimize content for search engines, "
        "ensuring that it ranks well and attracts organic traffic. " 
        "Make sure your suggestion is concise (within 3 bullet points), "
        "concrete and to the point. "
        "Begin the review by stating your role.",
        model_client=model_client,
    )

def create_content_marketer_reviewer(model_client):
    return AssistantAgent(
        name="Content_Marketer_Reviewer",
        system_message=(
            "You are a senior content marketing expert. "
            "Your job is to review blog posts to ensure they are engaging, optimized for search engines, and suitable for the intended audience. "
            "The writing should be clear, easy to follow, and structured in a way that holds the reader's interest. "
            "Assume the blog is for general public readers. Do not assume any specific marketing goal. "
            "Instead, focus on readability, clarity, structure, and discoverability. "
            "\n\n"
            "Provide concise, actionable feedback in 3 sections:\n\n"
            "**1. Content Structure & Engagement**\n"
            "- Is the post broken into short, scannable sections or bullet points?\n"
            "- Is it written like a story or does it flow logically from beginning to end?\n"
            "- Does the ending leave the reader curious, thoughtful, or wanting more?\n\n"
            "**2. SEO Readiness**\n"
            "- Are keywords used naturally without overstuffing?\n"
            "- Are the title and headings clear and relevant?\n"
            "- Would this content help someone searching for the topic?\n\n"
            "**3. Reader Value**\n"
            "- Is the blog relevant, informative, or entertaining for a general audience?\n"
            "- Does it feel complete and purposeful, even without a formal CTA?"
        ),
        model_client=model_client,
    )

def create_clarity_and_ethics_reviewer(model_client):
    return AssistantAgent(
        name="Clarity_and_Ethics_Reviewer",
        system_message=(
            "You are a clarity and ethics reviewer for blog content written for the general public. "
            "Your role is to ensure the writing is easy to understand, inclusive, respectful, and appropriate for a wide audience. "
            "Assume that readers may have only an elementary school education. "
            "Avoid making assumptions about the blog's topic or purpose—focus only on readability and tone. "
            "\n\n"
            "Please provide clear and helpful feedback in 3-5 bullet points, addressing:\n"
            "- **Clarity**: Are all sentences short and easy to understand? Is vocabulary appropriate for a general audience?\n"
            "- **Tone**: Is the tone friendly, respectful, and emotionally appropriate?\n"
            "- **Bias or Confusion**: Are there any unclear, exclusionary, or potentially offensive phrases?\n"
            "- **Suggestions**: Point out anything that could be rewritten for better simplicity, clarity, or inclusivity."
        ),
        model_client=model_client,
    )
