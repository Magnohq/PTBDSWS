from flask import Flask, redirect, request, make_response, abort

app = Flask(__name__)

@app.route('/user/<nome>')
def saudar(nome):
    return f'<h1>Hello, {nome}!</h1>'

@app.route('/redirecionamento')
def redirecionar():
    return redirect('https://ptb.ifsp.edu.br/')

@app.route('/contextorequisicao')
def contexto():
    agente = request.headers.get('User-agent')
    return f'<p>Your browser is {agente}</p>'

@app.route('/')
def inicio():
    return '<h1>Hello world!</h1> <h2>Disciplina PTBDSWS</h2>'

@app.route('/objetoresposta')
def criar_cookie():
    resposta = make_response("<h1>This document carries a cookie!</h1>")
    resposta.set_cookie('answer', '42')
    return resposta

@app.route('/abortar')
def dar_erro():
    abort(404)

@app.route('/codigostatusdiferente')
def status_custom():
    return ("Forbidden", 403)