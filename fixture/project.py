from model.project import Project
from selenium.webdriver.common.by import By
import random
import string


class ProjectHelper:

    def __init__(self, app):
        self.app = app

    def open_manage_page(self):
        wd = self.app.wd
        if not wd.current_url.endswith("localhost/mantisbt-2.25.4/manage_proj_page.php"):
            wd.get('http://localhost/mantisbt-2.25.4/manage_proj_page.php')

    project_cache = None

    def get_project_list(self):
        wd = self.app.wd
        self.open_manage_page()
        self.project_cache = []
        table = wd.find_elements(by=By.TAG_NAME, value="tbody")
        rows = table[0].find_elements(by=By.TAG_NAME, value="tr")
        name_id = 0
        for row in rows:
            cells = row.find_elements(by=By.TAG_NAME, value="td")
            project_name = cells[name_id].text
            link = cells[name_id].find_element(by=By.TAG_NAME, value="a").get_attribute("href")
            project_id = link[link.index("=")+1:len(link)]
            self.project_cache.append(Project(name=project_name, id=project_id))
        return list(self.project_cache)


    def create_project(self, project):
        wd = self.app.wd
        self.open_manage_page()
        wd.find_element(by=By.CSS_SELECTOR, value="button[type='submit']").click()
        wd.find_element(by=By.NAME, value="name").click()
        wd.find_element(by=By.NAME, value="name").clear()
        wd.find_element(by=By.NAME, value=f"name").send_keys(project.name)
        wd.find_element(by=By.CSS_SELECTOR, value="input[type='submit']").click()

    def create_name(self, old_projects):
        symbols = string.ascii_letters
        name = "".join([random.choice(symbols) for i in range(8)])
        while self.name_is_exist(name, old_projects):
            name = "".join([random.choice(symbols) for i in range(8)])
        return name

    def name_is_exist(self, name, old_projects):
        zzz = False
        for project in old_projects:
            if name == project.name:
                zzz = True
        return zzz

    def delete_by_id(self, id):
        wd = self.app.wd
        self.open_manage_page()
        self.open_project_page_by_id(id)
        # нажать на кнопуку "удалить"
        wd.find_element(by=By.CSS_SELECTOR, value="input[value='Удалить проект']").click()
        wd.find_element(by=By.CSS_SELECTOR, value="input[value='Удалить проект']").click()


    def open_project_page_by_id(self, id):
        wd = self.app.wd
        # нажимаем кнопку edit для заданной по id контакта
        wd.find_element(by=By.CSS_SELECTOR, value="a[href='manage_proj_edit_page.php?project_id=%s']" % id).click()


