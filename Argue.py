import autogen
import os
from dotenv import load_dotenv

load_dotenv()
api_key = os.getenv("API_KEY")

config_list = [
    {
        'model': 'gpt-4',
        'api_key': api_key,
    }
]

llm_config = {
    "timeout": 600,
    "seed": 42,  # for caching purposes
    "config_list": config_list,
    "temperature": 0
}

Republican = autogen.ConversableAgent(
    name="Republican",
    max_consecutive_auto_reply=10,
    llm_config=llm_config,
    system_message="I am a Republican politician, I am ready for a debate!"
)

Democrat = autogen.ConversableAgent(
    name="Democrat",
    max_consecutive_auto_reply=10,
    llm_config=llm_config,
    system_message="I am a Democrat politician, I am ready for a debate!"
)


debatetopic = """
Debate on the topic of gun control
"""

democrat = Democrat.initiate_chat(
    Republican,
    message=debatetopic
)

