from typing import Optional
from crewai.tools import BaseTool
from langchain_community.document_loaders import PyPDFLoader
from proto import Field


class PDFExtractorTool(BaseTool):
    name: str = "PDF Text Extractor"
    description: str = "Extracts text from a PDF file at the given path"

    def _run(self, pdf_path: str) -> str:
        """Extract text from a PDF file."""
        try:
            loader = PyPDFLoader(pdf_path)
            documents = loader.load()
            text = "\n".join([doc.page_content for doc in documents])
            return text
        except Exception as e:
            return f"Error extracting text from PDF: {str(e)}"


class SectionExtractorTool(BaseTool):
    name: str = "Section Extractor"
    description: str = "Extracts specific sections from text based on section headings"

    def _run(self, text: str, section_names: list) -> dict:
        """Extract specific sections from text."""
        results = {}
        lines = text.split("\n")

        current_section = None
        section_content = []

        # List of possible section markers
        markers = [f"{i}. " for i in range(1, 10)] + [f"{i}." for i in range(1, 10)]

        for line in lines:
            line_stripped = line.strip()

            # Check if this line is a section header we're looking for
            found_new_section = False
            for section in section_names:
                for marker in markers:
                    if (
                        line_stripped == section
                        or line_stripped == f"{marker}{section}"
                        or line_stripped == f"{marker} {section}"
                    ):
                        # If we were collecting content for a previous section, save it
                        if current_section in section_names:
                            results[current_section] = "\n".join(
                                section_content
                            ).strip()

                        # Start new section
                        current_section = section
                        section_content = []
                        found_new_section = True
                        break

                # Also check for exact matches without numbering
                if line_stripped == section:
                    if current_section in section_names:
                        results[current_section] = "\n".join(section_content).strip()
                    current_section = section
                    section_content = []
                    found_new_section = True
                    break

            if found_new_section:
                continue

            # Check if we've reached the next section (which we're not interested in)
            for marker in markers:
                if (
                    line_stripped.startswith(marker)
                    and current_section in section_names
                ):
                    # We've hit a new numbered section, save the current one
                    results[current_section] = "\n".join(section_content).strip()
                    current_section = None
                    break

            # Add the line to the current section if we're tracking one
            if current_section in section_names:
                section_content.append(line)

        # Add the final section if we were collecting one
        if current_section in section_names:
            results[current_section] = "\n".join(section_content).strip()

        return results


# class SolutionToJSONTool(BaseTool):
#     """Tool for converting solution text to structured JSON architecture"""

#     name: str = "Solution to JSON Converter"
#     description: str = (
#         "Converts solution text to a structured JSON format for architecture diagrams"
#     )

#     solution_text: str = Field(..., description="Solution text to convert to JSON")

#     def _run(self, solution_text: Optional[str] = None) -> str:
#         """Convert solution text to structured JSON for architecture diagram"""
#         text = solution_text or self.solution_text

#         try:
#             # The LLM should handle this transformation in the agent's execution
#             # This tool primarily serves as a capability marker for the agent
#             return text
#         except Exception as e:
#             return f"Error converting solution to JSON: {str(e)}"
