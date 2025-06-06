import fitz
import pandas as pd

def pdf_to_excel(pdf_file, excel_file):
    # Open the PDF
    pdf = fitz.open(pdf_file)
    data = []

    # Extract tables from each page (if they exist)
    for page_num in range(len(pdf)):
        page = pdf.load_page(page_num)
        text = page.get_text("text")

        # Here, you would need to parse tables from the text manually or use a tool to extract tables
        # Assuming some mock table extraction from text
        lines = text.splitlines()
        data.append(lines)

    # Convert to a DataFrame and save to Excel
    df = pd.DataFrame(data)
    df.to_excel(excel_file, index=False)
    print(f'Successfully converted {pdf_file} to {excel_file}')
