# -*- coding: utf-8 -*-
from cgi import escape, FieldStorage
from tempfile import TemporaryFile
from urllib2 import unquote


class POSTDataHandler(object):

    def __init__(self):
        pass

    def get_post_data(self, environ):
        _POST = {}

        if 'CONTENT_TYPE' in environ:
            if not environ['CONTENT_TYPE'].startswith('multipart/form-data'):
                _POST = self.__get_simple_formdata(environ)
            else:
                _POST = self.__get_multipart_formdata(environ)

        return _POST

    def __get_simple_formdata(self, environ):
        _POST = {}
        datos = environ['wsgi.input'].read().split('&')

        for par in datos:
            key, original_value = par.split('=')
            value = unquote(original_value).replace('+', ' ')
            value = POSTDataCleaner().sanitize_string(value)
            _POST[key] = value if not key in _POST else self.__to_list(
                _POST[key], value)

        return _POST

    def __get_multipart_formdata(self, environ):
        _POST = {}
        archivo_temporal = TemporaryFile()
        archivo_temporal.write(environ['wsgi.input'].read())
        archivo_temporal.seek(0)
        datos = FieldStorage(fp=archivo_temporal, environ=environ)

        for fieldname in datos:
            formfield = datos[fieldname]
            if isinstance(formfield, list):
                _POST[fieldname] = []
                for elemento in formfield:
                    _POST[fieldname].append(self.__get_value(elemento))
            else:
                _POST[fieldname] = self.__get_value(formfield)

        return _POST

    def __get_value(self, elemento):
        archivo = dict(
            filetype=elemento.type,
            filename=elemento.filename,
            content=elemento.value
        )
        value = elemento.value if elemento.filename is None else archivo
        if not isinstance(value, dict):
            value = POSTDataCleaner().sanitize_string(value)
        return value

    def __to_list(self, post_item, value):
        _postitem = post_item
        cleaned_value = POSTDataCleaner().sanitize_string(value)
        if isinstance(post_item, list):
            _postitem.append(cleaned_value)
        else:
            actual_value = post_item
            _postitem = []
            _postitem.extend([actual_value, cleaned_value])

        return _postitem


class POSTDataCleaner(object):

    def sanitize_string(cls, string):
        string_escape = escape(unicode(string, 'utf-8'), quote=True)
        string_encode = string_escape.encode('ascii', 'xmlcharrefreplace')

        diccionario = {'Ç': 199, 'ç' : 231, 'Á': 193, 'É': 201, 'Í': 205, 'Ó': 211,
            'Ú': 218, 'Ü': 220, 'á': 225, 'é': 233, 'í': 237, 'ó': 243,
            'ú': 250, 'ü': 252, 'Ñ': 209, 'ñ': 241}

        for caracter in diccionario:
            hexadecimal = "&#%s;" % diccionario[caracter]
            string_encode = string_encode.replace(hexadecimal, caracter)

        return string_encode.replace("'", "&#39;")
