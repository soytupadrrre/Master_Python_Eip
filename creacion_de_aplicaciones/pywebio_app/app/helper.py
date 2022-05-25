from pywebio import output

def menu():
    """
    Menu de opciones empleado en todas las aplicaciones
    """
    output.put_markdown("# Víctor Luque - Iris PyWebIO"),
    output.put_markdown("## Menu")
    output.put_link("- Home", "/")
    output.put_text("")
    output.put_link("- Ver Datos", "/?app=app_datos")
    output.put_text("")
    output.put_link("- Matriz de Confusion", "/?app=app_matrix")
    output.put_text("")
    output.put_link("- Predecir", "/?app=app_prediccion")
    output.put_text("")
    output.put_link("- Insertar", "/?app=app_insertar")
    output.put_text("")
    output.put_link("- Actualizar", "/?app=app_actualizar")
    output.put_text("")
    output.put_link("- Eliminar", "/?app=app_eliminar")
    output.put_text("")
    