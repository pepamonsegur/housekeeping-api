# -*- coding: utf-8 -*-
import json

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
        data = DBQuery().execute(sql)[0]

        # propiedades simples
        self.title = data[0]
        self.description = data[1]
        self.useraccess = make(Useraccess, data[3])

    # DELETE
    def delete(self):
        sql = """DELETE FROM task WHERE task_id = {id}""".format(
            id=self.task_id)
        DBQuery().execute(sql)


    def select_all(self):
        sql = """SELECT title, description, done, useraccess
                 FROM   task
        """
        data = DBQuery().execute(sql)
        return data



class TaskView(object):

    def __init__(self):
        self.model = Task()

    def list(self):
        data = self.model.select_all()
        return json.dumps(data)



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
