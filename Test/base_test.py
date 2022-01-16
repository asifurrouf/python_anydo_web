
from selenium import webdriver
import pytest
import allure
from pathlib import Path
from selenium.webdriver.chrome.options import Options


@allure.severity(allure.severity_level.CRITICAL)
class BaseTest():
    @pytest.fixture()
    def setUp(self) -> None:
        path = Path()
        options = Options()
        options.add_argument("--start-fullscreen")
        self.driver = webdriver.Chrome(executable_path=(path / "chromedriver").absolute(), options=options)
        yield
        self.driver.close()

    class TestCase(object):
        pass