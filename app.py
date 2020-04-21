from bottle import route, run, request, static_file, template, redirect
from rastreia import rastrear

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
    if len(codigo) != 13:
    	redirect('/')
    else:
    	redirect('/rastrear/{codigo}'.format(codigo=codigo))

@route('/rastrear/<codigo>')
def rastreia_codigo(codigo):
	resultado = rastrear(codigo)
	return template('rastreamento', codigo=codigo, resultado=resultado)

run(host='localhost', port=8080, debug=True, reloader=True)