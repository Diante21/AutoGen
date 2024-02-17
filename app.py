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

assistant = autogen.AssistantAgent(
    name="assistant",
    llm_config=llm_config,
    system_message="I am an AI assistant, ask me anything!"
)

# human_input_mode has 3 options: "ALWAYS", "TERMINATE", "NEVER"
# "ALWAYS" - always ask for human input
# "TERMINATE" - ask for human input if the assistant is not confident
# "NEVER" - never ask for human input

user_proxy = autogen.UserProxyAgent(
    name="user_proxy",
    human_input_mode="NEVER",
    max_consecutive_auto_reply=10,
    is_termination_msg=lambda x: x.get("content", "").rstrip().endswith("TERMINATE"),  # Terminate if the message ends
    # with "TERMINATE"
    code_execution_config={"work_dir": "web", "use_docker": True},
    llm_config=llm_config,
    system_message="""reply TERMINATE if the task has been solved at full satisfaction, otherwise ask for more information
    otherwise, reply CONTINUE, or the reason why the task is not solved yet."""
)


task = """ 
Write python code to output numbers 1 to 100, and then store the code in a file
"""

user_proxy.initiate_chat(
    assistant,
    message=task
)

task2 = """
Change the code in the numbers.py you just created to output numbers 1 to 200
"""

user_proxy.initiate_chat(
    assistant,
    message=task2
)
