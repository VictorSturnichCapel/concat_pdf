import os
from PyPDF2 import PdfMerger

def concatenate_pdfs(src_folder, output_file):
    merger = PdfMerger()
    pdf_files = [f for f in os.listdir(src_folder) if f.endswith('.pdf')]

    for pdf in sorted(pdf_files):
        merger.append(os.path.join(src_folder, pdf))

    merger.write(output_file)
    merger.close()

if __name__ == "__main__":
    src_folder = os.path.join(os.path.dirname(__file__), '..', 'src')
    output_file = os.path.join(os.path.dirname(__file__), '..', 'final', 'output.pdf')
    concatenate_pdfs(src_folder, output_file)
    print(f"PDFs concatenated into {output_file}")