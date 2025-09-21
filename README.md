#  Système de Gestion de Pointage en Entreprise

## Description
Ce projet est une application web développée avec **Django** permettant de gérer les **présences des employés** dans une entreprise.  
Il permet aux administrateurs de :
- Ajouter et gérer les employés.
- Enregistrer les présences (heures d’entrée et de sortie).
- Suivre les absences et retards.
- Générer des rapports de présence.

##  Technologies utilisées
- **Backend** : Django (Python)
- **Base de données** : postgresql
- **Frontend** : Django Templates (HTML, CSS)
- **Éditeur** : VS Code

## Modèle de données
### Tables principales
1. **Employé**
   - nom, prénom, matricule, poste, structure, site, téléphone, email, date_engagement.
2. **Présence**
   - employe_id (FK), date_presence, heure_entree, heure_sortie, statut.
3. **Utilisateur (Admin)**
   - géré automatiquement par Django pour la connexion.
4. (Optionnel) **Historique**
   - suivi des actions faites par l’admin (ajout, modification, suppression).


##  Installation et exécution
### 1. Cloner le dépôt
```bash
git clone https://github.com/Tuunganes/Systemes_Pointages.git
cd Systemes_pointages

