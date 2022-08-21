BLOCK_SIMBOL = '%block%'
VAR_SIMBOL = '$'

LIST_DICT_SIMBOL = '||'
LIST_DICT_SIMBOL_VALUE = '|+|'


class HTMLParser:
    def __init__(self, get_var, load_html, html):
        self.get_var = get_var
        self.load_html = load_html
        self.html = html


    # replace blocks with html
    def parse_html(self, html=None):
        if html is None:
            html = self.html

        html = self.handel_lists_and_dicts(html)

        html_lines = html.split('\n')
        html_lines = list(map(self.handel_blocks, html_lines))
        html_lines = list(map(self.handel_variables, html_lines))

        html = '\n'.join(html_lines)

        return html


    # find blocks in a line and replace
    def handel_blocks(self, line):
        blocks = line.split(BLOCK_SIMBOL)[1::2]

        for block in blocks:
            block_name, dep = self.get_block_name_and_dep(block)

            block_html = self.get_block_html(block_name, dep)
            block_html = self.parse_html(block_html)

            line = self.symbol_to_value(line, BLOCK_SIMBOL,
                                            block, block_html)

        return line


    # find variables in lines and replace
    def handel_variables(self, line):
        vars_found = line.split(VAR_SIMBOL)[1::2]

        for var_name in vars_found:
            var_val = self.get_var(var_name)

            line = self.symbol_to_value(line, VAR_SIMBOL,
                                            var_name, self.get_var(var_name))

        return line

    
    # find list and dicts and replace
    def handel_lists_and_dicts(self, html):
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
                out = self.list_dict_get_out(b, key)
                pieces[i] = out
                skip = True
                key = None
        
        return ' '.join(pieces)


    def loop_over_list_or_dict(self, var, b, key):
        out = ""
        if type(var) is list:
            out = self.handel_list(out, var, b, key)
        else: # dict
            out = self.handel_dict(out, var, b, key)

        return out

    
    """
    Helper Methods
    """

    def get_block_name_and_dep(self, block):
        block_l = block.split('?')
        block_name = block_l[0].strip()
        dep = None

        if len(block_l) == 2:
            dep = block_l[1]
            if dep.strip() == '':
                dep = block_name

        return block_name, dep


    def get_block_html(self, block_name, dep):
        if dep is not None:
            try:
                self.get_var(dep)
                return self.load_html(block_name)  
            except:
                return ''
        
        return self.load_html(block_name)


    def symbol_to_value(self, line, symbol, var, value):
        return line.replace(f"{symbol}{var}{symbol}", value)


    def list_dict_get_out(self, b, key):
        try:
            listordict = self.get_var(key)
            return self.loop_over_list_or_dict(listordict, b, key)
        except:
            return ''


    def handel_list(self, out, var, b, key):
        for val in var:
            if type(val) is str:
                nb = self.symbol_to_value(b, LIST_DICT_SIMBOL_VALUE,
                                            key+"_val", val.replace('\n', '<br>'))
                out += nb
            else:
                out += self.loop_over_list_or_dict(val, b, key)
        return out


    def handel_dict(self, out, var, b, key):
        for k in var:
            nb = self.symbol_to_value(b, LIST_DICT_SIMBOL_VALUE,
                                        key+"_key", k.replace('\n', '<br>'))
            if type(var[k]) == list:
                out += self.handel_list_in_dict(var[k], nb, key)

            else:
                nb = self.symbol_to_value(nb, LIST_DICT_SIMBOL_VALUE,
                                            f"{key}_val", var[k].replace('\n', '<br>'))
                out += nb

        return out


    def handel_list_in_dict(self, var_k, nb, key):
        c = 0
        for i in var_k:
            nb = self.symbol_to_value(nb, LIST_DICT_SIMBOL_VALUE,
                                        f"{key}_val_{c}", i.replace('\n', '<br>'))
            c += 1

        return nb