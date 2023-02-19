import pytest
from selenium import webdriver
from selenium.webdriver.edge.service import Service as EdgeService
from webdriver_manager.microsoft import EdgeChromiumDriverManager


@pytest.fixture
def driver():
    print("Creating EDGE driver")
    my_driver = webdriver.Edge(service=EdgeService(EdgeChromiumDriverManager().install()))
    yield my_driver
    print("Close EDGE driver")
    my_driver.quit()
