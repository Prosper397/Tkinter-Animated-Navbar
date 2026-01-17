from PIL import Image

# Création d'une image simple de 256*256 pixels
img = Image.new('RGB', (256, 256), color=(73, 109, 137))

#Sauvegarder au format .ico
img.save('logo2.ico')
print("Le fichier logo2.ico a été créé !")