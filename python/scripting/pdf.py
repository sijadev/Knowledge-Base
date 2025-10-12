import PyPDF2
from sys import argv
from pathlib import Path

path = str(Path(__file__).parent.absolute())

input_file = path + '/pdf/orginal.pdf'
output_file = path + '/pdf/new.pdf'
combined_file = path + '/pdf/combined.pdf'
watermark_file = path + '/pdf/wtr.pdf'
watermarked_pdf = path + '/pdf/watermarked.pdf'


def pdf(input_path):
    # Read the binary
    # mode = 'rb' (read binary)
    with open(input_path, 'rb') as r_binary_file:
        my_reader = PyPDF2.PdfFileReader(r_binary_file)
        num_of_pages = my_reader.numPages
        print(f'The pdf has {num_of_pages} page(s).')
        page = my_reader.getPage(0)
        page.rotateCounterClockwise(90)
        my_writer = PyPDF2.PdfFileWriter()
        my_writer.addPage(page)
        with open(output_file, 'wb') as w_binary_file:
            my_writer.write(w_binary_file)


def pdf_merger(input_list):
    merger = PyPDF2.PdfFileMerger()
    for pdf_file in input_list:
        merger.append(pdf_file)
    merger.write(combined_file)


def set_watermark():
    my_input = PyPDF2.PdfFileReader(open(combined_file, 'rb'))
    watermark = PyPDF2.PdfFileReader(open(watermark_file, 'rb'))
    writer = PyPDF2.PdfFileWriter()
    for index in range(my_input.getNumPages()):
        page = my_input.getPage(index)
        page.mergePage(watermark.getPage(0))
        writer.addPage(page)
    with open(watermarked_pdf, 'wb') as file:
        writer.write(file)


file_count = len(argv[0:])

if file_count == 1:
    pdf(input_file)
else:
    my_input_list = argv[1:]
    pdf_merger(my_input_list)
    set_watermark()
