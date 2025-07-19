import allure
from playwright.sync_api import Page, expect
from pagesObjects.BasePage import BasePage


class HomePage(BasePage):

    def __init__(self, page: Page):
        super().__init__(page)


    #locators
        self.login_bouton = page.locator('#login2')
        self.signup_bouton = page.locator('#signin2')
        self.titre_popin_signup = page.locator('#signInModalLabel')
        self.titre_popin_login = page.locator('#logInModalLabel')
        self.champ_user_name = page.locator('#sign-username')
        self.champ_password = page.locator('#sign-password')
        self.login_champ_user_name = page.locator('#loginusername')
        self.login_champ_password = page.locator('#loginpassword')
        self.signup_bouton_popin = page.locator('button[onclick="register()"]')
        self.login_bouton_popin = page.get_by_role('button', name='Log in')

    #methodes

    def verifier_que_le_user_est_sur_la_homePage(self):
        expect(self.page).to_have_title("STORE")

    def cliquer_sur_le_bouton_login(self):
        self.cliquer_sur_un_element(self.login_bouton)

    def cliquer_sur_le_bouton_signup(self):
        self.cliquer_sur_un_element(self.signup_bouton)

    def verifier_louverture_de_la_popin_signup(self):
        self.verifier_que_element_est_visible(self.titre_popin_signup, "Sign up")

    def verifier_louverture_de_la_popin_login(self):
        self.verifier_que_element_est_visible(self.titre_popin_login, "Log in")

    def saisir_les_credentials(self, username, password):
        self.remplir_le_champ(self.champ_user_name, username)
        self.remplir_le_champ(self.champ_password, password)

    def saisir_les_credentials_login(self, username, password):
        self.remplir_le_champ(self.login_champ_user_name, username)
        self.remplir_le_champ(self.login_champ_password, password)

    def cliquer_sur_signup_boutton_popin(self):
        # self.page.once("dialog", lambda dialog: dialog.accept())
        self.cliquer_sur_un_element(self.signup_bouton_popin)

    def cliquer_sur_login_boutton_popin(self):
        self.cliquer_sur_un_element(self.login_bouton_popin)





