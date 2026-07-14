from dotenv import load_dotenv
load_dotenv()

from langchain_openai import ChatOpenAI
from retention.agent.tools import TOOLS


llm = ChatOpenAI(model="gpt-5.5", temperature=0)

llm = llm.bind_tools(TOOLS)