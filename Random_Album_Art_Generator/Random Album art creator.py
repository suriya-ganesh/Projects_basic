# Inspiration: [Fake Album Covers](https://fakealbumcovers.com/)
from IPython.display import Image as IPythonImage
from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw

import requests
from xml.etree import ElementTree as ET

def display_cover(top,bottom ):
    
    name='album_art_raw.png'
    album_art_raw = requests.get('https://picsum.photos/500/500/?random')
 
    with open(name,'wb') as album_art_raw_file:
       album_art_raw_file.write(album_art_raw.content)

    img = Image.open("album_art_raw.png")
    draw = ImageDraw.Draw(img)

    band_name_font = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf", 25) #25pt font
    album_name_font = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf", 20) # 20pt font

    band_x, band_y = 50, 50
    album_x, album_y = 50, 400

    outline_color ="black"

    draw.text((band_x-1, band_y-1), top, font=band_name_font, fill=outline_color)
    draw.text((band_x+1, band_y-1), top, font=band_name_font, fill=outline_color)
    draw.text((band_x-1, band_y+1), top, font=band_name_font, fill=outline_color)
    draw.text((band_x+1, band_y+1), top, font=band_name_font, fill=outline_color)

    draw.text((album_x-1, album_y-1), bottom , font=album_name_font, fill=outline_color)
    draw.text((album_x+1, album_y-1), bottom , font=album_name_font, fill=outline_color)
    draw.text((album_x-1, album_y+1), bottom , font=album_name_font, fill=outline_color)
    draw.text((album_x+1, album_y+1), bottom , font=album_name_font, fill=outline_color)

    draw.text((band_x,band_y),top,(255,255,255),font=band_name_font)
    draw.text((album_x, album_y),bottom,(255,255,255),font=album_name_font)

    return img


wikipedia='https://en.wikipedia.org/wiki/Special:Random'
page = requests.get(wikipedia).text.strip()
file= ET.fromstring(page).find('head/title')
band_title = file.text.replace(' - Wikipedia','')

wikipedia='https://en.wikipedia.org/wiki/Special:Random'
page = requests.get(wikipedia).text.strip()p
file= ET.fromstring(page).find('head/title')
album_title = file.text.replace(' - Wikipedia','')
print(album_title)

print("Your band: ", band_title)
print("Your album: ", album_title)

img = display_cover(band_title,album_title)


img.save('sample-out.png')

IPythonImage(filename='sample-out.png')