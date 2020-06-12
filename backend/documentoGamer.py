from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw 


def CreateDocument(dados):
    img = Image.open("Carteirinhagamer.png")
    draw = ImageDraw.Draw(img)
    font = ImageFont.truetype("Alef-Regular.ttf", 14)
    color = (0,0,0)
    
    draw.text((195, 90),dados[0],color,font=font) # username
    draw.text((195, 135),dados[1],color,font=font) # dados adicionais
    draw.text((393, 90),dados[2],color,font=font) # psn
    draw.text((393, 133),dados[3],color,font=font) # nintendo
    draw.text((393, 176),dados[4],color,font=font) # xbox
    draw.text((393, 218),dados[5],color,font=font) # steam
    
    photo = Image.open(dados[6])
    basewidth = 150
    wpercent = (basewidth/float(photo.size[0]))
    hsize = int((float(photo.size[1])*float(wpercent)))
    photo = photo.resize((basewidth,hsize), Image.ANTIALIAS)
    img.paste(photo, (30,70))
    img.save('sample-out4.png')
    
    