import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox
import pdf_to_word as pw
import word_to_pdf as wp
import pdf_to_excel as pe
import excel_to_pdf as ep

def convert_pdf_to_word():
    pdf_file = filedialog.askopenfilename(filetypes=[("PDF Files", "*.pdf")])
    if pdf_file:
        word_file = filedialog.asksaveasfilename(defaultextension=".docx", filetypes=[("Word Files", "*.docx")])
        pw.pdf_to_word(pdf_file, word_file)

def convert_word_to_pdf():
    word_file = filedialog.askopenfilename(filetypes=[("Word Files", "*.docx")])
    if word_file:
        pdf_file = filedialog.asksaveasfilename(defaultextension=".pdf", filetypes=[("PDF Files", "*.pdf")])
        wp.word_to_pdf(word_file, pdf_file)

def convert_pdf_to_excel():
    pdf_file = filedialog.askopenfilename(filetypes=[("PDF Files", "*.pdf")])
    if pdf_file:
        excel_file = filedialog.asksaveasfilename(defaultextension=".xlsx", filetypes=[("Excel Files", "*.xlsx")])
        pe.pdf_to_excel(pdf_file, excel_file)

def convert_excel_to_pdf():
    excel_file = filedialog.askopenfilename(filetypes=[("Excel Files", "*.xlsx")])
    if excel_file:
        pdf_file = filedialog.asksaveasfilename(defaultextension=".pdf", filetypes=[("PDF Files", "*.pdf")])
        ep.excel_to_pdf(excel_file, pdf_file)

# GUI Setup
root = tk.Tk()
root.title("File Converter")

# Buttons for conversion
btn_pdf_to_word = tk.Button(root, text="Convert PDF to Word", command=convert_pdf_to_word)
btn_pdf_to_word.pack(pady=10)

btn_word_to_pdf = tk.Button(root, text="Convert Word to PDF", command=convert_word_to_pdf)
btn_word_to_pdf.pack(pady=10)

btn_pdf_to_excel = tk.Button(root, text="Convert PDF to Excel", command=convert_pdf_to_excel)
btn_pdf_to_excel.pack(pady=10)

btn_excel_to_pdf = tk.Button(root, text="Convert Excel to PDF", command=convert_excel_to_pdf)
btn_excel_to_pdf.pack(pady=10)

root.mainloop()
