from src.vars_loader import get_var


def is_something(sline, somehting):
    if len(sline) <= 2:
        return False
    return len(sline.split(somehting)) > 2

def is_block(sline):
    return is_something(sline, '#')

def is_var(sline):
    return is_something(sline, '$')

def extract_template_var_name(sline, s):
    values = sline.split(s)[1::2]
    return values

def extract_template_name(sline):
    return extract_template_var_name(sline, '#')[0]

def extract_template_vars(sline):
    return extract_template_var_name(sline, '$')


def render(line):
    sline = line.strip()

    if is_block(sline):
        file_name = extract_template_name(sline)
        return load_html(file_name)

    elif is_var(sline):
        print('hi')
        vars_list = extract_template_vars(sline)
        for v in vars_list:
            line = line.replace(f"${v}$", get_var(v))
        return line

    else:
        return line


def load_html(file_name):
    with open(f"layout/{file_name}.html") as f:
        html = f.read()
    
    html = html.split('\n')
    html = list(map(render, html))
    html = '\n'.join(html)

    return html


layout = load_html('layout')

print(layout)