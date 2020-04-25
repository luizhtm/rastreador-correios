import requests
from bs4 import BeautifulSoup

def rastrear(codigo):
	data = {
		'acao': 'track',
		'objetos': codigo,
		'btnPesq': 'Buscar'
	}

	url = "https://www2.correios.com.br/sistemas/rastreamento/ctrl/ctrlRastreamento.cfm"
	response = requests.post(url, data=data)
	doc = BeautifulSoup(response.text, 'html.parser')

	datas_eventos = doc.find_all('td', class_="sroDtEvent")
	eventos = doc.find_all('td', class_="sroLbEvent")

	if len(eventos) == 0:
		return []

	todos_eventos = []
	for i in range(len(eventos)):
		data_lista = datas_eventos[i].text.strip().split('\n')
		data = data_lista[0].strip()
		hora = data_lista[1].strip()
		cidade = data_lista[2].strip()
		cidade = cidade.replace('\xa0', ' ')

		eventos_lista = eventos[i].text.strip().split('\n')
		eventos_lista = [evento for evento in eventos_lista if evento.strip() != '']

		evento = eventos_lista[0].strip()

		dados = {
			'data': data,
			'hora': hora,
			'local': cidade,
			'evento': evento
		}

		if evento == "Objeto encaminhado":
			linha_destino = eventos_lista[4].strip()
			cidade_destino = linha_destino[2:].strip()
			dados['destino'] = cidade_destino

		todos_eventos.append(dados)

	return todos_eventos
