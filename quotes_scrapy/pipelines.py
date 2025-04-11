# Import necessary modules from ReportLab
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas


class SaveQuotesToPDFPipeline:
    """
    Pipeline to save scraped quotes into a PDF file.
    """

    def __init__(self):
        # Initialize the PDF file and canvas
        self.file_path = "Quotes.pdf"  # Name of the output PDF file
        self.canvas = canvas.Canvas(self.file_path, pagesize=letter)
        (
            self.width,
            self.height,
        ) = letter  # Page dimensions (letter size: 612 x 792 points)
        self.y_position = self.height - 50  # Starting Y position for content
        self.line_height = 15  # Space between lines

    def process_item(self, item, spider):
        """
        Process each scraped item and add it to the PDF.
        """
        # Extract data from the item
        text = item.get("text", "No text")  # Quote text
        author = item.get("author", "Unknown author")  # Author name
        tags = ", ".join(item.get("tags", []))  # Tags as a comma-separated string

        # Add the quote to the PDF
        self.add_text_to_pdf(f'"{text}"')  # Add the quote text
        self.add_text_to_pdf(f"- {author}")  # Add the author
        self.add_text_to_pdf(f"Tags: {tags}")  # Add the tags
        self.add_text_to_pdf("")  # Add a blank line between quotes

        return item  # Return the item for further processing (if any)

    def add_text_to_pdf(self, text):
        """
        Helper method to add text to the PDF.
        Handles page breaks if the content exceeds the page height.
        """
        if self.y_position < 50:  # Check if we need a new page
            self.canvas.showPage()  # Start a new page
            self.y_position = self.height - 50  # Reset Y position

        self.canvas.drawString(50, self.y_position, text)  # Add text to the PDF
        self.y_position -= self.line_height  # Move down for the next line

    def close_spider(self, spider):
        """
        Called when the spider finishes crawling.
        Saves the PDF file and logs a message.
        """
        self.canvas.save()  # Save the PDF file
        spider.logger.info(f"PDF saved to {self.file_path}")  # Log the file location
