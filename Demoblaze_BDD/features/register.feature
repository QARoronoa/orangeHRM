Feature: register

  Scenario Outline: Créer un compte avec des informations valides
    Given l’utilisateur est sur la page d’accueil
    When il clique sur "Sign up"
    And il visualise la popin avec le titre signup
    And saisit un nouveau nom d'utilisateur et password <username> <password>
    And clique sur "Sign up"
#    Then un message de confirmation s’affiche

 Examples:
  |username|password|
  | test123| test123|

