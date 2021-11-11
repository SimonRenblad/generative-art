
from PIL import Image, ImageDraw
import math

images = []

width = 400
center = width // 2
color_1 = (0, 0, 0)
color_2 = (255, 255, 255)
step = 0.001
a = 7.0
b = 1.0
c = 7.0
d = 1.0
k = a/b
j = c/d
sc = 100


img = Image.new('RGB', (width, width), color_1)
draw = ImageDraw.Draw(img)

for t in range(0, int(2*math.pi * 1000)):
    t = t / 1000.0
    x = math.cos(a*t) - math.pow(math.cos(b*t), j)
    y = math.sin(c*t) - math.pow(math.sin(d*t), k)
    draw.point((center + int(sc*x),center + int(sc*y)), color_2)

img.save('test2.png')

# for i in range(0, max_radius, step):
#     im = Image.new('RGB', (width, width), color_1)
#     draw = ImageDraw.Draw(im)
#     draw.ellipse((center - i, center - i, center + i, center + i), fill=color_2)
#     images.append(im)

# for i in range(0, max_radius, step):
#     im = Image.new('RGB', (width, width), color_2)
#     draw = ImageDraw.Draw(im)
#     draw.ellipse((center - i, center - i, center + i, center + i), fill=color_1)
#    images.append(im)

# images[0].save('./pillow_imagedraw.gif',
#                save_all=True, append_images=images[1:], optimize=False, duration=40, loop=0)