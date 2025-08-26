import asyncio
import os
from dotenv import load_dotenv

from ai_blog_app import generate_blog_post_with_review

# The .env file is loaded automatically to make this example easy to run.
# In a production application, you should not rely on this.
# Instead, ensure your environment variables are managed securely
load_dotenv(dotenv_path=os.path.join(os.path.dirname(__file__), ".env"))

async def main():
    """
    This script provides a practical demonstration of the AI Blog App library's
    content generation pipeline. It shows how to use a single function to 
    orchestrate a multi-agent system that autonomously writes, critiques, 
    and reviews an article for quality and compliance, using a 
    specified LLM provider and model.

    """
    topic = "How to use AI for business ideas generation"

        # --- CHOOSE YOUR LLM PROVIDER AND MODEL ---
    # The 'provider' must match a provider key in your 'llm_config.json' file.
    # The 'model' name is optional and will override the default in the JSON.
    # Supported providers: "gemini", "openai", "ollama", etc.
    #
    # To use OpenAI:
    # provider = "openai"
    # model = "gpt-4-turbo"
    #
    # To use Gemini:
    provider = "gemini"
    model = "gemini-1.5-flash"  # Optional, could be left out if default is in JSON

    print(f"\n--- Generating blog post for: '{topic}' using {provider} / {model} ---")

    try:
        final_post = await generate_blog_post_with_review(
            topic=topic,
            provider=provider,
            model=model  
        )
    except Exception as e:
        print(f"\033[91mError: {e}\033[0m")
        return

    print("\n\033[92m--- Generated Blog Post ---\033[0m\n")
    print(final_post)


if __name__ == "__main__":
    asyncio.run(main())
