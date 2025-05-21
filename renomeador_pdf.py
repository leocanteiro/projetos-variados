import os
import PyPDF2
import tkinter as tk
from tkinter import filedialog

def extract_first_line(pdf_path):
    with open(pdf_path, 'rb') as file:
        pdf_reader = PyPDF2.PdfReader(file)
        first_page = pdf_reader.pages[0]
        text = first_page.extract_text()
        first_line = text.split('\n')[0]
        produto_index = first_line.find('PRODUTO')
        if produto_index != -1:
            return first_line[produto_index + 7:].strip()
    return None

def rename_pdf(pdf_path, new_name):
    pdf_dir = os.path.dirname(pdf_path)
    pdf_name = os.path.basename(pdf_path)
    new_pdf_path = os.path.join(pdf_dir, new_name + '.pdf')

    counter = 1
    while os.path.exists(new_pdf_path):
        print(f"Arquivo '{new_pdf_path}' já existente. Tentando um nome diferente.")
        new_pdf_path = os.path.join(pdf_dir, f"{new_name}_{counter}.pdf")
        counter += 1

    os.rename(pdf_path, new_pdf_path)
    print(f"File '{pdf_name}' renamed to '{os.path.basename(new_pdf_path)}'")

def select_pdf_files():
    root = tk.Tk()
    root.withdraw()
    file_paths = filedialog.askopenfilenames(filetypes=[("PDF Files", "*.pdf")])
    return root, file_paths

root, pdf_paths = select_pdf_files()
if pdf_paths:
    for pdf_path in pdf_paths:
        first_line = extract_first_line(pdf_path)
        if first_line:
            rename_pdf(pdf_path, first_line)
        else:
            print("Sem texto no PDF selecionado.")
            
else:
    print("Sem arquivos PDFs selecionados.")

root.destroy()
