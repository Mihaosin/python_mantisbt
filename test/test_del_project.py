from model.project import Project
import random


def test_del_project(app):
    # логин
    app.session.login("administrator", "root")
    # получить список old_projects
    old_projects = app.soap.get_project_list()
    # old_projects = app.project.get_project_list()
    # проверяем длину списка проектов, если пустой - создаем новый проект
    if len(old_projects) == 0:
        app.project.create_project(Project(name="new_project"))
        old_projects = app.soap.get_project_list()
        # old_projects = app.project.get_project_list()
    # выбираем случайный проект для удаления и удаляем его
    project = random.choice(old_projects)
    app.project.delete_by_id(project.id)
    # получить список new_projects
    new_projects = app.soap.get_project_list()
    # new_projects = app.project.get_project_list()
    # модифицировать old_projects
    old_projects.remove(project)
    # проверка
    assert sorted(old_projects, key=Project.id_or_max) == sorted(new_projects, key=Project.id_or_max)