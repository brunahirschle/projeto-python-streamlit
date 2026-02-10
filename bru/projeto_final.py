import cotacao
import streamlit as st
import requests 
import pandas as pd

tab1, tab2, tab3 = st.tabs(['cotação', 'gráficos', 'conversor'])





with tab1:
    cotacao_dolar = cotacao.buscar_cotacao('USD', 'BRL')
    cotacao_euro = cotacao.buscar_cotacao('EUR', 'BRL')
    cotacao_bit = cotacao.buscar_cotacao('BTC', 'BRL')

    col1, col2, col3 = st.columns(3)

    with col1:
        st.metric(label='Dólar(USD)', value= f'R$ {cotacao_dolar:.2f}')
    with col2:
        st.metric(label='Euro(EUR)', value= f'R$ {cotacao_euro:.2f}')
    with col3:
        st.metric(label='Bitcoin(BTC)', value= f'R$ {cotacao_bit:.2f}')





with tab2:
    url_base = f'https://economia.awesomeapi.com.br/json/daily/BTC-BRL/10'
    dados = requests.get(url_base).json()
    df = pd.DataFrame(dados)
    df['timestamp'] = pd.to_datetime(df['timestamp'], unit='s')
    df['bid'] = df['bid'].astype(float)
    df = df.set_index('create_date')

    st.line_chart(df['bid'])



with tab3:
    st.title('Conversor de Moedas')

    moeda_base = st.text_input('Moeda base:', 'USD').upper()
    moeda_destino = st.text_input('Moeda destino:', 'BRL').upper()
    valor = st.number_input('valor:')
    botao = st.button('Converter')


    if botao:
        cotacao1 = cotacao.buscar_cotacao(moeda_base, moeda_destino)
        resultado = cotacao.converter(valor, cotacao1)
        cotacao.registrar_historico(moeda_base, moeda_destino, valor, resultado)
        st.success(f'{valor}{moeda_base} valem {resultado:.2f} {moeda_destino}')

        st.markdown('---')
        st.subheader('Historico de Conversao')
        st.table(cotacao.historico)

st.session_state['dados_historico'] = cotacao.historico