from src.TemplateEngine import TemplateEngine
from src.pdf_gen import create_pdf


# typing .html is not necessary
engine = TemplateEngine('layout/layout.html')

layout = engine.render()

create_pdf(layout)

print(layout)