from playwright.sync_api import Page
from locators.documentation_page_locators import DocumentationPageLocators
import allure


class DocumentationPage:
    def __init__(self, page: Page):
        self.page = page
        self.locators = DocumentationPageLocators

    @allure.step("Click on models chapters")
    def click_on_models_chapters(self):
        self.page.click(selector=self.locators.MODELS_CHAPTERS)

    @allure.step("Click on user data chapters")
    def click_on_user_data_chapters(self):
        self.page.click(selector=self.locators.USER_DATA_CHAPTERS)

    @allure.step("Click on post data chapters")
    def click_on_post_data_chapters(self):
        self.page.click(selector=self.locators.POST_DATA_CHAPTERS)

    @allure.step("Click on comment data chapters")
    def click_on_comment_data_chapters(self):
        self.page.click(selector=self.locators.COMMENT_DATA_CHAPTERS)

    @allure.step("Click on tag data chapters")
    def click_on_tag_data_chapters(self):
        self.page.click(selector=self.locators.TAG_DATA_CHAPTERS)

    @allure.step("Click on errors chapters")
    def click_on_errors_chapters(self):
        self.page.click(selector=self.locators.ERRORS_CHAPTERS)

    @allure.step("Clack on APi Explorer")
    def click_on_api_explorer(self):
        self.page.click(selector=self.locators.API_EXPLORER)

    @allure.step("Click on add")
    def click_add(self):
        self.page.click(selector=self.locators.ADD)
