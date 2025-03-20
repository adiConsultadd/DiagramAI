from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task
from architecturegeneration.tools.custom_tool import PDFExtractorTool, SectionExtractorTool

@CrewBase
class Architecturegeneration():
    agents_config = 'config/agents.yaml'
    tasks_config = 'config/tasks.yaml'

    @agent
    def create_pdf_agent(self) -> Agent:
        pdf_tool = PDFExtractorTool()
        
        return Agent(
            config=self.agents_config['pdf_extracter'],
            verbose=True,
            allow_delegation=False,
            tools=[pdf_tool],
        )

    @agent
    def create_section_extraction_agent(self) -> Agent :
        section_tool = SectionExtractorTool()
        
        return Agent(
            config=self.agents_config['certain_section_extracter'],
            verbose=True,
            allow_delegation=False,
            tools=[section_tool],
        )

    @task
    def create_pdf_extraction_task(self) -> Task:
        return Task(
            config=self.tasks_config['create_pdf_extraction_task'],
            # inputs={"pdf_url": pdf_url},
        )

    @task
    def create_section_extraction_task(self) -> Task:
        return Task(
           config=self.tasks_config['create_section_extraction_task'],
        #    inputs={
        #         "extracted_text": extracted_text,
        #         "sections_to_extract": sections_to_extract
        #     },
        )

    @crew
    def crew(self) -> Crew:
        """Creates the Architecturegeneration crew"""
        # print(pdf_url)
        # pdf_task = self.create_pdf_extraction_task(pdf_url=pdf_url)
        # section_task = self.create_section_extraction_task(extracted_text=pdf_task.output, sections_to_extract=sections_to_extract)
        return Crew(
            agents=self.agents,
            tasks=self.tasks,
            process=Process.sequential,
            verbose=True,
        )
