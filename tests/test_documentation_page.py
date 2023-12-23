from utils.list_of_data_documentation_page import ListOfDataDocumentationPage
from locators.documentation_page_locators import DocumentationPageLocators
import pytest
import allure


@allure.title('Test "API Explorer" button')
@allure.description(
    'Where we click on "API Explorer" button, we go to the Explorer page'
)
@pytest.mark.doc
def test_api_explorer_on_documentation_page(documentation_page, assertions):
    documentation_page.click_on_api_explorer()
    assertions.check_url("https://dummyapi.io/explorer")


@allure.title("Tests that we get new page after clicking on add")
@allure.description("We can get 2 advert, we check list of add include advert")
@pytest.mark.doc
def test_click_add_on_documentation_page(documentation_page):
    documentation_page.click_add()
    with documentation_page.page.context.expect_page() as tab:
        new_page_url = tab.value.url
    assert new_page_url in ListOfDataDocumentationPage.LIST_OF_ADVERTISED_DATA


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
    assert new_page_url == ListOfDataDocumentationPage.LIST_OF_ADVERTISED_DATA[0]


@allure.title("Checks if all the section is on documentation page")
@allure.description("Checks if all the section is on a documentation page")
@pytest.mark.doc
def test_text_and_count_of_sections_on_documentation_page(
    documentation_page, assertions
):
    assertions.count_of_elements(locator=DocumentationPageLocators.SECTIONS, count=7)
    assertions.contains_text(
        locator=DocumentationPageLocators.SECTIONS,
        data=ListOfDataDocumentationPage.ALL_SECTIONS,
    )


@allure.title('Checks if all the paragraphs in the "Getting Started"')
@allure.description('Checks if all the paragraphs in the "Getting Started" section are')
@pytest.mark.doc
def test_text_and_count_of_paragraphs_in_getting_started_on_documentation_page(
    documentation_page, assertions
):
    locator = DocumentationPageLocators.PARAGRAPHS_IN_GETTING_STARTED
    assertions.count_of_elements(locator=locator, count=4)
    assertions.contains_text(
        locator=locator, data=ListOfDataDocumentationPage.PARAGRAPHS_IN_GETTING_STARTED
    )


@allure.title('Checks if all the paragraphs in the "Models"')
@allure.description('Checks if all the paragraphs in the "Models" section are')
@pytest.mark.doc
def test_text_and_count_of_paragraphs_in_models_on_documentation_page(
    documentation_page, assertions
):
    locator = DocumentationPageLocators.PARAGRAPHS_IN_MODELS
    documentation_page.click_on_models_chapters()
    assertions.count_of_elements(locator=locator, count=10)
    assertions.contains_text(
        locator=locator, data=ListOfDataDocumentationPage.PARAGRAPHS_IN_MODELS
    )


@allure.title('Checks if all the paragraphs in the "User data"')
@allure.description('Checks if all the paragraphs in the "User data" section are')
@pytest.mark.doc
def test_text_and_count_of_paragraphs_in_user_data_on_documentation_page(
    documentation_page, assertions
):
    locator = DocumentationPageLocators.ANY_PARAGRAPHS
    documentation_page.click_on_user_data_chapters()
    assertions.count_of_elements(locator=locator, count=5)
    assertions.contains_text(
        locator=locator, data=ListOfDataDocumentationPage.PARAGRAPHS_IN_USER_DATA
    )


@allure.title('Checks if all the paragraphs in the "Post data"')
@allure.description('Checks if all the paragraphs in the "Post data" section are')
@pytest.mark.doc
def test_text_and_count_of_paragraphs_in_post_data_on_documentation_page(
    documentation_page, assertions
):
    locator = DocumentationPageLocators.ANY_PARAGRAPHS
    documentation_page.click_on_post_data_chapters()
    assertions.count_of_elements(locator=locator, count=7)
    assertions.contains_text(
        locator=locator, data=ListOfDataDocumentationPage.PARAGRAPHS_IN_POST_DATA
    )


@allure.title('Checks if all the paragraphs in the "Comment data"')
@allure.description('Checks if all the paragraphs in the "Comment data" section are')
@pytest.mark.doc
def test_text_and_count_of_paragraphs_in_comment_data_on_documentation_page(
    documentation_page, assertions
):
    locator = DocumentationPageLocators.ANY_PARAGRAPHS
    documentation_page.click_on_comment_data_chapters()
    assertions.count_of_elements(locator=locator, count=5)
    assertions.contains_text(
        locator=locator, data=ListOfDataDocumentationPage.PARAGRAPHS_IN_COMMENT_DATA
    )


@allure.title('Checks if all the paragraphs in the "Tag data"')
@allure.description('Checks if all the paragraphs in the "Tag data" section are')
@pytest.mark.doc
def test_text_and_count_of_paragraphs_in_tag_data_on_documentation_page(
    documentation_page, assertions
):
    locator = DocumentationPageLocators.ANY_PARAGRAPHS
    documentation_page.click_on_tag_data_chapters()
    assertions.count_of_elements(locator=locator, count=1)
    assertions.contains_text(locator=locator, data="Get List")


@allure.title('Checks if all the paragraphs in the "Errors"')
@allure.description('Checks if all the paragraphs in the "Errors" section are')
@pytest.mark.doc
def test_text_and_count_of_paragraphs_in_errors_on_documentation_page(
    documentation_page, assertions
):
    locator = DocumentationPageLocators.ANY_PARAGRAPHS
    documentation_page.click_on_errors_chapters()
    assertions.count_of_elements(locator=locator, count=7)
    assertions.contains_text(
        locator=locator, data=ListOfDataDocumentationPage.ERRORS_DATA
    )
