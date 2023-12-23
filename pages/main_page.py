from playwright.sync_api import Page
from locators.main_page_locators import MainPageLocators
import allure
from pages.base import BasePage


class MainPage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)
        self.locators = MainPageLocators

    @allure.step("Click on button sign in on main page")
    def click_sign_in_button(self) -> None:
        self.click(locator=self.locators.SIGN_IN_BUTTON)

    @allure.step("Click on button documentation on main page")
    def click_documentation_button(self) -> None:
        self.click(locator=self.locators.DOCUMENTATION_BUTTON)

    @allure.step("Click on button explorer on main page")
    def click_explorer_button(self) -> None:
        self.click(locator=self.locators.EXPLORER_BUTTON)

    @allure.step("Click on button Become a patreon on main page")
    def click_become_patreon(self) -> None:
        self.click(locator=self.locators.BECOME_A_PATREON_BUTTON)

    @allure.step("Click on element by locator")
    def click_by_locator(self, locator: str) -> None:
        self.click(locator=locator)
