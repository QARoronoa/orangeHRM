Feature: Login

Scenario Outline: Connexion avec des identifiants valides

  Given l’utilisateur est sur la page d’accueil
  When il clique sur "Log in"
  And il visualise la popin avec le titre login
  And saisit un nouveau nom d'utilisateur et password <username> <password>
  And clique sur le bouton "Log in"
#  Then il est connecté et voit son nom d'utilisateur dans le menu


  Examples:
  |username|password|
  | test123| test123|
