from playwright.sync_api import Page
from locators.main_page_locators import MainPageLocators
import allure


class MainPage:
    def __init__(self, page: Page) -> None:
        self.page = page
        self.locators = MainPageLocators

    @allure.step("Click on button sign in on main page")
    def click_sign_in_button(self) -> None:
        self.page.locator(selector=self.locators.SignInBtn).click()

    @allure.step("Click on button documentation on main page")
    def click_documentation_button(self) -> None:
        self.page.locator(selector=self.locators.DocumentationBtn).click()

    @allure.step("Click on button explorer on main page")
    def click_explorer_button(self) -> None:
        self.page.locator(selector=self.locators.ExplorerBtn).click()
