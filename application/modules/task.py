# -*- coding: utf-8 -*-
from core.db import DBQuery


class Task(object):

    def __init__(self):
        self.task_id = 0
        self.title = ''
        self.description = ''
        self.done = 0
        # self.useraccess = compose(useraccess, Useraccess)

    # POST
    def insert(self):
        sql = """INSERT INTO task (title, description, done, useraccess)
            VALUES ('{title}', '{description}', {done}, '{useraccess}')
            """.format(title=self.title, description=self.description,
                    doen=self.done,
                    useraccess=self.useraccess.useraccess_id)
        self.task_id = DBQuery().execute(sql)

    # PUT
    def update(self):
        sql = """UPDATE task
                 SET    title = '{title}',
                        description = '{description}',
                        done = {done},
                        useraccess = '{useraccess}'
                 WHERE  task_id = {id}
        """.format(title=self.title,
            description=self.description, done=self.done, useraccess=self.useraccess)
        DBQuery().execute(sql)

    # GET
    def select(self):
        sql = """SELECT title, description, done, useraccess
                 FROM   task
                 WHERE  task_id = {id}
        """.format(id=self.task_id)
        datos = DBQuery().execute(sql)[0]

        # propiedades simples
        self.title = datos[0]
        self.description = datos[1]
        self.useraccess = make(Useraccess, datos[3])

    # DELETE
    def delete(self):
        sql = """DELETE FROM task WHERE task_id = {id}""".format(
            id=self.task_id)
        DBQuery().execute(sql)



class TaskView(object):

    def list(self):
        return str("Muestro lista")



class TaskController(object):

    def __init__(self):
        self.model = Task()
        self.view = TaskView()

    # POST
    def save(self):
        return self.model.insert()

    # PUT
    def update(self):
        return self.model.update()

    # DELETE
    def delete(self):
        return self.model.delete()

    # GET
    def view(self):
        return self.model.select()

    # GET
    def list(self):
        return self.view.list()
