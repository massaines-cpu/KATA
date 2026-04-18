# bibliotheque qui gère les images

from PIL import Image, ImageColor
img = Image.new('RGB', (1200, 1200), color = "#F0622B")
# img.show()

#changer couleur d'un pixel
noir = ImageColor.getcolor("#000000", "RGB")
img.putpixel((128, 128), noir)
img.show()

def pixel_image(nom, largeur, hauteur):
    pass

