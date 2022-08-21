from .HTMLLoader import HTMLLoader
from .HTMLParser import HTMLParser


"""
I could have probably found some code or a library to do this.
"""


class TemplateEngine:
    # instantiate
    def __init__(self, base_file_path, get_var):
        # to get variables
        self.get_var = get_var

        # base HTML file path
        self.base_file_path = base_file_path.replace('.html', '')
        self.base_file_name = self.base_file_path.split('/')[-1]

        # the path of the directory where the HTML files are
        self.html_path = '/'.join(self.base_file_path.split('/')[:-1])

        # HTML Loader
        html_loader = HTMLLoader(self.html_path)
        self.load_html = html_loader.load_html

        # get the HTML of the base HTML file
        self.html = self.load_html(self.base_file_name)

        # HTML Parser
        html_parser = HTMLParser(self.get_var, self.load_html, self.html)
        self.parse_html = html_parser.parse_html


    # render
    def render(self):
        job_title = self.get_var('job title').strip().replace(' ', '_')
        full_name = self.get_var('full name').strip().replace(' ', '_')
        
        file_name = f"{full_name}_{job_title}"

        return self.parse_html(), file_name