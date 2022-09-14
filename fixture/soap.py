from zeep import Client
# from zeep import WebFault
from model.project import Project


class SoapHelper:

    def __init__(self, app):
        self.app = app

    def get_project_list(self, username = "administrator", password = "root"):
        client = Client("http://localhost/mantisbt-2.25.4/api/soap/mantisconnect.php?wsdl")
        xxxx = client.service.mc_projects_get_user_accessible(username, password)
        list = []
        for i in xxxx:
            list.append(Project(id=i.id, name=i.name))
        return list

