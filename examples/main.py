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
    # To use a different model, simply uncomment the provider and model you want.
    # Make sure you have the corresponding API key in your .env file!
    #
    # Option 1: Use Google Gemini (requires GEMINI_API_KEY in .env)
    #provider = "gemini"
    #model = "gemini-1.5-flash"

    # Option 2: Use OpenAI (requires OPENAI_API_KEY in .env)
    provider = "openai"
    model = "gpt-4-turbo"

    # Option 3: Use Anthropic Claude (requires ANTHROPIC_API_KEY in .env)
    # provider = "claude"
    # model = "claude-3-opus-20240229"

    # Option 4: Use a local Ollama model (requires Ollama running locally)
    # provider = "ollama"
    # model = "llama3"

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
