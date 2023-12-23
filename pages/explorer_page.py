from playwright.sync_api import Page
from locators.explorer_page_locators import ExplorerPageLocators
import allure
from pages.base import BasePage


class ExplorerPage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)
        self.locators = ExplorerPageLocators

    @allure.step("Click go to documentation button")
    def click_go_to_documentation(self):
        self.click(locator=self.locators.GO_TO_DOCUMENTATION_BUTTON)

    @allure.step("Click on advert")
    def click_add(self):
        self.click(locator=self.locators.ADVERTISING)

    @allure.step("Click on section by locator")
    def click_on_sections_by_locator(self, locator: str):
        self.click(locator=locator)
