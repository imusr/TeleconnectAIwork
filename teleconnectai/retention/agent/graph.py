from langgraph.graph import StateGraph
from langgraph.graph import START, END

from langgraph.prebuilt import ToolNode
# from retention.agent.state import AgentState
# from retention.agent.nodes import chatbot_node
from retention.agent.tools import TOOLS

from langgraph.prebuilt import tools_condition

from typing import TypedDict, Annotated
import operator

from langchain_core.messages import AnyMessage
from retention.agent.graph_llm import llm



class AgentState(TypedDict):
    messages: Annotated[list[AnyMessage], operator.add]


def chatbot_node(state):
    response = llm.invoke(state["messages"])
    return {
        "messages": [response]
    }


builder = StateGraph(AgentState)


builder.add_node("chatbot", chatbot_node)
builder.add_node("tools", ToolNode(TOOLS))

builder.add_conditional_edges("chatbot", tools_condition, {"tools": "tools", END: END})

builder.add_edge("tools", "chatbot")
builder.add_edge(START, "chatbot")


graph_app = builder.compile()


