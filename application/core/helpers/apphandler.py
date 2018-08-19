from os.path import isfile
from settings import APP_DIR

class AppHandler(object):

    def url_parser(self, environ):
        uri = environ['REQUEST_URI'].split('/')
        modulo = self.get_modulo(uri)
        recurso = uri[4] if len(uri) > 4 else 'default'
        return modulo, recurso

    def get_arg(self, environ):
        uri = environ['REQUEST_URI'].split('/')
        return uri[5] if len(uri) > 5 else 0

    def get_controller_name(self, modulo):
        return "{modelo}Controller".format(modelo=modulo.title())

    def get_modulo(self, uri):
        modulo = uri[3] if len(uri) > 3 else 'default'
        if not isfile("{}/modules/{}.py".format(APP_DIR, modulo)):
            modulo = 'default'
        return modulo

    def get_salida(self, environ):
        modulo, recurso = self.url_parser(environ)
        controlador = self.get_controller_name(modulo)

        salida = (controlador, modulo, recurso)
        return salida

