import os
import PyPDF2

# Define the full path to the source PDF file
source_pdf_path = "C:/Users/hasht/Downloads/Bank Statement kotak For SIP.pdf"  # Replace with your source PDF file's path

# Define the folder path where you want to save the first page PDF
output_folder = "C:/Users/hasht/Downloads/"  # Replace with your desired output folder

# Create a PDF reader object
pdf_reader = PyPDF2.PdfReader(source_pdf_path)
# Ensure the output folder exists; create it if it doesn't
os.makedirs(output_folder, exist_ok=True)

# create writer object
pdf_writer = PyPDF2.PdfWriter()

# Open the source PDF file
with open(source_pdf_path, 'rb') as pdf_file:            
    # Add the first page to the writer
    pdf_writer.add_page(pdf_reader.pages[0])
        
        # Define the full path for the first page PDF in the output folder
    first_page_pdf_path = os.path.join(output_folder, 'first_page.pdf')
        
        # Create a new PDF file for the first page
    with open(first_page_pdf_path, 'wb') as output_pdf:
            # Write the first page to the new PDF file
        pdf_writer.write(output_pdf)
# Close the source PDF file (not necessary, but good practice)
pdf_file.close()
