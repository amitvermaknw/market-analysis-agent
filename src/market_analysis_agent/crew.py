import os
from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task
from crewai.agents.agent_builder.base_agent import BaseAgent
from typing import List
from crewai import LLM
from crewai_tools import SerperDevTool, ScrapeWebsiteTool, WebsiteSearchTool
from market_analysis_agent.models import ContentOutput

# If you want to run a snippet of code before or after the crew starts,
# you can use the @before_kickoff and @after_kickoff decorators
# https://docs.crewai.com/concepts/crews#example-crew-class-with-decorators

@CrewBase
class MarketAnalysisAgent():
    """Market Analysis Agent crew"""

    agents: List[BaseAgent]
    tasks: List[Task]

    def __init__(self):
        self.groq_llm = LLM(
            model="groq/llama-3.3-70b-versatile",
            api_key=os.environ["GROQ_API_KEY"]
        )

    # Learn more about YAML configuration files here:
    # Agents: https://docs.crewai.com/concepts/agents#yaml-configuration-recommended
    # Tasks: https://docs.crewai.com/concepts/tasks#yaml-configuration-recommended
    
    # If you would like to add tools to your agents, you can learn more about it here:
    # https://docs.crewai.com/concepts/agents#agent-tools
    @agent
    def market_news_monitor_agent(self) -> Agent:
        return Agent(
            config=self.agents_config['market_news_monitor_agent'], 
            verbose=True,
            tools=[SerperDevTool(), ScrapeWebsiteTool()],
            llm=self.groq_llm
        )

    @agent
    def data_analyst_agent(self) -> Agent:
        return Agent(
            config=self.agents_config['data_analyst_agent'], 
            verbose=True,
            tools=[SerperDevTool(), WebsiteSearchTool()],
            llm = self.groq_llm
        )
    
    @agent
    def content_creator_agent(self) -> Agent:
        return Agent(
            config=self.agents_config['content_creator_agent'],
            tools=[SerperDevTool(), WebsiteSearchTool()]
        )
    
    @agent
    def quality_assurance_agent(self) -> Agent:
        return Agent(
            config=self.agents_config['quality_assurance_agent']
        )

    # To learn more about structured task outputs,
    # task dependencies, and task callbacks, check out the documentation:
    # https://docs.crewai.com/concepts/tasks#overview-of-a-task
    @task
    def monitor_financial_news_task(self) -> Task:
        return Task(
            config=self.tasks_config['monitor_financial_news'], 
            agent=self.market_news_monitor_agent
        )

    @task
    def analyze_market_data_task(self) -> Task:
        return Task(
            config=self.tasks_config['analyze_market_data'], 
            agent=self.data_analyst_agent
        )

    @task
    def create_content_task(self) -> Task:
        return Task(
            config=self.tasks_config['create_content'],
            agent=self.content_creator_agent,
            context=[self.monitor_financial_news_task, self.analyze_market_data_task]
        )
    
    @task
    def quality_assurance_task(self)-> Task:
        return Task(
            config=self.tasks_config['quality_assurance'],
            agent=self.quality_assurance_agent,
            output_pydantic=ContentOutput,
            output_file='output/social_media_posts.md'
        )
    
    @crew
    def crew(self) -> Crew:
        """Creates the MarketAnalysisAgent crew"""

        return Crew(
            agents=self.agents, 
            tasks=self.tasks, 
            process=Process.sequential,
            verbose=True,
        )
