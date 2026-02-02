from dotenv import load_dotenv
load_dotenv()

from langchain_classic import hub
from langchain_classic.agents import AgentExecutor
from langchain_classic.agents.react.agent import create_react_agent
from langchain_openai import ChatOpenAI
from langchain_tavily import TavilySearch

tools = [TavilySearch()]
llm = ChatOpenAI(model="gpt-3.5-turbo") 
react_prompt = hub.pull("hwchase17/react")
agent = create_react_agent(
    llm = llm,
    tools = tools,
    prompt = react_prompt,
)
agent_executor = AgentExecutor(agent=agent, tools=tools, verbose=True)
chain = agent_executor

def main():         
    result = chain.invoke( 
            input={
                "input": "Search for 3 junior ai engineer jobs in Poland",
            }
    )
    print(result)

if __name__ == "__main__":
    main()