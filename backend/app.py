
# -*- coding: utf-8 -*-
from flask import Flask, jsonify, request, redirect, url_for
from flask_cors import CORS, cross_origin
import json
from PIL import Image, ImageDraw
from PIL import ImageFont
from werkzeug.utils import secure_filename
from flask import current_app
from flask import send_from_directory
import os
import uuid

UPLOAD_FOLDER = '/home/nathana/DocumentoGamer/backend/'
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
        response_object['path'] = CreateDocument(request)
    else:
        response_object['path'] = 'Esta caindo aqui'
    return jsonify(response_object)

def CreateDocument(dados):
    img = Image.open("Carteirinhagamer.png")
    draw = ImageDraw.Draw(img)
    font = ImageFont.truetype("Alef-Regular.ttf", 14)
    color = (0,0,0)
    print("Create document",dados)
    draw.text((195, 90),dados.form.get('username').encode("utf-8"),color,font=font) # username
    draw.text((195, 135),dados.form.get('otherdatas').encode("utf-8"),color,font=font) # dados adicionais
    draw.text((393, 90),dados.form.get('psn').encode("utf-8"),color,font=font) # psn
    draw.text((393, 133),dados.form.get('nintendo').encode("utf-8"),color,font=font) # nintendo
    draw.text((393, 176),dados.form.get('xbox').encode("utf-8"),color,font=font) # xbox
    draw.text((393, 218),dados.form.get('steam').encode("utf-8"),color,font=font) # steam

    path = upload_file(dados)
    print(path)
    photo = Image.open(path)
    basewidth = 150
    wpercent = (basewidth/float(photo.size[0]))
    hsize = int((float(photo.size[1])*float(wpercent)))
    photo = photo.resize((basewidth,hsize), Image.ANTIALIAS)
    new_photo = 'Carteirinhagamer'+str(uuid.uuid4().hex)+".png"
    img.paste(photo, (30,70))
    img.save(new_photo)
    return new_photo

def upload_file(request):
    if not request:
        return "icon.png"
    else:
        file = request.files['avatar']
        filename = secure_filename(file.name)
        file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        return filename


@app.route('/uploads/<path:filename>', methods=['GET', 'POST'])
def download_file(filename):
    print("download",filename)
    uploads = os.path.join(current_app.root_path, app.config['UPLOAD_FOLDER'])
    print(uploads)
    return send_from_directory(directory=uploads, filename=filename)

if __name__ == '__main__':
    app.run()
