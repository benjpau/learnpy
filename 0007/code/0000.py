from PIL import Image, ImageDraw, ImageFont

img = Image.open('test.jpg')
w, h = img.size
fontsize = h / 4
position = w - fontsize
myfont = ImageFont.truetype('Arial.ttf', fontsize)
ImageDraw.Draw(img).text((position, 0), str(3), font=myfont, fill='red')
img.save('test_aft.jpg')