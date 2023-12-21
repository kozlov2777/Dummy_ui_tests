import time

import playwright.sync_api
import pytest
from playwright.sync_api import expect, Cookie


@pytest.mark.login
def test_something(main_page):
    main_page.click_sign_in_button()
    expect(
        main_page.page.locator('//*[@id="__next"]/div/div/div[1]/div/h1')
    ).to_contain_text(expected="Sign in")
    expect(main_page.page).to_have_url("https://dummyapi.io/sign-in")


@pytest.mark.doc
def test_documentation_button(main_page):
    main_page.click_documentation_button()
    expect(
        main_page.page.locator('//*[@id="__next"]/div/div/div[1]/div/h1')
    ).to_contain_text(expected="Documentation")
    expect(main_page.page).to_have_url("https://dummyapi.io/docs")


@pytest.mark.explorer
def test_explorer_button(main_page):
    main_page.click_explorer_button()
    expect(
        main_page.page.locator('//*[@id="__next"]/div/div/div[1]/div/h1')
    ).to_contain_text(expected="API Data Explorer")
    expect(main_page.page).to_have_url("https://dummyapi.io/explorer")

@pytest.mark.e2e
def test(main_page):
    main_page.page.click(selector='//*[@id="__next"]/div/header/div/div[2]/a')
    main_page.page.click(selector='//*[@id="firebaseui_container"]/div/div[1]/form/ul/li[1]/button/span[2]')
    main_page.page.fill(selector='//*[@id="identifierId"]', value='kozlov2777@gmail.com')
    main_page.page.click(selector='//*[@id="identifierNext"]/div/button/span')
    main_page.page.fill(selector='//*[@id="password"]/div[1]/div/div[1]/input', value='somepassword')
