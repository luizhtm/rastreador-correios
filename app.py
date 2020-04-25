from bottle import route, view, run, request, static_file, template, redirect, url
from rastreia import rastrear
import re

@route('/static/:path#.+#', name='static')
def serve_static(path):
	return static_file(path, root='static')

@route('/')
@view('index')
def index():
	return { 'get_url': url }

@route('/rastrear', method='POST')
def rastreia():
	codigo = request.forms.get('codigo')
	codigo = codigo.strip().upper()
	redirect('/rastrear/{codigo}'.format(codigo=codigo))

@route('/rastrear/<codigo>')
@view('rastreamento')
def rastreia_codigo(codigo):
	valido = re.fullmatch(r'[A-Z]{2}[0-9]{9}[A-Z]{2}', codigo)

	resultado = []

	if valido:
		resultado = rastrear(codigo)

	return { 'get_url': url, 'codigo': codigo, 'resultado': resultado, 'valido': valido }

run(host='localhost', port=8080, debug=True, reloader=True)