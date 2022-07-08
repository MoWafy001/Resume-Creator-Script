def render(line):
    sline = line.strip()
    if len(sline) > 2 and sline[0] == '#' and sline[-1] == '#':
        file_name = sline[1:-1]
        return load_html(file_name)
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