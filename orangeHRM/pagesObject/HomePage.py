from pagesObject.BasePage import BasePage


class HomePage(BasePage):
    def __init__(self, page):
        super().__init__(page)

        #locators
        self.texte_dashboard = page.locator('h6.oxd-text', has_text="Dashboard")
        self.menu_user = page.locator(".oxd-userdropdown-name")
        self.bouton_logout = page.locator("a.oxd-userdropdown-link", has_text="Logout")


        #methodes
    def verifier_la_redirection_vers_dashboard(self):
        self.verifier_le_texte_de_lelement(self.texte_dashboard,"Dashboard")

    def cliquer_sur_menu_utilisateur(self):
        self.cliquer_sur_un_element(self.menu_user)

    def cliquer_sur_logout(self):
        self.cliquer_sur_un_element(self.bouton_logout)
