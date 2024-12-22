import os
from pypdf import PdfWriter

# Specify the folder containing my files (this is the old way - see new code below)
#folder_path = r"C:\Users\User\Desktop\Automating\Merging PDF files"

# Get the folder where the script is located
folder_path = os.path.dirname(os.path.abspath(__file__))

# Empty variable to store pdfs later on
pdfs = []

#print(os.listdir(folder_path))

# Loop through all files in the folder
for file_name in os.listdir(folder_path):
    # Construct the full file path
    file_path = os.path.join(folder_path, file_name)

    # Check if it's a file and ends with .pdf
    if os.path.isfile(file_path) and file_name.lower().endswith('.pdf'):
        pdfs.append(file_path)

print("PDF Files:", pdfs)

merger = PdfWriter()

for pdf in pdfs:
    merger.append(pdf)

merger.write("NewFile.pdf")
merger.close()

# Workflow for Bundling (Bundle of Documents for example)
# Step 1: Gather all PDFs in one folder
# Step 2: Open up Word File to use as index - insert date, description, and insert page number
# Step 3: Start arranging PDFs - while making sure its arrange according to date
# Step 4: Upload all PDFs in order - make sure the PDFs have page number at bottom (formatting is fix)
# Step 5: Turn Index (from word file) to PDF
# Step 6: Combine everything
# Step 7: Starting Double Checking