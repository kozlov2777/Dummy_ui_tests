import pytest
from playwright.sync_api import expect
import allure


@allure.title('Test "API Explorer" button')
@allure.description(
    'Where we click on "API Explorer" button, we go to the Explorer page'
)
@pytest.mark.doc
def test_api_explorer_on_documentation_page(documentation_page):
    documentation_page.click_on_api_explorer()
    expect(documentation_page.page).to_have_url("https://dummyapi.io/explorer")


@allure.title("Tests that we get new page after clicking on add")
@allure.description("We can get 2 advert, we check list of add include advert")
@pytest.mark.doc
def test_click_add_on_documentation_page(documentation_page):
    documentation_page.click_add()
    list_of_add = [
        "https://www.bluehost.com/?utm_medium=affiliate&irpid=105&channelid=P99C46097236S653N0B3A151D855E0000V100&utm_source=IR",
        "https://www.templatemonster.com/website-templates.php?aff=dummyapi&a_bid=9d380bcb&chan=dummyapi",
    ]
    with documentation_page.page.context.expect_page() as tab:
        new_page_url = tab.value.url
    assert new_page_url in list_of_add


@allure.title("Test that advert change")
@allure.description(
    "Test retry if result is failure, because maybe we get different add"
)
@pytest.mark.doc
@pytest.mark.flaky(reruns=5)
def test_add_change_on_documentation_page(documentation_page):
    documentation_page.click_add()
    with documentation_page.page.context.expect_page() as tab:
        new_page_url = tab.value.url
    assert (
        new_page_url
        == "https://www.bluehost.com/?utm_medium=affiliate&irpid=105&channelid=P99C46097236S653N0B3A151D855E0000V100&utm_source=IR"
    )


@allure.title("Checks if all the section is on documentation page")
@allure.description("Checks if all the section is on a documentation page")
@pytest.mark.doc
def test_text_and_count_of_sections_on_documentation_page(documentation_page):
    locator = '//*[@id="__next"]/div/div/div[3]/div/div[1]/div/div'
    (expect(documentation_page.page.locator(locator)).to_have_count(7))
    (
        expect(documentation_page.page.locator(locator)).to_contain_text(
            [
                "Getting Started",
                "Models",
                "User Data",
                "Post Data",
                "Comment Data",
                "Tag Data",
                "Errors",
            ]
        )
    )


@allure.title('Checks if all the paragraphs in the "Getting Started"')
@allure.description('Checks if all the paragraphs in the "Getting Started" section are')
@pytest.mark.doc
def test_text_and_count_of_paragraphs_in_getting_started_on_documentation_page(
    documentation_page,
):
    locator = '//*[@id="__next"]/div/div/div[3]/div/div[2]/h3'
    (expect(documentation_page.page.locator(locator)).to_have_count(4))
    (
        expect(documentation_page.page.locator(locator)).to_contain_text(
            ["Base URL", "Header", "Paging", "Created"]
        )
    )


@allure.title('Checks if all the paragraphs in the "Models"')
@allure.description('Checks if all the paragraphs in the "Models" section are')
@pytest.mark.doc
def test_text_and_count_of_paragraphs_in_models_on_documentation_page(
    documentation_page,
):
    locator = '//*[@id="__next"]/div/div/div[3]/div/div[2]/h3'
    documentation_page.click_on_models_chapters()
    (expect(documentation_page.page.locator(locator)).to_have_count(10))
    (
        expect(documentation_page.page.locator(locator)).to_contain_text(
            [
                "List",
                "User Preview",
                "User Full",
                "Location",
                "Post Create",
                "Post Preview",
                "Post",
                "Comment Create",
                "Comment",
                "Tag",
            ]
        )
    )


@allure.title('Checks if all the paragraphs in the "User data"')
@allure.description('Checks if all the paragraphs in the "User data" section are')
@pytest.mark.doc
def test_text_and_count_of_paragraphs_in_user_data_on_documentation_page(
    documentation_page,
):
    locator = '//*[@id="__next"]/div/div/div[3]/div/div[2]/div'
    documentation_page.click_on_user_data_chapters()
    (expect(documentation_page.page.locator(locator)).to_have_count(5))
    (
        expect(documentation_page.page.locator(locator)).to_contain_text(
            ["Get List", "Get User by id", "Create User", "Update User", "Delete User"]
        )
    )


@allure.title('Checks if all the paragraphs in the "Post data"')
@allure.description('Checks if all the paragraphs in the "Post data" section are')
@pytest.mark.doc
def test_text_and_count_of_paragraphs_in_post_data_on_documentation_page(
    documentation_page,
):
    locator = '//*[@id="__next"]/div/div/div[3]/div/div[2]/div'
    documentation_page.click_on_post_data_chapters()
    (expect(documentation_page.page.locator(locator)).to_have_count(7))
    (
        expect(documentation_page.page.locator(locator)).to_contain_text(
            [
                "Get List",
                "Get List By User",
                "Get List By Tag",
                "Get Post by id",
                "Create Post",
                "Update Post",
                "Delete Post",
            ]
        )
    )


@allure.title('Checks if all the paragraphs in the "Comment data"')
@allure.description('Checks if all the paragraphs in the "Comment data" section are')
@pytest.mark.doc
def test_text_and_count_of_paragraphs_in_comment_data_on_documentation_page(
    documentation_page,
):
    locator = '//*[@id="__next"]/div/div/div[3]/div/div[2]/div'
    documentation_page.click_on_comment_data_chapters()
    (expect(documentation_page.page.locator(locator)).to_have_count(5))
    (
        expect(documentation_page.page.locator(locator)).to_contain_text(
            [
                "Get List",
                "Get List By Post",
                "Get List By User",
                "Create Comment",
                "Delete Comment",
            ]
        )
    )


@allure.title('Checks if all the paragraphs in the "Tag data"')
@allure.description('Checks if all the paragraphs in the "Tag data" section are')
@pytest.mark.doc
def test_text_and_count_of_paragraphs_in_tag_data_on_documentation_page(
    documentation_page,
):
    locator = '//*[@id="__next"]/div/div/div[3]/div/div[2]/div'
    documentation_page.click_on_tag_data_chapters()
    (expect(documentation_page.page.locator(locator)).to_have_count(1))
    (expect(documentation_page.page.locator(locator)).to_contain_text("Get List"))


@allure.title('Checks if all the paragraphs in the "Errors"')
@allure.description('Checks if all the paragraphs in the "Errors" section are')
@pytest.mark.doc
def test_text_and_count_of_paragraphs_in_errors_on_documentation_page(
    documentation_page,
):
    locator = '//*[@id="__next"]/div/div/div[3]/div/div[2]/div'
    documentation_page.click_on_errors_chapters()
    (expect(documentation_page.page.locator(locator)).to_have_count(7))
    (
        expect(documentation_page.page.locator(locator)).to_contain_text(
            [
                "APP_ID_NOT_EXIST",
                "APP_ID_MISSING",
                "PARAMS_NOT_VALID",
                "BODY_NOT_VALID",
                "RESOURCE_NOT_FOUND",
                "PATH_NOT_FOUND",
                "SERVER_ERROR",
            ]
        )
    )
