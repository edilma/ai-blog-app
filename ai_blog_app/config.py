import json
import os
from pathlib import Path
from dotenv import load_dotenv

from autogen_ext.models.openai import OpenAIChatCompletionClient
from autogen_core.models import ModelInfo

# Load environment variables from .env file
load_dotenv(dotenv_path=Path(__file__).parent.parent / "examples" / ".env")


def create_model_client(provider="openai", model="gpt-3.5-turbo"):
    
    config_path = Path(__file__).parent / "llm_config.json"
    
    if not config_path.exists():
        raise FileNotFoundError("llm_config.json not found in ai_blog_app/")

    with open(config_path) as f:
        config_list = json.load(f)

    for config in config_list:
        if config["provider"] == provider:
            # Support environment variable substitution like ${GEMINI_API_KEY}
            api_key = os.path.expandvars(config.get("api_key", ""))
            
            return OpenAIChatCompletionClient(
            model=model,
            api_key=api_key,
            base_url=config.get("base_url"),
            model_info=ModelInfo(
                vision=True,
                function_calling=True,
                json_output=True,
                family=config["provider"],
                structured_output=True
            )
        )

    raise ValueError(f"Provider '{provider}' not found in llm_config.json")
