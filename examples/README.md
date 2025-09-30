# AI Blog App Examples

This directory contains a self-contained, working example of the AI Blog App library. It's the best way to quickly see the framework in action.

## How to Run the Example

Follow these steps in order to run the example:

### 1. Navigate to this directory

```bash
cd examples
```

### 2. Create a virtual environment

```bash
# Create a virtual environment
python -m venv env

# Activate the virtual environment
# On Windows:
.\env\Scripts\activate

# On macOS/Linux:
source env/bin/activate
```

### 3. Configure API credentials

Create a `.env` file from the provided template:

```bash
# On Windows:
copy .env.example .env

# On macOS/Linux:
cp .env.example .env
```

Then edit the `.env` file and add your API key(s) for the LLM provider you want to use:
- For OpenAI models: Add your `OPENAI_API_KEY`
- For Google Gemini models: Add your `GEMINI_API_KEY`
- For Anthropic Claude models: Add your `ANTHROPIC_API_KEY`
- For local Ollama: No key needed, just ensure Ollama is running

### 4. Install dependencies

Install the necessary dependencies including the AI Blog App library:

```bash
pip install -r requirements.txt
```

### 5. Run the example

```bash
python main.py
```

This will start the multi-agent system, which will generate a blog post based on the topic defined in `main.py` (by default: "How to use AI for business ideas generation").

## Understanding the Output

When you run the example, you'll see:
1. The agents initializing
2. The Writer creating an initial draft
3. Multiple reviewers providing feedback
4. The Critic consolidating feedback
5. The Writer creating a final, improved version
6. The final blog post displayed in the console

## Customizing the Example

You can modify `main.py` to:
- Change the topic
- Select a different LLM provider and model (uncomment your preferred option)
- Add context for more grounded content generation
- Adjust the maximum word count

For more advanced usage, refer to the main [README.md](../README.md) in the project root.
