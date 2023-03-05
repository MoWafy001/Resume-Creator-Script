from src.vars_loader import VarsReader
from src.TemplateEngine import TemplateEngine
from src.pdf_gen import create_pdf
import sys


def get_script_dir():
    return '/'.join(__file__.split('/')[:-1])


def get_vars_path(script_dir):
    if len(sys.argv) >= 2:
        return sys.argv[1]

    if not os.path.exists(f"{script_dir}/vars.yaml"):
        print("vars.yaml does not exist in the current directory")
        sys.exit(1)

    return f"{script_dir}/vars.yaml"


def get_template_name(get_var):
    try:
        return get_var('template')
    except:
        print("No template specified in the YAML file, using the default template")
        return 'Default'


def create_resume(vars_file_path, script_dir):
    script_dir += '/..'
    # will be used to read from the YAML file
    get_var = VarsReader(vars_file_path).get_var

    # get the template name
    template = get_template_name(get_var)

    # render the template
    engine = TemplateEngine(
        f'{script_dir}/templates/{template}/layout/layout.html', get_var)
    layout, file_name = engine.render()

    # create the pdf
    create_pdf(layout, file_name, template, script_dir)

    print(file_name, 'created')
