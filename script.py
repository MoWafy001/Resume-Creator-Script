from src.TemplateEngine import TemplateEngine
from src.pdf_gen import create_pdf


# typing .html is not necessary
engine = TemplateEngine('layout/layout.html')

layout, file_name = engine.render()

create_pdf(layout, file_name)

print(layout)