
from flask import Flask, render_template 

app = Flask(__name__, static_folder='static')

@app.route('/')
def template_pagina():
    return render_template('layout.html')

@app.route('/inicio')
def inicio_pagina():
    return render_template('index.html')

@app.route('/contacto')
def formulario_conacto():
    return render_template('contacto.html')

@app.route('/nosotros')
def pagina_nosotros():
    return render_template('nosotros.html')

@app.route('/delitoinformatico')
def delito_informatico():
    return render_template('delito-inf.html')

@app.route('/delitolaboral')
def delito_laboral():
    return render_template('delito-lab.html')

@app.route('/delitopenal')
def delito_penal():
    return render_template('delito-penal.html')

@app.route(404)
def page_not_found(error):
    return render_template('404.html'), 404
