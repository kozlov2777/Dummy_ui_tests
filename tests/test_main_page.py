import pytest
from playwright.sync_api import expect
from locators.main_page_locators import MainPageLocators
from utils.list_of_data_main_page import ListOfDataMainPage
import allure


@pytest.mark.main_page
def test_something(main_page, assertions):
    assertions.have_text(locator=MainPageLocators.SIGN_IN_BUTTON, text="Sign In")
    main_page.click_sign_in_button()
    assertions.check_url(url="https://dummyapi.io/sign-in")


@pytest.mark.main_page
def test_documentation_button(main_page, assertions):
    assertions.have_text(
        locator=MainPageLocators.DOCUMENTATION_BUTTON, text="Documentation"
    )
    main_page.click_documentation_button()
    assertions.check_url(url="https://dummyapi.io/docs")


@pytest.mark.main_page
def test_explorer_button(main_page, assertions):
    assertions.have_text(locator=MainPageLocators.EXPLORER_BUTTON, text="Explorer")
    main_page.click_explorer_button()
    expect(main_page.page).to_have_url("https://dummyapi.io/explorer")


@allure.title('Checks if all the features on main page"')
@allure.description('Checks if all the feature in the "features" section are')
@pytest.mark.main_page
def test_text_and_count_of_features_on_main_page(main_page, assertions):
    locator = MainPageLocators.FEATURES
    assertions.count_of_elements(locator=locator, count=6)
    assertions.contains_text(locator=locator, data=ListOfDataMainPage.FUTURES)


@allure.title('Checks if all the left use case on main page"')
@allure.description('Checks if all the "use cases" in the left section are')
@pytest.mark.main_page
def test_text_and_count_of_left_use_case_on_main_page(main_page, assertions):
    locator = MainPageLocators.USE_CASES_LEFT
    assertions.count_of_elements(locator=locator, count=3)
    assertions.contains_text(locator=locator, data=ListOfDataMainPage.USE_CASES_LEFT)


@allure.title('Checks if all the right use case on main page"')
@allure.description('Checks if all the "use cases" in the right section are')
@pytest.mark.main_page
def test_text_and_count_of_right_use_case_on_main_page(main_page, assertions):
    locator = MainPageLocators.USE_CASES_RIGHT
    assertions.count_of_elements(locator=locator, count=3)
    assertions.contains_text(locator=locator, data=ListOfDataMainPage.USE_CASES_RIGHT)


@allure.title('Checks if all the usage statistic on main page"')
@allure.description('Checks if all the statistic in the "usage statistic" section are')
@pytest.mark.main_page
def test_text_and_count_of_usage_statistic_on_main_page(main_page, assertions):
    locator = MainPageLocators.USAGE_STATISTICS
    assertions.count_of_elements(locator=locator, count=3)
    assertions.contains_text(locator=locator, data=ListOfDataMainPage.USAGE_STATISTICS)


@allure.title('Checks our sponsors on main page"')
@allure.description('Checks "our sponsors" section are')
@pytest.mark.main_page
def test_text_and_count_of_our_sponsors_on_main_page(main_page, assertions):
    locator = MainPageLocators.OUR_SPONSORS_ARTICLE
    assertions.count_of_elements(locator=locator, count=1)
    assertions.contains_text(locator=locator, data=ListOfDataMainPage.OUR_SPONSORS)


@allure.title("Tests that we get new page after clicking on Become a patreon")
@allure.description("We go to new page with url: https://www.patreon.com/join/dummyapi")
@pytest.mark.main_page
def test_click_become_patreon_on_main_page(main_page):
    main_page.click_become_patreon()
    with main_page.page.context.expect_page() as tab:
        new_page_url = tab.value.url
    assert new_page_url == "https://www.patreon.com/join/dummyapi"


@allure.title('Checks if all the  left related links on main page"')
@allure.description("Checks if all the left related links in the section are")
@pytest.mark.main_page
def test_text_and_count_of_left_related_links_on_main_page(main_page, assertions):
    locator = MainPageLocators.RELATED_LINKS_LEFT
    assertions.count_of_elements(locator=locator, count=2)
    assertions.contains_text(
        locator=locator, data=ListOfDataMainPage.RELATED_LINKS_LEFT
    )


@allure.title('Checks if all the  right related links on main page"')
@allure.description("Checks if all the right related links in the section are")
@pytest.mark.main_page
def test_text_and_count_of_right_related_links_on_main_page(main_page, assertions):
    locator = MainPageLocators.RELATED_LINKS_RIGHT
    assertions.count_of_elements(locator=locator, count=2)
    assertions.contains_text(
        locator=locator, data=ListOfDataMainPage.RELATED_LINKS_RIGHT
    )


@allure.description(
    "Tests that we get new page after clicking on link in Related links"
)
@pytest.mark.parametrize(
    "locator, url",
    [
        pytest.param(
            MainPageLocators.TELEGRAM_COMMUNITY,
            "https://t.me/dummyapi",
            id="Click on DummyAPI Telegram Community",
        ),
        pytest.param(
            MainPageLocators.TELEGRAM_CHAT,
            "https://t.me/dummyapi",
            id="Click on DummyAPI Telegram Chat",
        ),
        pytest.param(
            MainPageLocators.RANDOM_USER,
            "https://randomuser.me/",
            id="Click on randomuser.me",
        ),
        pytest.param(
            MainPageLocators.RANDOM_USER_LICENSE,
            "https://randomuser.me/copyright",
            id="Click on randomuser.me/copyright",
        ),
        pytest.param(
            MainPageLocators.UNSPLASH,
            "https://unsplash.com/",
            id="Click on unsplash.com",
        ),
        pytest.param(
            MainPageLocators.UNSPLASH_LICENSE,
            "https://unsplash.com/license",
            id="Click on unsplash.com/license",
        ),
        pytest.param(
            MainPageLocators.RGBTOHEX,
            "https://rgbtohex.page/",
            id="Click on https://rgbtohex.page",
        ),
    ],
)
@pytest.mark.main_page
def test_click_link_in_related_links_on_main_page(main_page, locator, url):
    main_page.click_by_locator(locator=locator)
    with main_page.page.context.expect_page() as tab:
        new_page_url = tab.value.url
    assert new_page_url == url
