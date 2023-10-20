import json
from pp_tool.pdf_tool import PDFProcessor
import PyPDF2
from PIL import Image
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
import os
from PyPDF2 import PdfMerger



if __name__ == "__main__":
    # Load API credentials from creds.json
    with open('creds.json', 'r') as creds_file:
        creds = json.load(creds_file)

    pdf_processor = PDFProcessor(creds["public_key"], creds["secret_key"])
    
    while True:
        print("PDF Processing Menu:")
        print("1. Combine PDFs")
        print("2. Separate PDF Pages")
        print("3. Remove PDF Password")
        print("4. Extract Text from PDF")
        print("5. Convert Images to PDF")
        print("6. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            # Implement the logic for combining PDFs
            
                print("Combine PDFs")

    # Get the input PDF files to be combined
                pdf_merger = PdfMerger()

            # Add the PDF files to merge
                pdf_merger.append(r'C:\Users\satya\OneDrive\Desktop\assignment\pdf_files\file1.pdf')
                pdf_merger.append(r'C:\Users\satya\OneDrive\Desktop\assignment\pdf_files\file2.pdf')

            # Save the merged PDF to an output file
                pdf_merger.write('output.pdf')
                pdf_merger.close()

                print("PDFs combined successfully!")
                
    

            
        elif choice == "2":
            print("Separate PDF Pages")
            #Implement the logic for Separate PDF Pages
            input_file = input("Enter the path of the input PDF file: ")
            output_dir = input("Enter the output directory to save separated pages: ")

    # Perform the PDF page separation
            try:
                pdf_file = open(input_file, 'rb')
                pdf_reader = PyPDF2.PdfFileReader(pdf_file)

                if not pdf_reader.isEncrypted:
                    num_pages = pdf_reader.numPages

            # Create the output directory if it doesn't exist
                    os.makedirs(output_dir, exist_ok=True)

            # Iterate through each page and save it as a separate PDF
                for page_number in range(num_pages):
                    pdf_writer = PyPDF2.PdfFileWriter()
                    pdf_writer.addPage(pdf_reader.getPage(page_number))

                    output_file = os.path.join(output_dir, f'page_{page_number + 1}.pdf')
                    with open(output_file, 'wb') as output_pdf:
                        pdf_writer.write(output_pdf)
                        print(f"PDF pages separated successfully. The pages are saved in '{output_dir}'.")
                else:
                    print("Error: The input PDF is encrypted. Please provide an unencrypted PDF.")
            except Exception as e:
                print(f"Error: {e}")

           
        elif choice == "3":
            print("Remove PDF Password")

    # Get the input PDF file with a password
            input_file = input("Enter the path of the password-protected PDF file: ")
            password = input("Enter the PDF password: ")

    # Get the output file name
            output_file = input("Enter the name of the output PDF file (without password): ")

    # Perform the PDF password removal
            try:
                pdf_reader = PyPDF2.PdfFileReader(open(input_file, 'rb'))

                if pdf_reader.isEncrypted:
                    pdf_reader.decrypt(password)
                    pdf_writer = PyPDF2.PdfFileWriter()

                    for page_number in range(pdf_reader.getNumPages()):
                       pdf_writer.addPage(pdf_reader.getPage(page_number))

                    with open(output_file, 'wb') as output_pdf:
                        pdf_writer.write(output_pdf)

                    print(f"Password removed successfully. The unencrypted PDF is saved as '{output_file}'.")
                else:
                    print("Error: The input PDF is not password-protected.")
            except Exception as e:
                print(f"Error: {e}")

        elif choice == "4":
            print("Extract Text from PDF")

    # Get the input PDF file
            input_file = input("Enter the path of the PDF file from which you want to extract text: ")

    # Get the output text file name
            output_file = input("Enter the name of the output text file: ")

    # Perform PDF text extraction
            try:
                pdf_file = open(input_file, 'rb')
                pdf_reader = PyPDF2.PdfFileReader(pdf_file)
                text = ""

                for page_number in range(pdf_reader.getNumPages()):
                   page = pdf_reader.getPage(page_number)
                   text += page.extractText()

                with open(output_file, 'w', encoding='utf-8') as output_text:
                    output_text.write(text)

                print(f"Text extracted successfully. The text is saved in '{output_file}'.")
            except Exception as e:
                print(f"Error: {e}")

        elif choice == "5":
            print("Convert Images to PDF")

    # Get the input image files (JPG, TIFF, and PNG)
            input_files = []
            num_images = int(input("Enter the number of image files to convert: "))

            for i in range(num_images):
               file_path = input(f"Enter the path of image file {i + 1} (JPG, TIFF, or PNG): ")
               input_files.append(file_path)

    # Get the name of the output PDF file
            output_file = input("Enter the name of the output PDF file: ")

    # Perform the image to PDF conversion
            try:
               c = canvas.Canvas(output_file, pagesize=letter)
               width, height = letter

               for file_path in input_files:
                    img = Image.open(file_path)
                    img_width, img_height = img.size
                    aspect_ratio = img_width / img_height

                    if img_width > width:
                        img_width = width
                        img_height = img_width / aspect_ratio

                    if img_height > height:
                        img_height = height
                        img_width = img_height * aspect_ratio

                    c.drawImage(file_path, 0, 0, width=img_width, height=img_height)
                    c.showPage
                    c.save()
                    print(f"Images converted to PDF successfully. The PDF is saved as '{output_file}'.")
            except Exception as e:
                print(f"Error: {e}")

            
        elif choice == "6":
            print("Exiting the application.")
            break
        else:
            print("Invalid choice. Please try again.")

    
    
