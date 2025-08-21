
## **Write at AI speed for human readers.**

# AI Blog App ✍️

📖 También disponible en [Español](README.es.md)

An advanced framework for building AI-powered content generation pipelines. This project uses a multi-agent system, powered by Microsoft AutoGen, to autonomously write, critique, and review articles for quality, compliance, and SEO. The system can accept optional context from a PDF, which the LLM then handles for data extraction and context. Users can also specify the desired length of the article, with a default length of 300 words.

---

## 🧠 How It Works

The AI Blog App simulates a collaborative writing and editing process using a team of specialized AI agents. Each agent plays a unique role in refining the article or blog post, communicating intelligently to revise and refine the content until it meets quality standards for readability, SEO, and flow.

-   **Writer Agent:** Crafts an initial blog post based on a topic prompt, designed to be simple, engaging, and story-driven.
-   **Critic Agent:** Reviews the writer's draft and offers direct, actionable feedback on story structure, clarity, tone, and flow.
-   **SEO Reviewer:** Ensures the blog includes relevant keywords, strong headings, and other on-page SEO elements to improve visibility on search engines.
-   **Content Marketing Reviewer:** Analyzes structure, engagement, and presentation to ensure the blog is clear, logically organized, and compelling for readers.
-   **Clarity and Ethics Reviewer:** Checks that the writing is easy to understand for a general audience, free of confusing or problematic language, and appropriate for public consumption.

The system also supports context from basic PDFs, with the LLM handling the data extraction.

---

## 💡 Key Features

**🧩 Modular Agent Architecture**
The framework includes specialized agents for:
-   **Writer:** Crafts story-driven blog posts using simple, clear language.
-   **Content Marketing Reviewer:** Improves structure, flow, and engagement.
-   **Clarity & Ethics Reviewer:** Ensures content is easy to understand and free from misleading claims.
-   **SEO Reviewer:** Optimizes for discoverability on search engines like Google and AI tools.

**💬 Intelligent Agent Collaboration**
Our system employs a collaborative model where specialized agents, each with a focused role, operate within a structured review loop. A central meta-agent then synthesizes their individual contributions into a cohesive, polished final product. This orchestration allows for the creation of high-engagement blog posts by leveraging the unique strengths of each specialized agent.

**📦 Use As a Library or API**
You can easily integrate this framework into your existing projects in a couple of ways:
-   **Python Library:** Directly incorporate the blog generation capabilities into your Python applications.
-   **API Service:** Run the application as a real-time API to power a blog generation service for your website or content platform.

**✅ SEO-Friendly & Reader-Focused**
Designed to help your content perform well on search engines and connect with real people. All blog posts are generated using content marketing best practices to help your content stand out.

---

## 🔧 Installation & Usage

### Dependencies

This project is built on **Microsoft AutoGen**, leveraging its multi-agent capabilities. The core dependencies are:

-   `autogen-agentchat>=0.7.1`
-   `autogen-ext[all]>=0.7.1`
-   `openai>=1.98.0`

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
"Coming soon on PyPI"

````

\<sub\>Requires Python 3.10+\</sub\>

Or install the Blog Agent Framework directly from GitHub using `pip`:

```bash
pip install git+https://github.com/edilma/AI_Blog_App.git

```
🌐 Project Links

Homepage: https://github.com/edilma/AI_Blog_App

Documentation: https://github.com/edilma/AI_Blog_App/blob/main/README.md

Bug Tracker: https://github.com/edilma/AI_Blog_App/issues



### ✍️ Basic Usage

Here's how to quickly get started with the built-in example.

1.  **Navigate** into the `examples` directory:

    ```bash
    cd examples
    ```

2.  **Create** your own `.env` file by copying the template.

    ```bash
    # On Windows
    copy .env.example .env

    # On macOS or Linux
    cp .env.example .env
    ```

3.  **Add** your preferred model credentials to `.env`. For example:

    ```
    GEMINI_API_KEY=your_gemini_api_key_here

    # or for OpenAI
    OPENAI_API_KEY=your_openai_key_here
    ```

4.  **Run** the example script:

    ```bash
    python main.py
    ```

-----

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

Created with 💻 by **Edilma Riano**
Helping businesses and creators use AI to work smarter and scale faster.

🐙 [Follow me on GitHub](https://github.com/edilma)
