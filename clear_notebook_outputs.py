import json
p = r"C:\Users\KIIT0001\Desktop\BikePredict\bike-rental-count-prediction-using-python.ipynb"
with open(p, 'r', encoding='utf-8') as f:
    nb = json.load(f)
changed = False
for c in nb.get('cells', []):
    if c.get('cell_type') == 'code':
        if c.get('outputs'):
            c['outputs'] = []
            changed = True
        if c.get('execution_count') is not None:
            c['execution_count'] = None
            changed = True
if changed:
    with open(p, 'w', encoding='utf-8') as f:
        json.dump(nb, f, indent=1, ensure_ascii=False)
    print('CLEARED: notebook outputs removed')
else:
    print('NO CHANGES: no outputs found')
