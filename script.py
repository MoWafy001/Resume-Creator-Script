"""
Imports
"""
from src.vars_loader import VarsReader
from src.TemplateEngine import TemplateEngine
from src.pdf_gen import create_pdf
import os
import sys


""" 
Setting up variable 
"""
script_dir = '/'.join(__file__.split('/')[:-1]) \
                # Where the this script is located

vars_file_path = f"{script_dir}/vars.yaml" \
                # The default YAML file to use

vars_file_path = sys.argv[1] if len(sys.argv) >= 2 else vars_file_path \
                # Getting a YAML file path as a CLI argument

get_var = VarsReader(vars_file_path).get_var \
                # will be used to read from the YAML file

template = 'Default' # The default resume template


try:
    template = get_var('template')
except:
    pass


""" 
The code starts here 
"""
# typing .html is not necessary
engine = TemplateEngine(f'{script_dir}/templates/{template}/layout/layout.html', get_var)
layout, file_name = engine.render()
create_pdf(layout, file_name, template, script_dir)


"""
Printing some output
"""
#print(layout)
print(file_name, 'created')