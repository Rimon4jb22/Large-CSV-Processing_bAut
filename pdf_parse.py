#get_certen_section_of_some_pdf

import os
from PyPDF2 import PdfReader

# Specify the directory containing the PDF files
pdf_directory = r" #the_path "

# Specify the output file path
output_file = "output.txt"

# Open the output file in append mode
with open(output_file, "a") as output:
    # Iterate over the PDF files in the directory
    for filename in os.listdir(pdf_directory):
        if filename.endswith(".pdf"):
            pdf_path = os.path.join(pdf_directory, filename)

            # Open the PDF file in read-binary mode
            with open(pdf_path, "rb") as pdf_file:
                reader = PdfReader(pdf_file)

                # Iterate over the pages in the PDF
                for page_num, page in enumerate(reader.pages):
                    text = page.extract_text()

                    # Check if the section title contains "disaggregation"
                    if "disaggregation" in text.lower():
                        # Find the index of the section title
                        start_index = text.lower().index("disaggregation")

                        # Find the index of the next section title or end of the document
                        end_index = text.lower().index("disaggregation",
                                                       start_index + 1) if "disaggregation" in text.lower()[
                                                                                               start_index + 1:] else len(
                            text)

                        # Extract the section text
                        section_text = text[start_index:end_index].strip()

                        # Write the section text to the output file
                        output.write(
                            "File: {}\nPage: {}\nSection:\n{}\n\n".format(filename, page_num + 1, section_text))
