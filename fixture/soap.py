from zeep import Client
# from zeep import WebFault
from model.project import Project


class SoapHelper:

    def __init__(self, app):
        self.app = app

    def get_project_list(self, username, password):
        client = Client(self.app.soap_client)
        xxxx = client.service.mc_projects_get_user_accessible(username, password)
        list = []
        for i in xxxx:
            list.append(Project(id=i.id, name=i.name))
        return list
