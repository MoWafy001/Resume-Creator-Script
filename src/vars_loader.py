import yaml

class VarsReader:
    def __init__(self, vars_path='vars.yaml'):
        with open(vars_path) as f:
            self.vars_d = yaml.safe_load(f)

    def get_var(self, var_name):
        if var_name not in self.vars_d:
            raise Exception(f'Variable {var_name} not found')
        else:
            return self.vars_d[var_name]