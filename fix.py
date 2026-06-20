import nbformat

# Cambia 'tu_notebook.ipynb' por el nombre real de tu archivo
file_path = 'GRUPO_2_AMIA_2025_TP_FInal.ipynb'

with open(file_path, 'r', encoding='utf-8') as f:
    nb = nbformat.read(f, as_version=4)

# Elimina la clave de widgets que causa el conflicto
if 'widgets' in nb.get('metadata', {}):
    del nb['metadata']['widgets']
    print("Sección 'widgets' eliminada con éxito.")

with open(file_path, 'w', encoding='utf-8') as f:
    nbformat.write(nb, f)
