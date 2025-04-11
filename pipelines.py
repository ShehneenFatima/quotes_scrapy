from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas


class SaveQuotesToPDFPipeline:
    def __init__(self):
        # Initialize the PDF file and canvas
        self.file_path = "Quotes.pdf"
        self.canvas = canvas.Canvas(self.file_path, pagesize=letter)
        self.width, self.height = letter  # Page dimensions
        self.y_position = self.height - 50  # Starting Y position for content
        self.line_height = 15  # Space between lines

    def process_item(self, item, spider):
        # Extract data from the item
        text = item.get("text", "No text")
        author = item.get("author", "Unknown author")
        tags = ", ".join(item.get("tags", []))

        # Add the quote to the PDF
        self.add_text_to_pdf(f'"{text}"')
        self.add_text_to_pdf(f"- {author}")
        self.add_text_to_pdf(f"Tags: {tags}")
        self.add_text_to_pdf("")  # Add a blank line between quotes

        return item

    def add_text_to_pdf(self, text):
        """Helper method to add text to the PDF."""
        if self.y_position < 50:  # Check if we need a new page
            self.canvas.showPage()  # Start a new page
            self.y_position = self.height - 50  # Reset Y position

        self.canvas.drawString(50, self.y_position, text)  # Add text to the PDF
        self.y_position -= self.line_height  # Move down for the next line

    def close_spider(self, spider):
        # Save the PDF when the spider finishes
        self.canvas.save()
        spider.logger.info(f"PDF saved to {self.file_path}")
