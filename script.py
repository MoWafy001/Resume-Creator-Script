"""
Imports
"""
from src.helpers import get_script_dir, get_vars_path, create_resume
import os


""" 
Setting up variable 
"""
script_dir = get_script_dir()  # Where the this script is located
vars_file_path = get_vars_path(script_dir)  # Where the vars.yaml is located


"""
Create resume
"""
# if vars_file_path is a directory, then we will loop through all the files in the directory
# else we will just create a resume from the vars_file_path
if os.path.isdir(vars_file_path):
    for file in os.listdir(vars_file_path):
        if file.endswith(".yaml") and not file.endswith(".component.yaml"):
            create_resume(f'{vars_file_path}/{file}', script_dir)
else:
    create_resume(vars_file_path, script_dir)
