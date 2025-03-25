import warnings
from architecturegeneration.crew import Architecturegeneration

warnings.filterwarnings("ignore", category=SyntaxWarning, module="pysbd")


def run():
    pdf_url = "case_studies/case_study (1).pdf"
    json_url = "validation.rule.json"

    pdf_text_url = "output/pdf_text.json"
    extracted_text_url = "output/extacted_text.json"
    diagram_json_url = "output/diagram.json"

    # sections_to_extract = "Solution Implementation  overview"

    sections_to_extract_list = [
        "Problem",
        "Solution Implementation",
        "Solution Overview",
    ]

    jsonOutput = {
        "solution": {
            "title": "Solution Title",
            "overview": "High-level description of the proposed solution",
        },
        "components": [
            {
                "id": "component-1",
                "name": "Component Name",
                "description": "Detailed description of the component's functionality",
                "technology": "Technologies used (e.g., HL7, FHIR, AWS)",
                "icon": "appropriate-eraser-icon",
                "category": "infrastructure|application|data|security|integration|user",
                "parent_id": "null",
            }
        ],
        "groups": [
            {
                "id": "group-1",
                "name": "Group Name",
                "description": "Description of the group's purpose",
                "icon": "appropriate-eraser-icon",
                "components": ["component-id-1", "component-id-2"],
            }
        ],
        "connections": [
            {
                "source_id": "component-1 or group-1",
                "target_id": "component-2 or group-2",
                "label": "Description of the connection",
                "type": "data-flow|dependency|integration|api|reference",
                "direction": "unidirectional|bidirectional",
                "icon": "appropriate-eraser-icon",
            }
        ],
    }

    inputs = {
        "pdf_url": pdf_url,
        "sections_to_extract": sections_to_extract_list,
        "jsonOutput": jsonOutput,
        "json_url": json_url,
        "pdf_text_url": pdf_text_url,
        "extracted_text_url": extracted_text_url,
        "diagram_json_url": diagram_json_url,
    }

    try:
        Architecturegeneration().crew().kickoff(inputs=inputs)
    except Exception as e:
        raise Exception(f"An error occurred while running the crew: {e}")
