from flask import Flask, jsonify, request
from flask_cors import CORS
import json
from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw 

DEBUG = True

app = Flask(__name__)
app.config.from_object(__name__)

CORS(app, resources={r'/*': {'origins': '*'}})


@app.route('/create', methods=['GET', 'POST'])
def create():
    response_object = {'status': 'success'}
    if request.method == 'POST':
        CreateDocument(request.get_json())
          
        response_object['message'] = 'Jogo adicionado'
    else:
        response_object['jogos'] = ''
    return jsonify(response_object)

def CreateDocument(dados):
    img = Image.open("Carteirinhagamer.png")
    draw = ImageDraw.Draw(img)
    font = ImageFont.truetype("Alef-Regular.ttf", 14)
    color = (0,0,0)
    
    draw.text((195, 90),dados.get('username'),color,font=font) # username
    draw.text((195, 135),dados.get('otherdatas'),color,font=font) # dados adicionais
    draw.text((393, 90),dados.get('psn'),color,font=font) # psn
    draw.text((393, 133),dados.get('nintendo'),color,font=font) # nintendo
    draw.text((393, 176),dados.get('xbox'),color,font=font) # xbox
    draw.text((393, 218),dados.get('steam'),color,font=font) # steam
    
    photo = Image.open(dados.get('file'))
    basewidth = 150
    wpercent = (basewidth/float(photo.size[0]))
    hsize = int((float(photo.size[1])*float(wpercent)))
    photo = photo.resize((basewidth,hsize), Image.ANTIALIAS)
    img.paste(photo, (30,70))
    img.save('Carteirinhagamer2020.png')
    


if __name__ == '__main__':
    app.run()
