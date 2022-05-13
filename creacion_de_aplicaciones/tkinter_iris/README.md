# IRIS TKINTER GUI
Script creado para la asignatura de Creación de aplicaciones Python de la Escuela Internacional de Postgrados, lección 10.

## Autor
* Nombre: Víctor Luque Martín<br>
* Fecha: 13-05-2022<br>
* Versión: 1.0<br>
* Email: [victorluque341@gmail.com](mailto:victorluque341@gmail.com)

## Dependencias
```powershell
pip install tkinter
pip install pygubu
```

## Descripción
Este script contiene una aplicación que permite crear una interfaz gráfica con el usuario.
El usuario puede navegar por los distintos menús de la aplicación y seleccionar las opciones que desee para acceder a nuevos apartados.
Los datos de Iris Dataset se encuentran en la ruta `data/iris.csv`.

Además del código fuente de la aplicación, se incluye el proyecto como un ejecutable (ejecutar VictorLuque_TkinterCompilado/VictorLuque_TkinterCompilado.exe).

## Interfaz gráfica
### Menú principal
Página principal con un menú con las opciones de navegación.
![home](img/home.png)

### Mostrar todos los datos de Iris DataSet
Página con una tabla con todos los datos de la base de datos.
![iris](img/alldata.png)

### Mostrar el resumen de Iris DataSet
Página con una tabla con el resumen de los datos de la base de datos.
![iris](img/resume.png)
![iris](img/resume_total.png)
![iris](img/resume_avg.png)
![iris](img/resume_max.png)
![iris](img/resume_min.png)
![iris](img/resume_std.png)
![iris](img/resume_per25.png)
![iris](img/resume_per50.png)
![iris](img/resume_per75.png)

### Precisión de los modelos Machine Learning
Página que muestra la precisión de los modelos Machine Learning.
La precisión se calcula con los datos dentro de Iris Dataset, con un 80% de los datos empleados como entrenamiento y un 20% como prueba (train y test).
Los resultados varían en función de la predicción de los modelos.
![iris](img/acc_1.png)
![iris](img/acc_2.png)

### Mostrar gráficos del Sepalo y del Petalo
Página con dos gráficos que muestran la longitud y la anchura del Sepalo y el Petalo
![iris](img/iris_plots.png)

### Insertar Datos
Página con un formulario para insertar datos en la base de datos.
![iris](img/insert.png)

### Predecir e Insertar datos
Página con un formulario para insertar datos en la base de datos y una tabla con los resultados de la predicción.

![iris](img/predict_data.png)

### Actualizar último dato
Página con un formulario para actualizar el último dato de la base de datos.
![iris](img/update_last.png)

### Actualizar dato por ID
Página con un formulario para actualizar un dato de la base de datos por su ID.
![iris](img/update_by_id.png)

### Eliminar último dato
Página con un formulario para eliminar el último dato de la base de datos.

![iris](img/delete_last.png)

### Eliminar dato por IDs
Página con un formulario para eliminar un dato de la base de datos por su ID.

![iris](img/delete_by_id.png)

## Notas:
Para compilar el proyecto es necesario evitar importar las siguientes dependencias:
* sklearn.utils._typedefs
* sklearn.neighbors._partition_nodes
* pygubu.builder.tkstdwidgets
