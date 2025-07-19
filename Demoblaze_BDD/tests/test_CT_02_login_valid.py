import time

import allure

from pagesObjects.HomePage import HomePage
from pytest_bdd import scenarios, given, when, step, parsers

scenarios('../features/login.feature')

@given('l’utilisateur est sur la page d’accueil')
def user_est_sur_la_page_dacceuil(setup):
    with allure.step("Go to home page"):
        home_page = HomePage(setup)
        home_page.verifier_que_le_user_est_sur_la_homePage()

@when('il clique sur "Log in"')
def user_clique_sur_le_boutton_login(setup):
    with allure.step("Clique sur le bouton 'Log in' (header)"):
        home_page = HomePage(setup)
        home_page.cliquer_sur_le_bouton_login()

@step('il visualise la popin avec le titre login')
def user_visualise_la_popin_login(setup):
    with allure.step('Vérifie que la popin de connexion est visible'):
        home_page = HomePage(setup)
        home_page.verifier_louverture_de_la_popin_login()

@step(parsers.parse('saisit un nouveau nom d\'utilisateur et password {username} {password}'))
def user_saisit_lidentifiant_et_le_mot_de_passe(setup, username, password):
    with allure.step(f"Saisit identifiants : username = {username}, password = {password}"):
        home_page = HomePage(setup)
        home_page.saisir_les_credentials_login(username, password)

@step('clique sur le bouton "Log in"')
def user_clique_sur_login_boutton_popin(setup):
    with allure.step('Clique sur le bouton "Log in" dans la popin'):
        home_page = HomePage(setup)
        home_page.cliquer_sur_login_boutton_popin()
