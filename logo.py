from PIL import Image, ImageDraw

#Créer une icone simple

img = Image.new('RGB', (32, 32), color='blue')
draw = ImageDraw.Draw(img)
draw.ellipse([8, 8, 24, 24], fill='white')

# Sauvegarder

img.save('logo.ico', format='ICO')
print("Image crée avec succès")

