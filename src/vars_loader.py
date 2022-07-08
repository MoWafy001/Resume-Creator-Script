with open('vars.txt') as f:
    txt = f.read().strip()


vars_d = {}

while '\n\n' in txt:
    txt = txt.replace('\n\n','\n')

lines = txt.split('\n')

for l in lines:
    k, v = l.strip().split('=')
    k = k.strip()
    v = v.strip()
    vars_d[k] = v

def get_var(var_name):
    if var_name not in vars_d:
        raise Exception(f'Variable {var_name} not found')
    else:
        return vars_d[var_name]
