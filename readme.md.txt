# Python Tkinter Animated Navbar

Une interface graphique moderne et fluide développée avec **Python 3.14.2**. Ce projet met en avant la création d'un menu latéral (sidebar) animé et rétractable sans utiliser de bibliothèques tierces complexes, en s'appuyant sur la puissance native de **Tkinter**.

[Image représentant l'interface de l'application avec son menu latéral violet]

## Fonctionnalités
* *Animation Fluide** : Menu latéral coulissant avec transition progressive[cite: 10].
* *Design Personnalisé** : Utilisation d'un dictionnaire de couleurs (`nero`, `purple`, `white`) pour une UI cohérente[cite: 10].
* *Rendu Graphique** : Utilisation d'un `Canvas` pour intégrer des images de fond et des superpositions de texte[cite: 10].
* *Gestion d'État** : Logique de commutation intelligente pour l'ouverture et la fermeture des menus[cite: 10].

## Spécifications Techniques
* *Langage** : Python 3.14.2 [cite: 10]
* *Bibliothèque GUI** : Tkinter [cite: 10]
* *Génération d'icônes** : Script utilitaire utilisant la bibliothèque Pillow[cite: 10].

##  Organisation des Fichiers
* `navbar.py` : Script principal de l'application
* `logo2.py` : Script de création de l'icône système
* `menu.png` : Icône d'ouverture de la barre de navigation.
* `close.png` : Icône de fermeture (à renommer depuis `lose.png`).
* `back_image3.png` : Image d'arrière-plan du tableau de bord.

## Installation

1. **Prérequis** :
   Assurez-vous que Python 3.14.2 est installé. Pour le script d'icône, installez Pillow :
   ```bash

   pip install Pillow
