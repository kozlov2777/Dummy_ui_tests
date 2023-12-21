from playwright.sync_api import Page
from locators.explorer_page_locators import ExplorerPageLocators
import allure


class ExplorerPage:
    def __init__(
        self,
        page: Page,
    ):
        self.page = page
        self.locators = ExplorerPageLocators

    @allure.step("Click go to documentation button")
    def click_go_to_documentation(self):
        self.page.click(selector=self.locators.GO_TO_DOCUMENTATION_BUTTON)

    @allure.step("Click on advert")
    def click_add(self):
        self.page.click(selector=self.locators.ADVERTISING)
