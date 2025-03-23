from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task
from architecturegeneration.tools.custom_tool import (
    PDFExtractorTool,
    SectionExtractorTool,
)
from crewai.knowledge.source.csv_knowledge_source import CSVKnowledgeSource
from crewai.knowledge.source.text_file_knowledge_source import TextFileKnowledgeSource

from crewai_tools import RagTool


@CrewBase
class Architecturegeneration:
    agents_config = "config/agents.yaml"
    tasks_config = "config/tasks.yaml"

    csv_source = CSVKnowledgeSource(file_paths=["eraser_icons.csv"])
    text_source = TextFileKnowledgeSource(file_paths=["eraser_knowledge.md"])

    @agent
    def create_pdf_agent(self) -> Agent:
        pdf_tool = PDFExtractorTool()

        return Agent(
            config=self.agents_config["create_pdf_agent"],
            verbose=True,
            allow_delegation=False,
            tools=[pdf_tool],
        )

    @agent
    def create_section_extraction_agent(self) -> Agent:
        section_tool = SectionExtractorTool()

        return Agent(
            config=self.agents_config["create_section_extraction_agent"],
            verbose=True,
            allow_delegation=False,
            tools=[section_tool],
        )

    @agent
    def section_json_to_steps_agent(self) -> Agent:
        return Agent(
            config=self.agents_config["section_json_to_steps_agent"],
            verbose=True,
            allow_delegation=False,
            knowledge_sources=[self.csv_source],
        )

    @agent
    def rule_validation_agent(self) -> Agent:
        return Agent(
            config=self.agents_config["rule_validation_agent"],
            verbose=True,
            allow_delegation=False,
        )

    @agent
    def architecture_to_eraser_agent(self) -> Agent:
        # eraser_rag = RagTool(
        #     name="EraserDiagramKnowledge",
        #     description="Knowledge base about Eraser.io cloud architecture diagram syntax and best practices",
        #     knowledge_base_path="knowledge/eraser_docs/",
        #     top_k=5,
        # )

        return Agent(
            config=self.agents_config["architecture_to_eraser_agent"],
            verbose=True,
            allow_delegation=False,
            knowledge_sources=[self.text_source],
            # tools=[eraser_rag],
        )

    # ---------------------------------------------------------------------------
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
            config=self.tasks_config["create_section_json_to_steps_task"],
        )

    @task
    def rule_validation_task(self) -> Task:
        return Task(config=self.tasks_config["rule_validation_task"])

    @task
    def json_to_eraser_diagram_task(self) -> Task:
        return Task(
            config=self.tasks_config["json_to_eraser_diagram_task"],
        )

    # ---------------------------------------------------------------------------

    @crew
    def crew(self) -> Crew:
        """Creates the Architecturegeneration crew"""

        return Crew(
            agents=self.agents,
            tasks=self.tasks,
            process=Process.sequential,
            verbose=True,
        )
