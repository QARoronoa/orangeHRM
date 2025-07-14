import locator
from playwright.sync_api import Page, Locator, expect


class BasePage():
    def __init__(self, page: Page):
        self.page = page

    def cliquer_sur_un_element(self, locator: Locator):
        expect(locator).to_be_visible()
        expect(locator).to_be_enabled()
        locator.click()

    def verifier_que_element_est_visible(self, locator: Locator, text):
        expect(locator).to_be_visible()
        expect(locator).to_contain_text(text)

    def remplir_le_champ(self, locator: Locator, text):
        expect(locator).to_be_visible()
        locator.clear()
        locator.fill(text)

