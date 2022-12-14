import pytest
from fixture.application import Application
import json
import os.path


fixture = None
target = None


def load_config(file):
    global target
    if target is None:
        a = os.path.abspath(__file__)
        b = os.path.dirname(a)
        config_file = os.path.join(b, file)
        with open(config_file) as h:
            target = json.load(h)
    return target


@pytest.fixture(scope="session")
def config(request):
    return load_config(request.config.getoption("--target"))


@pytest.fixture
def app(request, config):
    global fixture
    browser = request.config.getoption("--browser")
    if fixture is None or not fixture.is_valid():
        fixture = Application(browser=browser, config=config)
    fixture.session.ensure_login(username=config['web']['username'], password=config['web']['password'])
    return fixture


@pytest.fixture(scope="session", autouse=True)
def stop(request):
    def fin():
        # fixture.session.ensure_logout()
        fixture.destroy()
    request.addfinalizer(fin)
    return fixture


def pytest_addoption(parser):
    parser.addoption("--browser", action="store", default="chrome")
    parser.addoption("--target", action="store", default="target.json")
