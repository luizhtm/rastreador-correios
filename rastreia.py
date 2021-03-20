import requests
import sys
import re
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

		if evento == "Objeto em trânsito - por favor aguarde":
			linha_destino = eventos_lista[4].strip()
			cidade_destino = linha_destino[2:].strip()
			dados['destino'] = cidade_destino

		todos_eventos.append(dados)

	return todos_eventos

def exibe_status(eventos):
	if not eventos:
		print("Encomenda ainda não postada ou código está incorreto.")
	else:
		mensagem = '\n'
		for evento in eventos:
			mensagem += 'Data: {data} - Hora: {hora}\n'.format(data=evento['data'], hora=evento['hora'])
			try:
				mensagem += 'Objeto em {local} sendo transferido para {destino}\n'.format(local=evento['local'], destino=evento['destino'])
			except:
				mensagem += '{local} - {evento}\n'.format(local=evento['local'], evento=evento['evento'])
			mensagem += '\n'

		print(mensagem)

def main():
	# Checa se o codigo está na chamada do script
	if len(sys.argv) > 1:
		print('blah')
		print(sys.argv[1])
		codigo = sys.argv[1]
	else:
		print('merda')
		codigo = input('Digite o código de rastreamento: ')

	codigo = codigo.upper()
	valido = re.fullmatch(r'[A-Z]{2}[0-9]{9}[A-Z]{2}', codigo)

	if valido:
		todos_eventos = rastrear(codigo)
		exibe_status(todos_eventos)
	else:
		print("Formato do código inválido.")

if __name__ == "__main__":
    main()