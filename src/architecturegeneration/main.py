import warnings
from datetime import datetime
from architecturegeneration.crew import Architecturegeneration
warnings.filterwarnings("ignore", category=SyntaxWarning, module="pysbd")


def run():
    pdf_url = "after-final_case_studies_20250319_190719.pdf"
    
    # sections_to_extract = input("Enter sections to extract (comma-separated): ").split(',')
    sections_to_extract = "Solution Overview, Solution, Implementation, Solution Implementation"
    sections_to_extract = [section.strip() for section in sections_to_extract] 

    print(sections_to_extract)

    inputs = {"pdf_url": pdf_url, "sections_to_extract": sections_to_extract}
    
    try:
        Architecturegeneration().crew().kickoff(inputs=inputs)
    except Exception as e:
        raise Exception(f"An error occurred while running the crew: {e}")
