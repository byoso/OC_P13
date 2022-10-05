![logo](https://user.oc-static.com/upload/2020/09/18/16004295603423_P11.png)

## Résumé

Site web d'Orange County Lettings

## Développement local

### Prérequis

- Compte GitHub avec accès en lecture à ce repository
- Git CLI
- SQLite3 CLI
- Interpréteur Python, version 3.6 ou supérieure

Dans le reste de la documentation sur le développement local, il est supposé que la commande `python` de votre OS shell exécute l'interpréteur Python ci-dessus (à moins qu'un environnement virtuel ne soit activé).

### macOS / Linux

#### Cloner le repository

- `cd /path/to/put/project/in`
- `git clone https://github.com/OpenClassrooms-Student-Center/Python-OC-Lettings-FR.git`

#### Créer l'environnement virtuel

- `cd /path/to/Python-OC-Lettings-FR`
- `python -m venv venv`
- `apt-get install python3-venv` (Si l'étape précédente comporte des erreurs avec un paquet non trouvé sur Ubuntu)
- Activer l'environnement `source venv/bin/activate`
- Confirmer que la commande `python` exécute l'interpréteur Python dans l'environnement virtuel
`which python`
- Confirmer que la version de l'interpréteur Python est la version 3.6 ou supérieure `python --version`
- Confirmer que la commande `pip` exécute l'exécutable pip dans l'environnement virtuel, `which pip`
- Pour désactiver l'environnement, `deactivate`

#### Exécuter le site

- `cd /path/to/Python-OC-Lettings-FR`
- `source venv/bin/activate`
- `pip install --requirement requirements.txt`
- `python manage.py runserver`
- Aller sur `http://localhost:8000` dans un navigateur.
- Confirmer que le site fonctionne et qu'il est possible de naviguer (vous devriez voir plusieurs profils et locations).

#### Linting

- `cd /path/to/Python-OC-Lettings-FR`
- `source venv/bin/activate`
- `flake8`

#### Tests unitaires

- `cd /path/to/Python-OC-Lettings-FR`
- `source venv/bin/activate`
- `pytest`

#### Base de données

- `cd /path/to/Python-OC-Lettings-FR`
- Ouvrir une session shell `sqlite3`
- Se connecter à la base de données `.open oc-lettings-site.sqlite3`
- Afficher les tables dans la base de données `.tables`
- Afficher les colonnes dans le tableau des profils, `pragma table_info(oc_lettings_site_profile);`
- Lancer une requête sur la table des profils, `select user_id, favorite_city from
  oc_lettings_site_profile where favorite_city like 'B%';`
- `.quit` pour quitter

#### Panel d'administration

- Aller sur `http://localhost:8000/admin`
- Connectez-vous avec l'utilisateur `admin`, mot de passe `Abc1234!`

### Windows

Utilisation de PowerShell, comme ci-dessus sauf :

- Pour activer l'environnement virtuel, `.\venv\Scripts\Activate.ps1`
- Remplacer `which <my-command>` par `(Get-Command <my-command>).Path`

----
## Déploiement

### Fonctionnement général, intégration continue
Ce projet sera déployé en intégration continue à destination de heroku. On utilisera différents services :
- **docker**: le projet sera conteneurisé avec docker
- **github** : hébergement du code source du projet
- **circleci** : circleci récupérera le code source sur github, puis effectuera des test de vérification du code source, avant de créer une image docker du projet, et de l'envoyer sur dockerhub et heroku.
- **dockerhub** : héberge une copie de l'image du projet
- **heroku** : hébergement du site lui-même
- **sentry** : sentry sera chargé de surveiller l'activité du server sur heroku, et de nous informer d'éventuelles erreurs.

### Configuration des services
Pour commencer il faut avoir installé sur la machine locale de développement les applications `docker`, `git`, et `heroku`.

- **sentry**: un projet a été défini sur le site de sentry pour oc-lettings
- **docker**: l'image docker est construite  partir du fichier `Dockerfile`
- **github** : le depot github du projet se trouve ici: https://github.com/byoso/OC_P13
- **circleci**: les logs de circleci du projet se trouvent ici: https://app.circleci.com/pipelines/github/byoso/OC_P13.

Circleci est paramétré pour suivre les modifications de code sur github, et agira en fonction.
Les actions de circleci sont pilotées par le fichier `.circleci/config.yml`, qui fait appel à 3 variables d'environement définies dans le context donné sur le site de circleci  (Organization Settings->Contexts->circleci_context).

| varibles d'environement définies pour Circleci            | utilité                      |
|---                                                                                                  |---                               |
| DOCKERHUB_LOGIN                                                            | login de connexion au compte dokerhub |
| DOCKERHUB_PASSWORD                                                 | mot de passe de connexion au compte dokerhub |
| HEROKU_TOKEN                                                                   | token d'authentification du projet pour heroku |

- **Heroku**: Heroku utilisera aussi des variables d’environnement. Le plus simple pour ce projet est d'utiliser le script `heroku_pusher.sh` pour créer le site sur heroku, puis de définir ces variables en executant le script `heroku_environment.sh` (non fourni avec le code source)

| varibles d'environement définies pour Heroku | utilité |
|--- |--- |
| DJANGO_SECRET_KEY                                              | clé secrète utilisée par django en produciton  |
| ENV                                                                                  | valeur: 'production' ainsi le site déployé sur heroku prendra sa configuration de production |
| SENTRY_DSN                                                                | url fournie par sentry pour le suivi du serveur  |


### Procédures de déploiement
#### Si le site à été complètement supprimé de Heroku
Depuis le répertoire local du projet, recréer le site sur Heroku:
```bash
heroku login
heroku container:login
heroku create oc-lettings-vf
heroku git:remote -a oc-lettings-vf
```
Et restaurez l'environement sur Heroku:
- restaurez les variables d'environement sur heroku en exécutant le script: `heroku_environment.sh` (ce script n'est pas fourni sur les plateformes publiques). Son contenu est structuré comme suit:
```bash
#! /bin/bash
heroku config:set ENV=production
heroku config:set DJANGO_SECRET_KEY=xxx
heroku config:set SENTRY_DSN=xxx
```

#### 1. Si déploiement avec Circleci (procédure normale)
Circleci est paramétré pour suivre le code du projet sur github. Un 'push ' sur n'importe quelle branche ne déclenchera que les test (flake8 et pytest) sur circleci. Un 'push' sur la branche `master` provoquera l’exécution des test, puis le déploiement sur heroku si les tests sont réussi.

#### 2. Si déploiement direct depuis le repertoire local
Construire l'image docker (si vous n'en avez pas déjà):
```
docker build -t oc_lettings_site .  # ne pas oublier le '.'
# verifier que l'image fonctionne:
doker run -p 8000:8000 oc_lettings_site
# voir le container créé (notez son 'name'):
docker container ps -a
# arréter le container (ouvrir un autre terminal):
docker stop <name>
# tagger l'image:
docker tag oc_lettings_site byoso/oc-lettings:oc_lettings_site
# push de l'image sur dockerhub
docker push byoso/oc-lettings:oc_lettings_site

```
puis pusher sur heroku:
```
heroku container:push web
heroku container:release web
```
#### Autres cas
Adaptez le script `heroku_pusher.sh` en commentant les lignes qui ne sont pas utiles suivant les besoins.