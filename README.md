# 📋 TaskFlow - Application de Gestion de Tâches

Une application web moderne de gestion de tâches construite avec Django 5.2 et TailwindCSS, avec une interface d'administration redessinée professionnellement.

![Python](https://img.shields.io/badge/Python-3.10-blue.svg)
![Django](https://img.shields.io/badge/Django-5.2.9-green.svg)
![TailwindCSS](https://img.shields.io/badge/TailwindCSS-3.x-06B6D4.svg)
![License](https://img.shields.io/badge/License-MIT-yellow.svg)

---

## ✨ Fonctionnalités

### Interface Utilisateur
- 🎨 **Design Moderne** : Interface utilisateur avec TailwindCSS, gradients et animations fluides
- 🌓 **Thème Élégant** : Palette de couleurs purple/blue cohérente
- 📱 **Responsive** : Compatible mobile, tablette et desktop
- ✨ **Glassmorphism** : Effets visuels modernes avec backdrop-filter
- 🎭 **Animations** : Transitions fluides et micro-animations

### Fonctionnalités CRUD
- ✅ **Créer** des tâches avec titre et description
- 📝 **Lire** et visualiser toutes les tâches
- ✏️ **Modifier** les tâches existantes
- 🗑️ **Supprimer** les tâches avec confirmation
- 🔍 **Rechercher** dans les tâches par titre ou description
- 🏷️ **Statut** : Marquer comme "Terminé" ou "En cours"

### Interface Admin Professionnelle
- 🎯 **Django Unfold** : Interface admin moderne et production-ready
- 🎨 **Badges Personnalisés** : Status colorés avec gradients
- ⚡ **Actions Batch** : Marquer terminé/en cours, dupliquer des tâches
- 📊 **Dashboard** : Sidebar moderne avec navigation hiérarchique
- 🔐 **Authentification** : Login redesigné avec glassmorphism
- 📑 **Tabs** : Filtrage rapide (Toutes | Terminées | En cours)

---

## 🚀 Installation

### Prérequis

- Python 3.10+
- pip (gestionnaire de paquets Python)
- Git

### Étapes d'installation

1. **Cloner le repository**
```bash
git clone <votre-repo-url>
cd mydjango
```

2. **Créer un environnement virtuel**
```bash
python -m venv venv
source venv/bin/activate  # Sur Windows: venv\Scripts\activate
```

3. **Installer les dépendances**
```bash
pip install -r requirements.txt
```

4. **Effectuer les migrations**
```bash
python manage.py migrate
```

5. **Créer un superutilisateur**
```bash
python manage.py createsuperuser
```

6. **Collecter les fichiers statiques**
```bash
python manage.py collectstatic --no-input
```

7. **Lancer le serveur de développement**
```bash
python manage.py runserver
```

8. **Accéder à l'application**
- Interface utilisateur : `http://127.0.0.1:8000/`
- Interface admin : `http://127.0.0.1:8000/admin/`

---

## 📁 Structure du Projet

```
mydjango/
├── config/                 # Configuration Django
│   ├── settings.py        # Settings avec configuration UNFOLD
│   ├── urls.py            # Routes principales
│   └── wsgi.py
├── tasks/                  # Application de gestion de tâches
│   ├── admin.py           # Configuration admin avec Unfold
│   ├── forms.py           # Formulaires Django
│   ├── models.py          # Modèle Task
│   ├── urls.py            # Routes de l'app tasks
│   ├── views.py           # Vues CRUD
│   └── templates/
│       └── tasks/
│           ├── base.html           # Template de base avec TailwindCSS
│           ├── task_list.html      # Liste des tâches
│           ├── task_detail.html    # Détail d'une tâche
│           ├── task_form.html      # Formulaire de création/édition
│           └── task_confirm_delete.html  # Confirmation de suppression
├── staticfiles/           # Fichiers statiques collectés
├── db.sqlite3            # Base de données SQLite
├── manage.py
├── requirements.txt
└── README.md
```

---

## 🛠️ Stack Technique

### Backend
- **Django 5.2.9** - Framework web Python
- **Python 3.10** - Langage de programmation
- **SQLite** - Base de données (développement)

### Frontend
- **TailwindCSS 3.x** - Framework CSS utility-first
- **HTML5** - Structure
- **JavaScript** - Interactivité (minimal)
- **Google Fonts (Inter)** - Typographie moderne

### Admin UI
- **Django Unfold 0.75.0** - Interface admin moderne
- **Tailwind CSS** - Styling de l'admin

---

## 📝 Utilisation

### Interface Utilisateur

#### Créer une tâche
1. Cliquez sur le bouton **"+ Nouvelle tâche"** dans la navigation
2. Remplissez le formulaire (titre, description, statut)
3. Cliquez sur **"Créer la tâche"**

#### Modifier une tâche
1. Dans la liste des tâches, cliquez sur **"Modifier"**
2. Modifiez les champs souhaités
3. Cliquez sur **"Enregistrer les modifications"**

#### Rechercher
1. Utilisez la barre de recherche en haut de la liste
2. Tapez votre mot-clé (cherche dans titre et description)
3. Cliquez sur **"Rechercher"**

#### Supprimer une tâche
1. Cliquez sur le bouton **"Supprimer"** (icône poubelle)
2. Confirmez la suppression dans la page de confirmation

### Interface Admin

#### Actions Batch
1. Sélectionnez plusieurs tâches (cochez les cases)
2. Choisissez une action dans le menu déroulant :
   - ✅ Marquer comme terminé
   - ⏳ Marquer comme en cours
   - 📋 Dupliquer les tâches
3. Cliquez sur **"Exécuter"**

#### Filtres Rapides (Tabs)
Utilisez les tabs en haut de la liste :
- **Toutes les tâches** : Vue complète
- **Tâches terminées** : Seulement les tâches terminées
- **En cours** : Seulement les tâches en cours

---

## 🎨 Personnalisation

### Couleurs du Thème

Les couleurs principales sont définies dans `config/settings.py` sous la section `UNFOLD["COLORS"]` :

```python
"primary": {
    "500": "168 85 247",  # Purple principal
    # Modifiez pour changer le thème
}
```

### Logo Personnalisé

1. Placez votre logo dans `tasks/static/logo.svg`
2. Dans `settings.py`, décommentez :
```python
"SITE_ICON": "static/logo.svg",
```
3. Relancez `python manage.py collectstatic`

### Titre de l'Admin

Dans `config/settings.py` :
```python
UNFOLD = {
    "SITE_TITLE": "Votre Titre",
    "SITE_HEADER": "Votre Header",
}
```

---

## 🔧 Configuration

### Variables d'Environnement (Production)

Pour la production, créez un fichier `.env` :

```env
SECRET_KEY=your-secret-key-here
DEBUG=False
ALLOWED_HOSTS=yourdomain.com,www.yourdomain.com
DATABASE_URL=postgresql://user:password@localhost/dbname
```

### Base de Données

Par défaut, SQLite est utilisé. Pour PostgreSQL :

1. Installez `psycopg2-binary` : `pip install psycopg2-binary`
2. Modifiez `DATABASES` dans `settings.py`

---

## 📸 Captures d'écran

### Interface Utilisateur
- **Liste des tâches** : Cards modernes avec badges colorés
- **Formulaire** : Inputs stylisés avec toggle switch
- **Détails** : Layout élégant avec métadonnées

### Interface Admin
- **Login** : Design moderne avec glassmorphism
- **Dashboard** : Sidebar hiérarchique avec icônes
- **Liste des tâches** : Tableau moderne avec filtres
- **Formulaire** : Fieldsets organisés et élégants

---

## 🧪 Tests

Pour tester l'application :

```bash
# Vérifier la configuration Django
python manage.py check

# Lancer les tests (à créer)
python manage.py test tasks
```

---

## 📦 Déploiement

### Checklist de déploiement

- [ ] Définir `DEBUG = False`
- [ ] Configurer `ALLOWED_HOSTS`
- [ ] Utiliser PostgreSQL au lieu de SQLite
- [ ] Configurer `SECRET_KEY` via variable d'environnement
- [ ] Collecter les fichiers statiques : `python manage.py collectstatic`
- [ ] Configurer un serveur WSGI (Gunicorn)
- [ ] Utiliser Nginx comme reverse proxy
- [ ] Configurer HTTPS

### Exemple avec Gunicorn

```bash
pip install gunicorn
gunicorn config.wsgi:application --bind 0.0.0.0:8000
```

---

## 🤝 Contribution

Les contributions sont les bienvenues ! Pour contribuer :

1. Fork le projet
2. Créez une branche pour votre fonctionnalité (`git checkout -b feature/AmazingFeature`)
3. Committez vos changements (`git commit -m 'Add some AmazingFeature'`)
4. Push vers la branche (`git push origin feature/AmazingFeature`)
5. Ouvrez une Pull Request

---

## 📄 Licence

Ce projet est sous licence MIT. Voir le fichier `LICENSE` pour plus de détails.

---

## 👨‍💻 Auteur

**Votre Nom**
- GitHub: [@votre-username](https://github.com/votre-username)
- Email: votre.email@example.com

---

## 🙏 Remerciements

- [Django](https://www.djangoproject.com/) - Framework web
- [TailwindCSS](https://tailwindcss.com/) - Framework CSS
- [Django Unfold](https://github.com/unfoldadmin/django-unfold) - Interface admin moderne
- [Google Fonts](https://fonts.google.com/) - Typographie Inter

---

## 📚 Documentation Supplémentaire

- [Documentation Django](https://docs.djangoproject.com/)
- [Documentation TailwindCSS](https://tailwindcss.com/docs)
- [Documentation Django Unfold](https://unfoldadmin.com/)

---

## 🔮 Roadmap

- [ ] Tests unitaires et d'intégration
- [ ] API REST avec Django REST Framework
- [ ] Authentification JWT
- [ ] Système de notifications
- [ ] Export CSV/PDF
- [ ] Dark mode toggle
- [ ] Internationalisation (i18n)
- [ ] Webhooks
- [ ] Dashboard avec statistiques

---

**Made with ❤️ using Django & TailwindCSS**
