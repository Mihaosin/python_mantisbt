from model.project import Project

def test_add_project(app):
    # логин
    app.session.login("administrator", "root")
    # переход на вкадку Управление проектами
    app.project.open_manage_page()
    # получить список old_projects
    old_projects = app.project.get_project_list()
    # создать новый проект
    project = Project(name="new_project")
    app.project.create_project(project)
    # получить список new_projects
    new_projects = app.project.get_project_list()
    # модифицировать old_projects
    old_projects.append(project)
    # проверка
    assert sorted(old_projects) == sorted(new_projects)