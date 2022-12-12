import random as rnd

def create_param_dict(n):
    keys = ['arrival', 'departure1', 'departure2', 'departure3', 'departure4']
    return {k: rnd.random(n) for k in keys}
    