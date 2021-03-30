from PIL import Image
from math import *
import array

im = Image.open("cat.png").convert('RGB')

px = im.load()

w, h = im.size

result = Image.new("RGB", (w, h), color='white')
resultpx = result.load()

while (True):
    try:

        print("Choisis ta matrix : ")
        print("1. Brighten")
        print("2. Darken")
        print("3. Edge detector Vertical")
        print("4. Edge detector Horizontal")
        print("5. Blur ?x?")

        id = int(input())

    except ValueError:
        print("Nombre non valide")
        continue

    if id == 1:
        m = [[1.5]]
    elif id == 2:
        m = [[.5]]
    elif id == 3:
        m = [[-1, 0, 1],
             [-1, 0, 1],
             [-1, 0, 1]]
    elif id == 4:
        m = [[1, 1, 1],
             [0, 0, 0],
             [-1, -1, -1]]
    elif id == 5:
        print("Entre un nombre impaire pour la taille souhaitez")

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

        m = [[1/pow(size, 2)]*size]*size



    else:
        print("Nombre non valide")
        continue

    break

mlen = len(m[0])

for i in range(w):
    for j in range(h):
        som = [0, 0, 0]
        for k in range(i - floor(mlen / 2), i + ceil(mlen / 2)):
            for l in range(j - floor(mlen / 2), j + ceil(mlen / 2)):
                actualPx = px[k % w, l % h]
                actualM = m[k - i + floor(mlen / 2)][l - j + floor(mlen / 2)]

                for c in range(3):
                    som[c] = som[c] + round(actualPx[c] * actualM)

        resultpx[i, j] = (som[0], som[1], som[2])

result.save("python.png")

im.show()
result.show()
