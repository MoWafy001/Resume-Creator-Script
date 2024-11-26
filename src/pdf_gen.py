from weasyprint import HTML, CSS
import os


def create_pdf(layout, file_name, template, script_dir):
    # Load CSS file paths automatically from the CSS directory
    dir_name = os.path.join(script_dir, 'templates', template, 'css')

    # Default CSS with fallback margins
    default_css = """
    @page {
        size: A4 auto;
        margin: 0; /* Default margins */
    }
    """

    css_files = [
        CSS(string=default_css),
        *[CSS(filename=os.path.join(dir_name, css_file)) for css_file in os.listdir(dir_name) if css_file.endswith('.css')]
    ]

    # Ensure the output directory exists
    output_dir = os.path.join(script_dir, 'out')
    if not os.path.exists(output_dir):
        os.mkdir(output_dir)

    # Generate the PDF
    output_path = os.path.join(output_dir, f'{file_name}.pdf')
    HTML(string=layout).write_pdf(output_path, stylesheets=css_files)

    print(f"PDF created at: {output_path}")
