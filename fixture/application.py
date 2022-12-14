from selenium import webdriver
from fixture.session import SessionHelper
from fixture.project import ProjectHelper
from fixture.soap import SoapHelper


class Application:

    def __init__(self, browser, config):
        if browser == "chrome":
            self.wd = webdriver.Chrome()
        elif browser == "firefox":
            self.wd = webdriver.Firefox()
        elif browser == "ie":
            self.wd = webdriver.Ie()
        elif browser == "edge":
            self.wd = webdriver.Edge()
        else:
            raise ValueError("Unrecognized broser %s" % browser)
        self.session = SessionHelper(self)
        self.project = ProjectHelper(self)
        self.soap = SoapHelper(self)
        self.config = config
        self.base_url = config['web']['baseUrl']
        self.username = config['web']['username']
        self.password = config['web']['password']
        self.logout = config['web']['logout']
        self.manage = config['web']['manage']
        self.soap_client = config['web']['soap_client']

    def is_valid(self):
        try:
            self.wd.current_url
            return True
        except:
            return False

    def open_home_page(self):
        wd = self.wd
        wd.get(self.base_url)

    def destroy(self):
        self.wd.quit()
