from selenium.webdriver.common.by import By


class SessionHelper:

    def __init__(self, app):
        # этот конструктор получает в качестве внешнего параметра ссылку на объект класса Application
        # и сохраняет ее в свойство с именем app
        self.app = app

    def login(self, username, password):
        wd = self.app.wd
        self.app.open_home_page()
        # авторизация в учетной записи
        wd.find_element(by=By.NAME, value="username").click()
        wd.find_element(by=By.NAME, value="username").clear()
        wd.find_element(by=By.NAME, value="username").send_keys(username)
        wd.find_element(by=By.CSS_SELECTOR, value="input[value='Вход']").click()
        wd.find_element(by=By.NAME, value="password").click()
        wd.find_element(by=By.NAME, value="password").clear()
        wd.find_element(by=By.NAME, value="password").send_keys(password)
        wd.find_element(by=By.CSS_SELECTOR, value="input[value='Вход']").click()

    def logout(self):
        wd = self.app.wd
        wd.get('http://localhost/mantisbt-2.25.4/logout_page.php')
        # выход из учетной записи
        # xxx = wd.find_element(by=By.CSS_SELECTOR, value="a[href='/mantisbt-2.25.4/logout_page.php']")
        # yyy = xxx.GetAttribute("value")
        # yyy.click()

    # def ensure_logout(self):
    #     wd = self.app.wd
    #     # if self.is_logged_in():
    #     self.logout()
    #
    # def is_logged_in(self):
    #     wd = self.app.wd
    #     return len(wd.find_elements(by=By.CSS_SELECTOR, value="a[href='/mantisbt-2.25.4/logout_page.php']")) > 0

    def is_logged_in_as(self, username):
        wd = self.app.wd
        return self.get_loggeg_in_user() == username

    def get_loggeg_in_user(self):
        wd = self.app.wd
        v = wd.find_elements(by=By.CSS_SELECTOR, value="a[href='/mantisbt-2.25.4/account_page.php']")
        v1 = v[1].get_attribute("text")
        return v1

    # def ensure_login(self, username, password):
    #
    #     if self.is_logged_in():
    #         if self.is_logged_in_as(username):
    #             return
    #         else:
    #             self.logout()
    #     self.login(username,password)