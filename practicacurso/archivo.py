from PIL import Image


imagen = Image.open("IMG_20190620_212744.png")
imagen.show()
print imagen.size


miniatura = (20, 20)
imagen.thumbnail(miniatura)
imagen.show()
print imagen.size
imagen.save("miniatura.png")
