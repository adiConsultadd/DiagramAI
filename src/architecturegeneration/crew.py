from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task
from architecturegeneration.tools.custom_tool import (
    PDFExtractorTool,
    SectionExtractorTool,
)
from crewai_tools import RagTool

@CrewBase
class Architecturegeneration:
    agents_config = "config/agents.yaml"
    tasks_config = "config/tasks.yaml"

    #---------------------------------------------------------------------------
    @agent
    def create_pdf_agent(self) -> Agent:
        pdf_tool = PDFExtractorTool()

        return Agent(
            config=self.agents_config["pdf_extracter"],
            verbose=True,
            allow_delegation=False,
            tools=[pdf_tool],
        )

    @agent
    def create_section_extraction_agent(self) -> Agent:
        section_tool = SectionExtractorTool()

        return Agent(
            config=self.agents_config["certain_section_extracter"],
            verbose=True,
            allow_delegation=False,
            tools=[section_tool],
        )

    @agent
    def section_json_to_steps_agent(self) -> Agent:
        return Agent(
            config=self.agents_config["section_json_to_steps"],
            verbose=True,
            allow_delegation=False,
        )

    @agent
    def rule_validation_agent(self) -> Agent:
        return Agent(
            config=self.agents_config["rule_validation_agent"],
            verbose=True,
            allow_delegation=False,
        )
    




    #---------------------------------------------------------------------------
    @task
    def create_pdf_extraction_task(self) -> Task:
        return Task(
            config=self.tasks_config["create_pdf_extraction_task"],
        )

    @task
    def create_section_extraction_task(self) -> Task:
        return Task(
            config=self.tasks_config["create_section_extraction_task"],
        )

    @task
    def create_section_json_to_steps_task(self) -> Task:
        return Task(
            config=self.tasks_config["generate_json"],
        )
    
    @task
    def rule_validation_task(self) -> Task:
        return Task(
            config=self.tasks_config["rule_validation_task"]
        )
    

    #---------------------------------------------------------------------------
    
    @crew
    def crew(self) -> Crew:
        return Crew(
            agents=self.agents,
            tasks=self.tasks,
            process=Process.sequential,
            verbose=True,
        )
