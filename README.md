# Diagramas
Sirven para mirar las dependencias del proyecto académica.

Esto permite construir un conjunto de diagramas qué muestran la ruta crítica.
Algo muy similar a CPM (Critical Path Method), qué permite visualizar el
desarrollo temporal de un proyecto, es complementario con el diagrama de gantt.

- https://es.wikipedia.org/wiki/M%C3%A9todo_de_la_ruta_cr%C3%ADtica
- https://www.obs-edu.com/int/blog-project-management/administracion-de-proyectos/las-3-metodologias-para-la-gestion-de-proyectos-que-mas-se-utilizan
- 

# Instalar dependencias
```sh
sudo python3 -m pip install --upgrade pip
sudo python3 -m pip install pandas
sudo python3 -m pip install graphviz
```
# Ejecutar
```sh
python3 generate_diagram.py
```
o
```sh
./generate_diagram.py
```

## Recomendaciones:
- Los campos de dependencias deben estar separados por " / "
por ejemplo: Persona / Organizacion
- Los nombres de las dependencias deben buscarse en el archivo
para saber si existen, el nombre preferido es "Proyecto Curricular",
por sobre "proyecto curricular".
