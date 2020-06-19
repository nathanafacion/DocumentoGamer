    
# -*- coding: utf-8 -*-
from flask import Flask, jsonify, request
from flask_cors import CORS, cross_origin
import json
from PIL import Image
from PIL import ImageFont
from werkzeug.utils import secure_filename

UPLOAD_FOLDER = '/'
DEBUG = True

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config.from_object(__name__)

cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'


@app.route('/carteirinha', methods=['POST','GET'])
@cross_origin()
def create():
    response_object = {'status': 'success'}
    print(request)
    if request.method == 'POST':
        print(request.get_json())
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
    
    draw.text((195, 90),dados.get('username').encode("utf-8"),color,font=font) # username
    draw.text((195, 135),dados.get('otherdatas').encode("utf-8"),color,font=font) # dados adicionais
    draw.text((393, 90),dados.get('psn').encode("utf-8"),color,font=font) # psn
    draw.text((393, 133),dados.get('nintendo').encode("utf-8"),color,font=font) # nintendo
    draw.text((393, 176),dados.get('xbox').encode("utf-8"),color,font=font) # xbox
    draw.text((393, 218),dados.get('steam').encode("utf-8"),color,font=font) # steam
    
    photo = Image.open(dados.get('avatar').encode("utf-8"))
    basewidth = 150
    wpercent = (basewidth/float(photo.size[0]))
    hsize = int((float(photo.size[1])*float(wpercent)))
    photo = photo.resize((basewidth,hsize), Image.ANTIALIAS)
    img.paste(photo, (30,70))
    img.save('Carteirinhagamer2020.png')
    
def upload_file(request):
    file = request.files['avatar']
    if file and allowed_file(file.filename):
        filename = secure_filename(file.filename)
        file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
    return filename


if __name__ == '__main__':
    app.run()
