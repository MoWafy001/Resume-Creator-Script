import pdfkit
import os


options = {
    'encoding': "UTF-8",
    'custom-header': [
        ('Accept-Encoding', 'gzip')
    ],
    'no-outline': None
}


def create_pdf(layout, file_name, template, script_dir):


    # load the css file names automaticlly from the css directory
    dir_name = f'{script_dir}/templates/{template}/css'
    css = list(map(lambda x: f"{dir_name}/{x}" , os.listdir(dir_name)))


    # Creates out/ if doesn't exist    
    if 'out' not in os.listdir(script_dir):
        os.mkdir(f'{script_dir}/out')


    # create the PDF resume
    pdfkit.from_string(layout, f'{script_dir}/out/{file_name}.pdf', options=options, css=css)