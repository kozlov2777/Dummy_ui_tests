import pytest
from pages.documentation_page import DocumentationPage
from pages.explorer_page import ExplorerPage
from pages.main_page import MainPage
from playwright.sync_api import Page
from utils.assertions import Assertions


@pytest.fixture
def assertions(page: Page):
    assertions = Assertions(page)
    yield assertions


@pytest.fixture
def main_page(page: Page):
    site = MainPage(page=page)
    site.page.goto("https://dummyapi.io")
    yield site


@pytest.fixture
def documentation_page(page: Page):
    site = DocumentationPage(page=page)
    site.page.goto("https://dummyapi.io/docs")
    yield site


@pytest.fixture
def explorer_page(page: Page):
    site = ExplorerPage(page=page)
    site.page.goto("https://dummyapi.io/explorer")
    yield site
