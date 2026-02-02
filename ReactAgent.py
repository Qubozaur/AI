from dotenv import load_dotenv

load_dotenv()
from langchain_core.messages import HumanMessage
from langchain.tools import tool
from langchain.agents import create_agent
from langchain_openai import ChatOpenAI
from tavily import TavilyClient

tavily = TavilyClient()

@tool
def search(query: str) -> str:
    """
    Search the web for information about the query
    Args:
        query: The query to search the web for
    Returns:
        The information found on the web    
    """
    print(f"Searching the web for {query}")
    return tavily.search(query=query) 

llm = ChatOpenAI(model="gpt-3.5-turbo")
tools = [search]
agent = create_agent(model=llm, tools=tools)

def main():
    print("Hello, World!")
    result = agent.invoke({"messages": [HumanMessage(content="Search for 3 job postings for ai junior engineer in Poland")]})
    print(result)



if __name__ == "__main__":
    main()