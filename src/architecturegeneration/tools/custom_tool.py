import pdfplumber
from crewai.tools import BaseTool

class EnhancedPDFExtractorTool(BaseTool):
    name: str = "Enhanced PDF Extractor Tool"
    description: str = "Extracts complete and clean text from PDFs including bullet points and special symbols."

    def _run(self, file_path: str) -> str:
        try:
            content = ""
            with pdfplumber.open(file_path) as pdf:
                for page in pdf.pages:
                    text = page.extract_text()
                    if text:
                        # Normalize common bullet styles
                        cleaned_text = (
                            text.replace("•", "-")
                                .replace("◦", "-")
                                .replace("●", "-")
                                .replace("○", "-")
                                .replace("▪", "-")
                        )
                        content += cleaned_text + "\n\n"
            return content.strip() if content.strip() else "No text extracted."
        except Exception as e:
            return f"Failed to extract text: {str(e)}"

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
