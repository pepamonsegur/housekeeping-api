# -*- coding: utf-8 -*-
from sys import path

# BASE DE DATOS LOCAL
DB_HOST = 'localhost'
DB_USER = 'root'
DB_PASS = ''
DB_NAME = 'housekeeping'

APP_DIR = path[len(path) - 1]
UPLOAD_DIR = '%s/uploads' % APP_DIR.replace('/application', '')
STATIC_DIR = '%s/site_media' % APP_DIR
