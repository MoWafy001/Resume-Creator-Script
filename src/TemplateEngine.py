"""
I could have probably found some code or a library to do this for me.
"""

from .vars_loader import get_var


BLOCK_SIMBOL = '#'
VAR_SIMBOL = '$'

LIST_DICT_SIMBOL = '||'
LIST_DICT_SIMBOL_VALUE = '|+|'


class TemplateEngine:
    # instantiate
    def __init__(self, base_file_path):
        base_file_path = base_file_path.replace('.html', '')

        self.base_file_path = base_file_path

        self.base_file_name = base_file_path.split('/')[-1]
        self.html_path = '/'.join(base_file_path.split('/')[:-1])

        self.html = self.load_base_html()


    # load html
    def load_html(self, file_name):
        with open(f"{self.html_path}/{file_name}.html") as f:
            html = f.read().strip()

        return html


    # load base html
    def load_base_html(self):
        return self.load_html(self.base_file_name)


    # replace blocks with html
    def replace_blocks_with_html(self, html=None):
        if html is None:
            html = self.html

        html = self.find_list_and_dicts_and_replace(html)

        html_lines = html.split('\n')
        html_lines = list(map(self.find_blocks_and_replace, html_lines))
        html_lines = list(map(self.find_vars_and_replace, html_lines))

        html = '\n'.join(html_lines)

        return html


    # find blocks in a line and replace
    def find_blocks_and_replace(self, line):
        blocks = line.split(BLOCK_SIMBOL)[1::2]

        for block_name in blocks:
            block_html = self.load_html(block_name)
            block_html = self.replace_blocks_with_html(block_html)
            line = line.replace(
                f"{BLOCK_SIMBOL}{block_name}{BLOCK_SIMBOL}", block_html)

        return line


    # find values in a line and replace
    def find_vars_and_replace(self, line):
        vars_found = line.split(VAR_SIMBOL)[1::2]

        for var_name in vars_found:
            var_val = get_var(var_name)

            line = line.replace(
                f"{VAR_SIMBOL}{var_name}{VAR_SIMBOL}", get_var(var_name))

        return line

    
    # find list and dicts and replace
    def find_list_and_dicts_and_replace(self, html):
        pieces = html.split(LIST_DICT_SIMBOL)

        keys_blocks = {}

        key = None
        b = None
        skip = True
        for i,v  in enumerate(pieces):
            if skip:
                skip = False
                continue

            if key is None:
                key = v
                pieces[i] = ''
            else:
                b = v
                listordict = get_var(key)
                out = self.loop_over_list_or_dict(listordict, b, key)
                pieces[i] = out
                skip = True
                key = None
        
        return ' '.join(pieces)


    def loop_over_list_or_dict(self, var, b, key):
        out = ""
        if type(var) is list:
            for val in var:
                if type(val) is str:
                    nb = b.replace(f"{LIST_DICT_SIMBOL_VALUE}{key}_val{LIST_DICT_SIMBOL_VALUE}", val.replace('\n', '<br>'))
                    out += nb
                else:
                    out += self.loop_over_list_or_dict(val, b, key)
        else: # dict
            for k in var:
                nb = b.replace(f"{LIST_DICT_SIMBOL_VALUE}{key}_key{LIST_DICT_SIMBOL_VALUE}", k.replace('\n', '<br>'))
                if type(var[k]) == list:
                    c = 0
                    for i in var[k]:
                        nb = nb.replace(f"{LIST_DICT_SIMBOL_VALUE}{key}_val_{c}{LIST_DICT_SIMBOL_VALUE}", i.replace('\n', '<br>'))
                        c += 1
                    out += nb
                else:
                    nb = nb.replace(f"{LIST_DICT_SIMBOL_VALUE}{key}_val{LIST_DICT_SIMBOL_VALUE}", var[k].replace('\n', '<br>'))
                    out += nb

        return out
            

    # render
    def render(self):
        return self.replace_blocks_with_html()