from src.vars_loader import get_var
from src.TemplateEngine import TemplateEngine
from src.pdf_gen import create_pdf


try:
    template = get_var('template')
except:
    template = 'Default'


# typing .html is not necessary
engine = TemplateEngine(f'templates/{template}/layout/layout.html', get_var)

layout, file_name = engine.render()

create_pdf(layout, file_name, template)

print(layout)