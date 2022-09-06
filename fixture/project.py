from model.project import Project
from selenium.webdriver.common.by import By


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
        pass



    # def get_project_list(self):
    #     if self.contact_cache is None:
    #         wd = self.app.wd
    #         self.app.open_home_page()
    #         self.contact_cache = []
    #         for row in wd.find_elements(by=By.NAME, value="entry"):
    #             cells = row.find_elements(by=By.TAG_NAME, value="td")
    #             id = cells[index_id].find_element(by=By.NAME, value="selected[]").get_attribute("value")
    #             lastname = cells[index_lastname].text
    #             firstname = cells[index_firstname].text
    #             address = cells[index_address].text
    #             all_mails = cells[index_mails].text
    #             all_phones = cells[index_phones].text
    #             self.contact_cache.append(Contact(id=id, lastname=lastname, firstname=firstname, address=address,
    #                                               all_mails_from_home_page=all_mails,
    #                                               all_phones_from_home_page=all_phones))
    #     return list(self.contact_cache)

    # def open_contact_to_edit_by_index(self, index):
    #     wd = self.app.wd
    #     self.app.open_home_page()
    #     row = wd.find_elements(by=By.NAME, value="entry")[index]
    #     cell = row.find_elements(by=By.TAG_NAME, value="td")[index_edit_button]
    #     cell.find_element(by=By.TAG_NAME, value="a").click()