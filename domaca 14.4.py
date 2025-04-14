from PIL import Image

obr = Image.new("RGB", (50, 50), color=(255, 255, 255))
sirka, vyska = obr.size
print(sirka, vyska)

pixels = obr.load()
for y in range(vyska):
    for x in range(sirka):
        vzdialenosť = min(x, y, sirka - 1 - x, vyska - 1 - y)
        if vzdialenosť % 2 == 0:
            pixels[x, y] = (0, 0, 0)
        else:
            pixels[x, y] = (255, 255, 255)

obr.show()
obr.save("opticky_stvorec.png")
