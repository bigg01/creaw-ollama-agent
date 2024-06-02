from crewai import Agent, Task, Crew, Process

from langchain_community.llms import Ollama
ollama_llm = Ollama(model="codellama")


from langchain_community.tools import DuckDuckGoSearchRun
search_tool = DuckDuckGoSearchRun()



researcher = Agent(
  role='CloudArchitect',
  goal='best practices for deploying a web app on Azure using Kubernetes',
  backstory="""
  you are a cloud architect and you need to find information on a topic. 
  Azure is your preferred cloud provider and you are looking for information on how to deploy a web app on Azure.
  Kubernetes is your preferred container orchestration tool.
  """,
  verbose=True,
  allow_delegation=False,
  tools=[search_tool],
  llm=ollama_llm
)

writer = Agent(
  role='DevOpsEngineer',
  goal='create terraform scripts to deploy a web app on Azure',
  backstory="""
  you are a DevOps engineer and you need to create terraform scripts to deploy a web app on Azure.
  Kubernetes is your preferred container orchestration tool.
  """,
  verbose=True,
  allow_delegation=True,
  llm=ollama_llm
)

task1 = Task(
  description="""Search for information on how to deploy a web app on Azure using Kubernetes""",
  agent=researcher,
  expected_output=""
)

task2 = Task(
  description="""Create terraform scripts to deploy a web app on Azure using Kubernetes""",
  agent=writer,
  expected_output=""
)

crew = Crew(
  agents=[researcher, writer],
  tasks=[task1, task2],
  verbose=2,
)

result = crew.kickoff()