from PIL import Image
from math import *
from masque import *

im = Image.open("cat.png").convert('RGB')

px = im.load()

w, h = im.size

result = Image.new("RGB", (w, h), color='white')
resultpx = result.load()

while (True):
    try:

        print("Choisis ton masque : ")
        print("1. Brighten")
        print("2. Darken")
        print("3. Edge detector Vertical")
        print("4. Edge detector Horizontal")
        print("5. Blur")

        id = int(input())

    except ValueError:
        print("Nombre non valide")
        continue

    if id == 1:
        m = Brighten()
    elif id == 2:
        m = Darken()
    elif id >= 3 and id <= 5:
        print("Entre un nombre impaire pour la taille souhaiter")

        try:
            size = int(input())
        except ValueError:
            print("Nombre non valide")
            continue

        if size < 3:
            print("La taille doit etre au moins de 3")
            continue

        if size % 2 == 0:
            print("Il faut un nombre impair")
            continue
            
        if id == 3:
            m = EdgeVertical(size)
        elif id == 4:
            m = EdgeHorizontal(size)
        elif id == 5:
            m = Blur(size)

    else:
        print("Nombre non valide")
        continue

    break

mlen = m.GetTaille()

for i in range(w):
    for j in range(h):
        som = [0, 0, 0]
        for k in range(i - floor(mlen / 2), i + ceil(mlen / 2)):
            for l in range(j - floor(mlen / 2), j + ceil(mlen / 2)):
                actualPx = px[max(min(k, w-1), 0), max(min(l, h-1), 0)]
                actualM = m.GetValeur(k - i + floor(mlen / 2), l - j + floor(mlen / 2))

                for c in range(3):
                    som[c] = som[c] + round(actualPx[c] * actualM)

        resultpx[i, j] = (som[0], som[1], som[2])

result.save("python.png")

im.show()
result.show()

print()
print("Merci d'avoir fait confiance à Théo pour votre image de chat")
