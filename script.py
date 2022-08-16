from src.vars_loader import VarsReader
from src.TemplateEngine import TemplateEngine
from src.pdf_gen import create_pdf
import os
import sys

script_dir = '/'.join(__file__.split('/')[:-1])

if len(sys.argv) < 2:
    vars_file_path = f"{script_dir}/vars.yaml"
else:
    vars_file_path = sys.argv[1]

get_var = VarsReader(vars_file_path).get_var

try:
    template = get_var('template')
except:
    template = 'Default'


# typing .html is not necessary
engine = TemplateEngine(f'{script_dir}/templates/{template}/layout/layout.html', get_var)

layout, file_name = engine.render()

create_pdf(layout, file_name, template, script_dir)

#print(layout)
print(file_name, 'created')