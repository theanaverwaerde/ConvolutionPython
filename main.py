from PIL import Image

im = Image.open("cat.png").convert('RGB')

px = im.load()

w, h = im.size

result = Image.new("RGB", (w, h), color='white')
resultpx = result.load()

m = [[.11, .11, .11, .11,.11],
     [.11, .11, .11, .11,.11],
     [.11, .11, .11, .11,.11],
     [.11, .11, .11, .11,.11],
     [.11, .11, .11, .11,.11]]

mlen = len(m[0])

for i in range(w):
    for j in range(h):
        somr = 0
        somg = 0
        somb = 0
        for k in range(i - int(mlen / 2)+1, i + int(mlen / 2)):
            for l in range(j - int(mlen / 2)+1, j + int(mlen / 2)):
                somr += int(px[k % w, l % h][0] * .11)  # m[k - i + int(mlen / 2)][l - j + int(mlen / 2)]
                somg += int(px[k % w, l % h][1] * .11)  # m[k - i + int(mlen / 2)][l - j + int(mlen / 2)]
                somb += int(px[k % w, l % h][2] * .11)  # m[k - i + int(mlen / 2)][l - j + int(mlen / 2)]

        resultpx[i, j] = (somr, somg, somb)

result.save("python.png")

im.show()
result.show()
