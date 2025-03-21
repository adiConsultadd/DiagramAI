from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task
from architecturegeneration.tools.custom_tool import (
    PDFExtractorTool,
    SectionExtractorTool,
)
from crewai.knowledge.source.csv_knowledge_source import CSVKnowledgeSource


@CrewBase
class Architecturegeneration:
    agents_config = "config/agents.yaml"
    tasks_config = "config/tasks.yaml"

    csv_source = CSVKnowledgeSource(file_paths=["eraser_icons.csv"])

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
            knowledge_sources=[self.csv_source],
        )

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

    @crew
    def crew(self) -> Crew:
        """Creates the Architecturegeneration crew"""

        return Crew(
            agents=self.agents,
            tasks=self.tasks,
            process=Process.sequential,
            verbose=True,
        )
