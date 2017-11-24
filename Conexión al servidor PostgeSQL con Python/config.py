"""
Autor: Alfredo
"""

#Importamos la librería ConfigParser para verificar la estructura de la conexión
from configparser import ConfigParser

#Creamos una función, donde cargamos el archivo con los parametros de conexión y seleccionamos la seccion de postgreSQL
def config(filename='database.ini', section='postgresql'):
    # Creamos el analizador
    parser = ConfigParser()
    # Leemos la configuración del archivo
    parser.read(filename)

    #Creamos un diccionario para la base de datos
    db = {}
    # Obtenemos la section de postgreSQL
    if parser.has_section(section):
        params = parser.items(section)
        for param in params:
            db[param[0]] = param[1]
    else:
        #Si se presenta un error lo mostraremos en pantalla
        raise Exception('Section {0} not found in the {1} file'.format(section, filename))
    #Retornamos el diccionario con los parametros
    return db
