import pytest
from playwright.sync_api import expect
import allure


@allure.title("Test text of title and description on the explorer page ")
@pytest.mark.explorer
def test_title_in_explorer_page(explorer_page):
    expect(
        explorer_page.page.locator('//*[@id="__next"]/div/div/div[1]/div/h1')
    ).to_have_text("API Data Explorer")
    expect(
        explorer_page.page.locator('//*[@id="__next"]/div/div/div[1]/p')
    ).to_have_text(
        "Example of API User Data limited to 10 items per collection. Click on links to move between different data sets."
    )


@allure.title("Test go to documentation button on the explorer page")
@allure.description(
    "Check that we go to the documentation page when click on the documentation button"
)
@pytest.mark.explorer
def test_go_to_documentation_button(explorer_page):
    explorer_page.click_go_to_documentation()
    expect(explorer_page.page).to_have_url("https://dummyapi.io/docs")


@allure.title("Tests that we get new page after clicking add on the explorer page")
@allure.description("We can get 2 advert, we check list of add include advert")
@pytest.mark.explorer
def test_click_add_on_explorer_page(explorer_page):
    explorer_page.click_add()
    list_of_add = [
        "https://www.bluehost.com/?utm_medium=affiliate&irpid=105&channelid=P99C46097236S653N0B3A151D855E0000V100&utm_source=IR",
        "https://www.templatemonster.com/website-templates.php?aff=dummyapi&a_bid=9d380bcb&chan=dummyapi",
    ]
    with explorer_page.page.context.expect_page() as tab:
        new_page_url = tab.value.url
    assert new_page_url in list_of_add


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
    assert (
        new_page_url
        == "https://www.bluehost.com/?utm_medium=affiliate&irpid=105&channelid=P99C46097236S653N0B3A151D855E0000V100&utm_source=IR"
    )


@allure.title("Checks if all the section is on the explorer page")
@allure.description("Checks if all the section is on the explorer page")
@pytest.mark.explorer
def test_text_and_count_of_sections_on_explorer_page(explorer_page):
    locator = '//*[@id="__next"]/div/div/div[3]/div/div'
    (expect(explorer_page.page.locator(locator)).to_have_count(7))
    (
        expect(explorer_page.page.locator(locator)).to_contain_text(
            [
                "Users List",
                "Full User Profile",
                "Posts List",
                "User Posts",
                "Comments List",
                "Tag List",
                "Post by Tag",
            ]
        )
    )


@pytest.mark.parametrize(
    "locator_of_section, locator_of_link, result_link, locator_of_values, count, result",
    [
        pytest.param(
            '//*[@id="__next"]/div/div/div[3]/div/div[1]',
            '//*[@id="__next"]/div/div/div[4]',
            "https://dummyapi.io/data/v1/user?limit=10",
            '//*[@id="__next"]/div/div/div[5]/div/div',
            10,
            [
                "ms. Ann Mason",
                "mr. Sohan Pierre",
                "mr. Gonzaga Ribeiro",
                "mrs. Josefina Calvo",
                "mrs. Els Ijsseldijk",
                "mr. Jesus Riley",
                "mr. Andri Leclerc",
                "mr. Konsta Manninen",
                "ms. Ane Frafjord",
                "mrs. OlaÃ­ Gomes",
            ],
            id="Test link and content of user list sections on the explorer page",
        ),
        pytest.param(
            '//*[@id="__next"]/div/div/div[3]/div/div[2]',
            '//*[@id="__next"]/div/div/div[4]',
            "https://dummyapi.io/data/v1/user/60d0fe4f5311236168a109ca",
            '//*[@id="__next"]/div/div/div[5]/div/div',
            1,
            ["ms. Sara Andersen", "sara.andersen@example.com"],
            id="Test link and content of full user profile sections on the explorer page",
        ),
        pytest.param(
            '//*[@id="__next"]/div/div/div[3]/div/div[3]',
            '//*[@id="__next"]/div/div/div[4]',
            "https://dummyapi.io/data/v1/post?limit=10",
            '//*[@id="__next"]/div/div/div[5]/div/div',
            10,
            [
                [
                    "ms. Vanessa Ramos",
                    "Dog in a forest at sunset dog in forest with sun",
                ],
                ["mr. Cameron Mendoza", "white black and brown long coated small dog"],
            ],
            id="Test link and content of post list sections on the explorer page",
        ),
        pytest.param(
            '//*[@id="__next"]/div/div/div[3]/div/div[4]',
            '//*[@id="__next"]/div/div/div[4]',
            "https://dummyapi.io/data/v1/user/60d0fe4f5311236168a109ca/post?limit=10",
            '//*[@id="__next"]/div/div/div[5]/div/div',
            10,
            [
                ["6560d2cabb702eadb7bf87db", "some trwerext"],
                ["6560bfa83101fd637e96a7e1", "some text"],
            ],
            id="Test link and content of users post sections on the explorer page",
        ),
        pytest.param(
            '//*[@id="__next"]/div/div/div[3]/div/div[5]',
            '//*[@id="__next"]/div/div/div[4]',
            "https://dummyapi.io/data/v1/post/60d21af267d0d8992e610b8d/comment?limit=10",
            '//*[@id="__next"]/div/div/div[5]/div/div',
            2,
            [
                ["mrs. Anaelle Dumas", "Nice pic"],
                ["mr. Kenneth Carter", "Handsome pic!!!"],
            ],
            id="Test link and content of comments list sections on the explorer page",
        ),
        pytest.param(
            '//*[@id="__next"]/div/div/div[3]/div/div[6]',
            '//*[@id="__next"]/div/div/div[4]',
            "https://dummyapi.io/data/v1/tag?limit=10",
            '//*[@id="__next"]/div/div/div[5]/div',
            1,
            [["test"], ["якрутой"]],
            id="Test link and content of Post by Tag sections on the explorer page",
        ),
        pytest.param(
            '//*[@id="__next"]/div/div/div[3]/div/div[7]',
            '//*[@id="__next"]/div/div/div[4]',
            "https://dummyapi.io/data/v1/tag/water/post?limit=10",
            '//*[@id="__next"]/div/div/div[5]/div/div',
            5,
            [
                [
                    "mr. Jan Siebert",
                    "Cooling off in the fountain white and black short",
                    "water",
                ],
                ["ms. Ann Mason", "dog in a dock by a lake", "water"],
            ],
            id="Test link and content of Post by Tag sections on the explorer page",
        ),
    ],
)
@pytest.mark.explorer
def test_sections_on_explorer_page(
    explorer_page,
    locator_of_section,
    locator_of_link,
    result_link,
    locator_of_values,
    count,
    result,
):
    explorer_page.page.click(selector=locator_of_section)
    expect(explorer_page.page.locator(locator_of_link)).to_have_text(result_link)
    expect(explorer_page.page.locator(locator_of_values)).to_have_count(count)
    expect(explorer_page.page.locator(locator_of_values)).to_contain_text(result)
