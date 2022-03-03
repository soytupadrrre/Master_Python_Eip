"""
Diseñando una aplicación web con flask

Script creado para la asignatura de Programación Avanzada en Python de la Escuela Internacional de Postgrados

Uso: 
- Windows: python "10.aplicacion_web.py"
- Linux: python3 "10.aplicacion_web.py"

@autor: Víctor Luque Martín
@fecha: 03-03-2022
@versión: 1.0
@licencia: MIT
@email: victorluque341@gmail.com
"""
from flask import Flask
import socket
import os
from datetime import datetime
app = Flask(__name__)

# Decorador para indicar el path de la pagina principal
@app.route('/')
def hello_world():
    # Obtención de nombre del equipo, ip local, nombre de usuario activo y fecha y hora
    host_name = socket.gethostname()
    local_ip = socket.gethostbyname(host_name)
    username = os.getlogin()
    # HTML con los datos a mostrar
    html = '''
    <html>
        <header>
            <title>Act 10 ProgAv Python VL</title>
        </header>
        <body style="display: flex; justify-content:center; align-items:flex-top">
            <div>
                <h1>Hola mundo &#127758</h1>
                <h2>Estoy usando Flask</h2>
                <p>Esta es la entrega de Víctor Luque de la actividad 10 de la asignatura <br><u>Programación Avanzada en Python</u></p>
                <p>Puedo renderizar HTML desde Python o Plantillas HTML utilizando Jinja2</p>
                <h2>Mi rival es <strong style="color:red;">Django</strong> &#129308&#129307</h2>
                <div>
                    <p> ¡Los datos de tu equipo son <strong>variables</strong>!</p>
                    <ul>
                        <li>Nombre: %s</li>
                        <li>Dirección IP: %s</li>
                        <li>Usuario: %s</li>
                        <li>Fecha: %s</li>
                    </ul>
                    <!-- Comentario HTML! -->
                    <p>&#9888 &#128187 ¡Cuidado con los hackers! &#128187 &#10071</p>
                </div>
                <button onclick=mostrarMensaje()>Mostrar mensaje de JavaScript</button>
            </div>
        </body>
        <script>
            function mostrarMensaje() {
                alert("¡Tambien cargo scripts en JavaScript!");
            }
        </script>
    </html>
    ''' % (host_name, local_ip, username, datetime.now().strftime("%d/%m/%Y %H:%M:%S"))
    return html

if __name__ == '__main__':
    # Se ejecuta el servidor en el puerto 5000
    # Para producción debug=True, de forma predeterminada Flask utiliza el modo producción (True)
    app.run(debug=False, host='localhost', port=5000)