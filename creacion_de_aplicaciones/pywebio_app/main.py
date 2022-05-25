from pywebio import start_server, config
import app
    
if __name__ == "__main__":
    config(theme="dark")
    app_list = [
        app.app_datos,
        app.app_matrix,
        app.app_prediccion,
        app.app_insertar,
        app.app_actualizar,
        app.app_eliminar,
    ]
    start_server(app_list, port=8080, debug=True)

