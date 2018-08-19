# -*- coding: utf-8 -*-
from sys import path
from string import Template

path.append(__file__.replace('/controller.py', ''))

from beaker.middleware import SessionMiddleware

from core.postdatahandler import POSTDataHandler
from core.helpers.apphandler import AppHandler

from modules.task import TaskController

# url funcionando: http://housekeeping-api.local/housekeeping/v1.0/task/list/

def front_controller(environ, start_response):
    salida, respuesta, cabeceras = ("", "200 OK", [])

    environ['POST'] = POSTDataHandler().get_post_data(environ)
    environ['arg'] = AppHandler().get_arg(environ)
    salida = AppHandler().get_salida(environ)

    controlador = salida[0]
    modulo = salida[1]
    recurso = salida[2]

    # try:
    #     exec "from modules.{} import {}".format(modulo, controlador)
    #     exec "controller = {}()".format(controlador)
    #     exec "salida = {}().{}()".format(controlador, recurso)
    # except:
    #     salida = str("modulo no existe")

    content_type = ('Content-Type', 'text/html; charset=utf-8')
    cabeceras.append(content_type)

    start_response(respuesta, cabeceras)
    salida = TaskController().list()
    return str(salida)


beaker_dic = {
    'session.type': 'file',
    'session.cookie_expires': True,
    'session.auto': True,
    'session.data_dir': '/tmp/sessions',
}

application = SessionMiddleware(front_controller, beaker_dic)
