import pdfkit
import os

options = {
    'encoding': "UTF-8",
    'custom-header': [
        ('Accept-Encoding', 'gzip')
    ],
    'no-outline': None
}


def create_pdf(layout, file_name, template):

    # load the css file names automaticlly from the css directory
    dir_name = f'templates/{template}/css'
    css = list(map(lambda x: f"{dir_name}/{x}" , os.listdir(dir_name)))


    pdfkit.from_string(layout, f'{file_name}.pdf', options=options, css=css)