from locators.explorer_page_locators import ExplorerPageLocators
from utils.list_of_data_explorer_page import ListOfDataExplorerPage
import pytest
import allure


@allure.title("Test text of title and description on the explorer page ")
@pytest.mark.explorer
def test_title_in_explorer_page(explorer_page, assertions):
    assertions.have_text(
        locator=ExplorerPageLocators.TITLE, text=ListOfDataExplorerPage.TITLE
    )
    assertions.have_text(
        locator=ExplorerPageLocators.DESCRIPTION,
        text=ListOfDataExplorerPage.DESCRIPTION,
    )


@allure.title("Test go to documentation button on the explorer page")
@allure.description(
    "Check that we go to the documentation page when click on the documentation button"
)
@pytest.mark.explorer
def test_go_to_documentation_button(explorer_page, assertions):
    explorer_page.click_go_to_documentation()
    assertions.check_url(url="https://dummyapi.io/docs")


@allure.title("Tests that we get new page after clicking add on the explorer page")
@allure.description("We can get 2 advert, we check list of add include advert")
@pytest.mark.explorer
def test_click_add_on_explorer_page(explorer_page):
    explorer_page.click_add()
    with explorer_page.page.context.expect_page() as tab:
        new_page_url = tab.value.url
    assert new_page_url in ListOfDataExplorerPage.LIST_OF_ADVERTISED_DATA


@allure.title("Test that advert change on the explorer page")
@allure.description(
    "Test retry if result is failure, because maybe we get different add"
)
@pytest.mark.explorer
@pytest.mark.flaky(reruns=5)
def test_add_change_on_explorer_page(explorer_page):
    explorer_page.click_add()
    with explorer_page.page.context.expect_page() as tab:
        new_page_url = tab.value.url
    assert new_page_url == ListOfDataExplorerPage.LIST_OF_ADVERTISED_DATA[0]


@allure.title("Checks if all the section is on the explorer page")
@allure.description("Checks if all the section is on the explorer page")
@pytest.mark.explorer
def test_text_and_count_of_sections_on_explorer_page(explorer_page, assertions):
    assertions.count_of_elements(locator=ExplorerPageLocators.SECTIONS, count=7)
    assertions.contains_text(
        locator=ExplorerPageLocators.SECTIONS, data=ListOfDataExplorerPage.SECTIONS
    )


@pytest.mark.parametrize(
    "locator_of_section, locator_of_link, result_link, locator_of_values, count, result",
    [
        pytest.param(
            ExplorerPageLocators.USER_LIST_SECTION,
            ExplorerPageLocators.API_URL,
            "https://dummyapi.io/data/v1/user?limit=10",
            ExplorerPageLocators.RESPONSE_BODY,
            10,
            ListOfDataExplorerPage.RESPONSE_OF_USERS_LIST,
            id="Test link and content of user list sections on the explorer page",
        ),
        pytest.param(
            ExplorerPageLocators.USER_PROFILE_SECTION,
            ExplorerPageLocators.API_URL,
            "https://dummyapi.io/data/v1/user/60d0fe4f5311236168a109ca",
            ExplorerPageLocators.RESPONSE_BODY,
            1,
            ListOfDataExplorerPage.RESPONSE_USERS_PROFILES,
            id="Test link and content of full user profile sections on the explorer page",
        ),
        pytest.param(
            ExplorerPageLocators.POST_LIST_SECTION,
            ExplorerPageLocators.API_URL,
            "https://dummyapi.io/data/v1/post?limit=10",
            ExplorerPageLocators.RESPONSE_BODY,
            10,
            ListOfDataExplorerPage.RESPONSE_POSTS_LIST,
            id="Test link and content of post list sections on the explorer page",
        ),
        pytest.param(
            ExplorerPageLocators.USER_POSTS_SECTION,
            ExplorerPageLocators.API_URL,
            "https://dummyapi.io/data/v1/user/60d0fe4f5311236168a109ca/post?limit=10",
            ExplorerPageLocators.RESPONSE_BODY,
            10,
            ListOfDataExplorerPage.RESPONSE_USER_POSTS,
            id="Test link and content of users post sections on the explorer page",
        ),
        pytest.param(
            ExplorerPageLocators.COMMENT_LIST_SECTION,
            ExplorerPageLocators.API_URL,
            "https://dummyapi.io/data/v1/post/60d21af267d0d8992e610b8d/comment?limit=10",
            ExplorerPageLocators.RESPONSE_BODY,
            2,
            ListOfDataExplorerPage.RESPONSE_COMMENTS_LIST,
            id="Test link and content of comments list sections on the explorer page",
        ),
        pytest.param(
            ExplorerPageLocators.TAG_LIST_SECTION,
            ExplorerPageLocators.API_URL,
            "https://dummyapi.io/data/v1/tag?limit=10",
            '//*[@id="__next"]/div/div/div[5]/div',
            1,
            ListOfDataExplorerPage.RESPONSE_TAGS_LIST,
            id="Test link and content of Tag List sections on the explorer page",
        ),
        pytest.param(
            ExplorerPageLocators.POST_BY_TAG_SECTION,
            ExplorerPageLocators.API_URL,
            "https://dummyapi.io/data/v1/tag/water/post?limit=10",
            ExplorerPageLocators.RESPONSE_BODY,
            5,
            ListOfDataExplorerPage.RESPONSE_POST_BY_TAG,
            id="Test link and content of Post by Tag sections on the explorer page",
        ),
    ],
)
@pytest.mark.explorer
def test_sections_on_explorer_page(
    explorer_page,
    assertions,
    locator_of_section,
    locator_of_link,
    result_link,
    locator_of_values,
    count,
    result,
):
    explorer_page.click_on_sections_by_locator(locator=locator_of_section)
    assertions.contains_text(locator=locator_of_link, data=result_link)
    assertions.count_of_elements(locator=locator_of_values, count=count)
    assertions.contains_text(locator=locator_of_values, data=result)
