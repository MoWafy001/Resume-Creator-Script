class HTMLLoader:
    def __init__(self, html_path):
        self.html_path = html_path


    def load_html(self, file_name):
        with open(f"{self.html_path}/{file_name}.html") as f:
            html = f.read().strip()

        return html