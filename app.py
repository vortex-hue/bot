import os
from slack_bolt import App
from slack_bolt.adapter.socket_mode import SocketModeHandler
from langchain.llms import OpenAI as LangChainOpenAI
from langchain.chains import LLMChain
from langchain.prompts import PromptTemplate

# Load environment variables
slack_bot_token = os.getenv("SLACK_BOT_TOKEN")
openai_api_key = os.getenv("OPENAI_API_KEY")

# Initialize the Slack app
app = App(token=slack_bot_token)

# Langchain OpenAI setup
openai_llm = LangChainOpenAI(api_key=openai_api_key)

# Define the prompt template
template = """
Assistant is a large language model trained by OpenAI. 
{history} 
Human: {human_input} 
Assistant:"""

prompt_template = PromptTemplate(
    input_variables=["history", "human_input"],
    template=template
)

# Initialize LLMChain
chatgpt_chain = LLMChain(
    llm=openai_llm,
    prompt=prompt_template,
    verbose=True
)

# Define the message handler
@app.message(".*")
def message_handler(message, say):
    user_input = message['text']
    response = chatgpt_chain.predict(human_input=user_input)
    say(response)

# Start the app
if __name__ == "__main__":
    handler = SocketModeHandler(app, os.getenv("SLACK_APP_TOKEN"))
    handler.start()
