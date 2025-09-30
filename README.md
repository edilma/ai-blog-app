
## **Write at AI speed for human readers.**

# AI Blog App ✍️

📖 También disponible en [Español](README.es.md)

***Create smarter, better blogs and articles—autonomously.***


The AI Blog App provides a powerful content generation engine powered by a multi-agent system. Its core function, `generate_blog_post_with_review()`, requires only a topic to produce high-quality, engaging blog and article content. Users can enhance the output by providing optional context (as a string) for grounded, factual generation, and can specify the maximum word count (default: 300 words). The system leverages specialized AI agents—writer, critic, and multiple reviewers—working collaboratively to ensure the final content meets professional standards for readability, SEO, and engagement.

> **Note for Developers:** This library is built on Microsoft's AutoGen framework, which opens up exciting possibilities for advanced customization. You can extend the agent system with your own specialized agents, modify conversation flows, or adapt the review process for specific content types. AutoGen's flexible architecture allows you to fine-tune agent behaviors, prompt templates, and interaction patterns to meet your specific requirements. The system is ideal for building RAG (Retrieval-Augmented Generation) applications—the API is already set up to accept external context, making it simple to integrate with document retrievers, knowledge bases, or custom data sources. See the [AutoGen documentation](https://microsoft.github.io/autogen/) to explore the full potential of this powerful framework.

---

## 🧠 How It Works

The AI Blog App simulates a collaborative writing and editing process using a team of specialized AI agents. Each agent plays a unique role in refining the article or blog post, communicating intelligently to revise and refine the content until it meets quality standards for readability, SEO, and flow.

-   **Writer Agent:** Crafts an initial blog post or article based on a topic prompt, designed to be simple, engaging, and story-driven.
-   **Critic Agent:** Reviews the writer's draft and offers direct, actionable feedback on story structure, clarity, tone, and flow.
-   **SEO Reviewer:** Ensures the blog includes relevant keywords, strong headings, and other on-page SEO elements to improve visibility on search engines.
-   **Content Marketing Reviewer:** Analyzes structure, engagement, and presentation to ensure the blog is clear, logically organized, and compelling for readers.
-   **Clarity and Ethics Reviewer:** Checks that the writing is easy to understand for a general audience, free of confusing or problematic language, and appropriate for public consumption.

While the library itself doesn't process PDFs directly, its context-aware design allows applications using this library to feed it data extracted from PDFs or other document sources, making it versatile for various content generation workflows.

---

## 💡 Key Features

**🧩 Modular Agent Architecture**
- Specialized agents with distinct roles in the content creation process
- Agent customization via prompt engineering
- Clear separation of responsibilities between writer, critic, and reviewer agents

**💬 Multi-stage Review Pipeline**
- Sequential agent workflow for reliable content generation
- Multiple specialized reviewer types examining different content aspects
- Feedback consolidation via critic agent for cohesive improvements

**📦 Simple Integration**
- Clean async Python API with comprehensive docstrings
- Easy import and use in existing Python projects
- Straightforward function call to generate complete blog posts and articles

**⚙️ Developer-Friendly Configuration**
- JSON-based provider and model configuration
- Environment variable credential management
- Configurable word count limitations
- Runtime model switching across multiple LLM providers

---

## 🔧 Installation & Usage

### Dependencies

This project is built on **Microsoft AutoGen**, leveraging its multi-agent capabilities. The core dependencies are:

-   `autogen-agentchat>=0.7.1`
-   `autogen-ext[all]>=0.7.1`
-   `openai>=1.98.0`
-   `tiktoken>=0.11.0`

### Flexible LLM Support

The application supports multiple Large Language Model (LLM) providers right out of the box:
-   **OpenAI:** Works with models like ChatGPT and GPT-4.
-   **Google Gemini:** Connects via an OpenAI-compatible API.
-   **Claude:** Supports models from Anthropic.
-   **Ollama:** Enables the use of local models such as LLaMA 3.

Configuration is straightforward and fully **JSON-driven** (`llm_config.json`), allowing you to easily swap providers or models without touching the codebase. All credentials are securely managed via `.env` files.

### 🚀 Installation

Install from PyPI:
```bash
pip install ai-blog-app
````

<sub>Requires Python 3.10+</sub>

Or install the Blog Agent Framework directly from GitHub using `pip`:

```bash
pip install git+https://github.com/edilma/ai-blog-app.git

```
🌐 Project Links

Homepage: https://github.com/edilma/AI_Blog_App

Documentation: https://github.com/edilma/AI_Blog_App/blob/main/README.md

Bug Tracker: https://github.com/edilma/AI_Blog_App/issues



### ✍️ Basic Usage

Using this library in your projects is straightforward:

1. **Set Up Environment Variables**

Create a `.env` file in your project directory with your API keys:

```plaintext
# Choose the provider you want to use and add its API key
OPENAI_API_KEY=sk-...your-key-here...
# Or for other providers:
# GEMINI_API_KEY=...your-key-here...
# ANTHROPIC_API_KEY=...your-key-here...
```

2. **Generate Content**

This example shows how to generate a blog post using the Gemini model:

```python
import asyncio
from dotenv import load_dotenv
from ai_blog_app import generate_blog_post_with_review

# Load environment variables from .env file
load_dotenv()

async def generate_post():
    topic = "The Future of AI in Content Marketing"
    
    print(f"Starting agent pipeline for topic: {topic}...")

    final_post = await generate_blog_post_with_review(
        topic=topic,
        provider="gemini",  # Options: "openai", "gemini", "claude", "ollama"
        model="gemini-1.5-flash",
        max_words=500  # Optional: control output length
    )
    
    print("\n--- GENERATED ARTICLE ---\n")
    print(final_post)
    
    # You can now save, display, or process the generated content
    return final_post

if __name__ == "__main__":
    # Run the async function
    asyncio.run(generate_post())
```

### 3. Additional Features

**Context-Based Generation**

You can provide additional context to ground the content in specific information:

```python
final_post = await generate_blog_post_with_review(
    topic="Benefits of Sustainable Agriculture",
    provider="openai",
    model="gpt-4o",
    context="Sustainable agriculture focuses on long-term ecosystem health...",
    max_words=700
)
```

**Full Example Script**

For complete, runnable examples with all configuration options, see the `examples/` directory in the GitHub repository:

[🔗 View the Examples Folder on GitHub](https://github.com/edilma/AI_Blog_App/tree/main/examples)


## 📁 Project Structure

The project is structured as a standard Python package, making it easy to install and use.

```
.
├── ai_blog_app/            # The main library source code
│   ├── agents/             # Contains the logic for individual AI agents
│   │   ├── __init__.py
│   │   ├── critic.py
│   │   ├── reviewers.py
│   │   └── writer.py
│   ├── utils/              # Contains utility functions
│   │   ├── __init__.py
│   │   └── helpers.py
│   ├── config.py           # Handles model client configuration
│   ├── llm_config.json     # LLM provider configuration
│   └── __init__.py
│
├── examples/               # Self-contained examples for users
│   ├── .env                # Environment file for variables
│   ├── .env.example        # Template for environment variables
│   └── main.py             # Main script to demonstrate library usage
│
├── .gitignore              # Specifies which files Git should ignore
├── LICENSE                 # The open-source license for the project
├── pyproject.toml          # The modern configuration file for the package
├── README.es.md            # Spanish version of the README
├── README.md               # This file!
└── uv.lock                 # Lock file for dependency management
```

-----

## 📜 License

This project is licensed under the [MIT License](LICENSE).

-----

## ✨ Author

Created by **Edilma Riano** — AI Systems Architect & Developer

I specialize in building practical AI tools that help businesses and content creators scale their operations. With expertise in agent-based systems and generative AI, I focus on creating solutions that merge technical excellence with business value.

### Connect & Collaborate

- 🐙 [GitHub](https://github.com/edilma)
- 💼 [LinkedIn](https://www.linkedin.com/in/edilma/)
- 🌐 [Portfolio](https://edilmariano.com/)

*Interested in custom AI content solutions or extending this library? Reach out for collaboration opportunities.*
