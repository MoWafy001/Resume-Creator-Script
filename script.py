import pdfkit

options = {
    'page-size': 'Letter',
    'margin-top': '0',
    'margin-right': '0',
    'margin-bottom': '0',
    'margin-left': '0',
    'encoding': "UTF-8",
    'custom-header': [
        ('Accept-Encoding', 'gzip')
    ],
    'no-outline': None
}

css = [ 'css/style.css' ]
pdfkit.from_file('layout/layout.html', 'out.pdf', options=options, css=css)

