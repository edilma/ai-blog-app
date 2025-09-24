from importlib.resources import files
import json
import os
from dotenv import load_dotenv
from autogen_ext.models.openai import OpenAIChatCompletionClient
from autogen_core.models import ModelInfo


def create_model_client(provider="openai", model="gpt-3.5-turbo"):
    load_dotenv()

    # Access llm_config.json bundled in the package
    config_path = files('ai_blog_app').joinpath("llm_config.json")
    
    with config_path.open("r", encoding="utf-8") as f:
        config_list = json.load(f)

    for config in config_list:
        if config["provider"] == provider:
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
