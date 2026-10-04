# Generic CRUD

Application Django de gestion de personnes.

## 1. Cloner le dépôt

```powershell
git clone https://github.com/dupontdenis/Django-etape-1.git
cd Django-etape-1
```

## 2. Créer et activer l’environnement virtuel

```powershell
python -m venv .venv
.\.venv\Scripts\activate
```

## 3. Installer les dépendances

```powershell
pip install -r requirements.txt
```

## 4. Préparer la base de données

Si le fichier `db.sqlite3` n’est pas présent, exécuter :

```powershell
python manage.py migrate
```

## 5. (Optionnel) Créer un superutilisateur

```powershell
python manage.py createsuperuser
```

## 6. Lancer le serveur

```powershell
python manage.py runserver
```

### Accès

- **Liste :** <http://127.0.0.1:8000/>
- **Création :** <http://127.0.0.1:8000/create/>
