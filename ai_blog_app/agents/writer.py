from autogen_agentchat.agents import AssistantAgent

def create_writer(model_client):
    writer = AssistantAgent(
        name="Writer",
        system_message="You are a writer. You write engaging and concise " 
            "blogpost (with title) on given topics. You must polish your "
            "writing based on the feedback you receive and give a refined "
            "version. Only return your final work without additional comments.",
        model_client=model_client,
    )
    return writer
