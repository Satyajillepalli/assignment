import os
import json
import requests
import PyPDF2
from PyPDF2 import PdfFileReader, PdfFileWriter
from PIL import Image
from PyPDF2 import PdfMerger


class PDFProcessor:
    def __init__(self, public_key, secret_key):
        self.public_key = public_key
        self.secret_key = secret_key
        self.api_base_url = "https://api.ilovepdf.com/v1"

    def authenticate_with_ilovepdf(self,public_key, secret_key):
        base_url = "https://api.ilovepdf.com/v1/"
        session = requests.Session()

    # Set up the authentication headers using the provided public and secret keys
        headers = {
        "Authorization": f"Bearer {public_key}:{secret_key}"
        }
        session.headers.update(headers)
        return session

 #implementation of combine _pdfs
    def combine_pdfs(self,output_pdf_path, pdf_files):
        try:
            pdf_merger = PyPDF2.PdfFileMerger()

            for pdf_file in pdf_files:
              pdf_merger.append(pdf_file)

              pdf_merger.write(output_pdf_path)
              pdf_merger.close()

              print("PDFs combined successfully!")
        except Exception as e:
            print(f"An error occurred: {str(e)}")


#implementation of separate_pages_to_directory
    def separate_pages_to_directory(self,input_pdf, output_directory):
        try:
        # Ensure the output directory exists
            os.makedirs(output_directory, exist_ok=True)
            pdf = PdfFileReader(input_pdf)
            total_pages = pdf.getNumPages()
            for page_num in range(total_pages):
                page = pdf.getPage(page_num)
                pdf_writer = PdfFileWriter()
                pdf_writer.addPage(page)

            # Construct the output PDF file path
                output_file = os.path.join(output_directory, f"page_{page_num + 1}.pdf")

            # Write the single-page PDF to the output file
                with open(output_file, "wb") as output_pdf:
                    pdf_writer.write(output_pdf)

                print(f"PDF pages separated and saved to '{output_directory}'")
        except Exception as e:
            print(f"An error occurred: {str(e)}")
       

    #implementation of remove_password_security
    def remove_password_security(self,input_pdf, output_pdf, password):
        try:
            pdf = PyPDF2.PdfFileReader(input_pdf)
            pdf_writer = PyPDF2.PdfFileWriter()

            if pdf.decrypt(password):
                for page_num in range(pdf.numPages):
                    page = pdf.getPage(page_num)
                    pdf_writer.addPage(page)

                with open(output_pdf, "wb") as output_file:
                    pdf_writer.write(output_file)

                print("Password security removed. Save the PDF to:", output_pdf)
            else:
                print("Unable to remove password security. Please provide the correct password.")
        except Exception as e:
            print(f"An error occurred: {str(e)}")

    # implementation of extract_text_to_text_file
    def extract_text_to_text_file(self,input_pdf, output_text_file):
        try:
            pdf = PyPDF2.PdfFileReader(input_pdf)
            total_pages = pdf.getNumPages()

            with open(output_text_file, "w", encoding="utf-8") as text_file:
                for page_num in range(total_pages):
                    page = pdf.getPage(page_num)
                    text = page.extractText()
                    text_file.write(text)

            print(f"Text extracted and saved to '{output_text_file}'")
        except Exception as e:
            print(f"An error occurred: {str(e)}")


    def convert_images_to_pdf(self,image_files, output_pdf):
        try:
        # Create a list to store PIL Image objects
           images = []
  
        # Open and append each image to the list
           for image_file in image_files:
               img = Image.open(image_file)
               images.append(img)

        # Save the list of images as a PDF
           images[0].save(output_pdf, save_all=True, append_images=images[1:])

           print(f"Images converted to PDF and saved to '{output_pdf}'")
        except Exception as e:
            print(f"An error occurred: {str(e)}")


# Additional methods can be added for other features.

if __name__ == "__main__":
    # Load API credentials from creds.json
    with open('creds.json', 'r') as creds_file:
        creds = json.load(creds_file)

    pdf_processor = PDFProcessor(creds["public_key"], creds["secret_key"])
    pdf_processor.authenticate()
