from langchain.agents import create_agent

from hr_assistant import config

def create_hr_agent(llm,tools):
    """Return Langchain agent that can callour tools to answer questions."""
    return create_agent(
        model=llm,
        tools = tools,
        system_prompt=config.SYSTEM_PROMPT
    )