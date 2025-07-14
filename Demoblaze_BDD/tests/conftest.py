import pytest
from playwright.sync_api import Page

@pytest.fixture(scope="function")
def setup(playwright):
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()

    page = context.new_page()
    page.goto('https://www.demoblaze.com/')
    yield page

    context.close()
    browser.close()
