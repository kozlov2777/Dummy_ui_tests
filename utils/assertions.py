from pages.base import BasePage
from playwright.sync_api import Page, expect


class Assertions(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)

    def check_url(self, url: str):
        expect(self.page).to_have_url(url)

    def have_text(self, locator: str, text: str):
        loc = self.page.locator(locator)
        expect(loc).to_have_text(text)

    def check_presence(self, locator: str):
        loc = self.page.locator(locator)
        expect(loc).to_be_visible(visible=True, timeout=12000)

    def check_absence(self, locator: str):
        loc = self.page.locator(locator)
        expect(loc).to_be_hidden(timeout=700)

    def count_of_elements(self, locator: str, count: int):
        loc = self.page.locator(locator)
        expect(loc).to_have_count(count=count)

    def contains_text(self, locator: str, data: list):
        loc = self.page.locator(locator)
        expect(loc).to_contain_text(expected=data)
