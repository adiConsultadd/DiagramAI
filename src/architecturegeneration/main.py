import warnings
from datetime import datetime
from architecturegeneration.crew import Architecturegeneration

warnings.filterwarnings("ignore", category=SyntaxWarning, module="pysbd")


def run():
    pdf_url = "after-final_case_studies_20250319_190719.pdf"

    # sections_to_extract = input("Enter sections to extract (comma-separated): ").split(',')
    sections_to_extract = (
        "Solution Overview, Solution, Implementation, Solution Implementation"
    )
    sections_to_extract = [section.strip() for section in sections_to_extract]

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
        "workflow_steps": [
            {
                "step": 1,
                "title": "Step Title",
                "description": "Detailed description of the step",
                "components_involved": ["component-id-1", "component-id-2"],
                "icon": "appropriate-eraser-icon",
                "expected_outcome": "Description of the outcome of this step",
            }
        ],
        "metadata": {
            "diagram_title": "Title for the overall diagram",
            "diagram_description": "Description for the overall diagram",
            "layout_suggestion": "horizontal|vertical|nested|network",
            "color_scheme": "Suggested color scheme",
            "notes": "Any additional notes for diagram generation",
        },
        "external_systems": [
            {
                "id": "external-1",
                "name": "External System Name",
                "description": "Description of the external system",
                "icon": "appropriate-eraser-icon",
                "connections": [
                    {
                        "to_component_id": "component-id",
                        "label": "Description of connection",
                        "type": "data-flow|integration|api",
                        "icon": "appropriate-eraser-icon",
                    }
                ],
            }
        ],
    }

    print(sections_to_extract)

    inputs = {
        "pdf_url": pdf_url,
        "sections_to_extract": sections_to_extract,
        "jsonOutput": jsonOutput,
    }

    try:
        Architecturegeneration().crew().kickoff(inputs=inputs)
    except Exception as e:
        raise Exception(f"An error occurred while running the crew: {e}")
