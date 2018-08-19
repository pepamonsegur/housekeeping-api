#-*- coding: utf-8 -*-


def leer_archivo(ruta):
    """Leer el contenido de un archivo de texto plano y lo retorna como string

    Params:
        ruta -- (string) Ruta del archivo a leer

    Returns:
        contenido -- (string) Cadena de texto con el contenido leído
    """
    with open(ruta, 'r') as archivo:
        contenido = archivo.read()
    return contenido