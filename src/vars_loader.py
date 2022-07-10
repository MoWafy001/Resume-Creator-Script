import yaml

with open('vars.yaml') as f:
    vars_d = yaml.safe_load(f)

def get_var(var_name):
    if var_name not in vars_d:
        raise Exception(f'Variable {var_name} not found')
    else:
        return vars_d[var_name]