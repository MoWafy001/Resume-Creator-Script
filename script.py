import pdfkit

css = 'style.css'
pdfkit.from_file('layout.html', 'out.pdf', css=css)

