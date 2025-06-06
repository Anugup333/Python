import pandas as pd
from fpdf import FPDF

def excel_to_pdf(excel_file, pdf_file):
    df = pd.read_excel(excel_file)
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=10)

    # Writing the DataFrame to the PDF
    for row in df.itertuples():
        row_text = ' | '.join(map(str, row[1:]))
        pdf.cell(200, 10, txt=row_text, ln=True)

    pdf.output(pdf_file)
    print(f'Converted Excel to PDF: {pdf_file}')
