from typing import List

from pydantic import BaseModel, Field
from dotenv import load_dotenv

load_dotenv()
from langchain_core.messages import HumanMessage
from langchain.tools import tool
from langchain.agents import create_agent
from langchain_openai import ChatOpenAI
from langchain_tavily import TavilySearch

class Source(BaseModel):
    """Scheme for source used by the agent"""
    url:str = Field(description="The URL of the source")

class AgentResponse(BaseModel):
    """Scheme for agent repsonse"""
    answer: str = Field(description="Agent answer for a query")
    sources: List[Source] = Field(default_factory=list, description="List od sources used to generate the answer")



llm = ChatOpenAI(model="gpt-3.5-turbo")
tools = [TavilySearch()]
agent = create_agent(model=llm, tools=tools, response_format=AgentResponse)


def main():
    print("Hello")
    result = agent.invoke(
        {
            "messages": HumanMessage(
                content="Search for 3 used old porsches"
            )
        }

    )
    print(result)

if __name__ == "__main__":
    main()