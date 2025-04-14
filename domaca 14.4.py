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




#jpg na gif
from PIL import Image

obr = Image.open("obrazok.jpg")
sirka, vyska = obr.size

obr_novy = Image.new("P", (sirka, vyska)) #'P'=paletový – vhodný pre GIF

pixels_old = obr.load()
pixels_new = obr_novy.load()

for y in range(vyska):
    for x in range(sirka):
        priemer = (pixels_old[x, y][0] + pixels_old[x, y][1] + pixels_old[x, y][2]) // 3 # priemer RGB
        pixels_new[x, y] = priemer

obr_novy.save("novy_obrazok.gif")
obr_novy.show()
