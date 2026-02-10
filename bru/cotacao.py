import requests

def buscar_cotacao(moeda_base, moeda_destino):
    url_base = 'https://economia.awesomeapi.com.br/json/last/USD-BRL'
    resposta = requests.get(url_base)
    dados = resposta.json()
    cambio = moeda_base + moeda_destino
    cotacao = float(dados[cambio]['bid'])
    return cotacao


cotacao = buscar_cotacao('USD', 'BRL')

def converter(valor, cotacao):
    return valor*cotacao 

valor1 = 50
resultado = converter(valor1, cotacao)

historico = []

def registrar_historico(moeda, valor, resultado):
    registro = {
                'moeda': moeda,
                'valor': valor,
                'resultado': resultado
                }
    historico.append(registro)
    

registrar_historico('USD-BRL', valor1, resultado)
for registro in historico:
    print(registro)

# registrar_historico(f'{moeda_base}-{moeda_destino}, 50, {cotacao}')