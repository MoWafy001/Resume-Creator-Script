import pdfkit
import os

options = {
    'page-size': 'Letter',
    'margin-top': '5mm',
    'margin-right': '5mm',
    'margin-bottom': '5mm',
    'margin-left': '5mm',
    'encoding': "UTF-8",
    'custom-header': [
        ('Accept-Encoding', 'gzip')
    ],
    'no-outline': None
}

# load the css file names automaticlly from the css directory
dir_name = 'css'
css = list(map(lambda x: f"{dir_name}/{x}" , os.listdir(dir_name)))

def create_pdf(layout, file_name):
    pdfkit.from_string(layout, f'{file_name}.pdf', options=options, css=css)