import requests

def buscar_cotacao(moeda_base, moeda_destino):
    url_base = f'https://economia.awesomeapi.com.br/json/last/{moeda_base}-{moeda_destino}'
    resposta = requests.get(url_base)
    dados = resposta.json()
    cambio = moeda_base + moeda_destino
    cotacao = float(dados[cambio]['bid'])
    return cotacao

moeda_base = 'USD'
moeda_destino = 'BRL'
cotacao = buscar_cotacao(moeda_base, moeda_destino)

def converter(valor, cotacao):
    return valor*cotacao 

valor1 = 50
resultado = converter(valor1, cotacao)

historico = []

def registrar_historico(moeda_base, moeda_destino, valor, resultado):
    registro = {
                'moeda_base': moeda_base,
                'moeda_destino': moeda_destino,
                'valor': valor,
                'resultado': resultado
                }
    historico.append(registro)
    

registrar_historico(moeda_base, moeda_destino, valor1, resultado)
for registro in historico:
    print(registro)

# registrar_historico(f'{moeda_base}-{moeda_destino}, 50, {cotacao}')