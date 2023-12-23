from playwright.sync_api import Page


class BasePage:
    def __init__(self, page: Page):
        self.page = page

    def click(self, locator: str) -> None:
        self.page.click(selector=locator)

    def input(self, locator: str, data: str) -> None:
        self.page.locator(selector=locator).fill(value=data)

    def get_text(self, locator: str, index: int) -> str:
        return self.page.locator(selector=locator).nth(index=index).text_content()

    def wait_for_elem(self, locator: str, timeout=12000) -> None:
        self.page.wait_for_selector(selector=locator, timeout=timeout)

    def current_url(self) -> str:
        return self.page.url
