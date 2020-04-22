from bottle import route, run, request, static_file, template, redirect
from rastreia import rastrear
import re

@route('*/js/<filename>')
def js(filename):
	return static_file(filename, root='./js/')

@route('*/css/<filename>')
def css(filename):
	return static_file(filename, root='./css/')

@route('/')
def index():
	return static_file('index.html', 'views/')

@route('/rastrear', method='POST')
def rastreia():
	codigo = request.forms.get('codigo')
	codigo = codigo.strip().upper()
	redirect('/rastrear/{codigo}'.format(codigo=codigo))

@route('/rastrear/<codigo>')
def rastreia_codigo(codigo):
	valido = re.fullmatch(r'[A-Z]{2}[0-9]{9}[A-Z]{2}', codigo)

	resultado = []
	
	if valido:
		resultado = rastrear(codigo)

	return template('rastreamento', codigo=codigo, resultado=resultado, valido=valido)

run(host='localhost', port=8080, debug=True, reloader=True)