from model.project import Project


def test_add_project(app):
    # получить список old_projects
    old_projects = app.soap.get_project_list()
    # сгенерировать имя проекта
    project_name = app.project.create_name(old_projects)
    # создать новый проект
    project = Project(name=project_name)
    app.project.create_project(project)
    # получить список new_projects
    # new_projects = app.project.get_project_list()
    new_projects = app.soap.get_project_list()
    # модифицировать old_projects
    old_projects.append(project)
    # проверка
    assert sorted(old_projects, key=Project.id_or_max) == sorted(new_projects, key=Project.id_or_max)

