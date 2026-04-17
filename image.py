# bibliotheque qui gère les images

from PIL import Image, ImageColor
# mon image
#                                largeur hauteur  couleur du fond
img = Image.new('RGB', (1200, 1200), color = "#ffffff")
# afficher l'image
img.show()

rouge = ImageColor.getcolor("#ff0000", "RGB")
#                  x   y
img.putpixel((128, 128), rouge)
img.show()