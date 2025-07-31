import asyncio
import os
from dotenv import load_dotenv

from ai_blog_app import generate_blog_post_with_review

# Load .env file (important for GEMINI_API_KEY)
load_dotenv(dotenv_path=os.path.join(os.path.dirname(__file__), ".env"))

async def main():
    """
    Run a blog post generation using Gemini (or any other provider).
    """
    topic = "How to use AI for business ideas generation"

    # --- Choose the provider and optionally override model ---
    provider = "gemini"
    model = "gemini-1.5-flash"  # Optional, could be left out if default is in JSON

    print(f"\n--- Generating blog post for: '{topic}' using {provider} / {model} ---")

    try:
        final_post = await generate_blog_post_with_review(
            topic=topic,
            provider=provider,
            model=model  # Optional: could also let config.json fully decide
        )
    except Exception as e:
        print(f"\033[91mError: {e}\033[0m")
        return

    print("\n\033[92m--- Generated Blog Post ---\033[0m\n")
    print(final_post)


if __name__ == "__main__":
    asyncio.run(main())
