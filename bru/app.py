import cotacao 
import streamlit as st

st.title('Conversor de Moedas')

moeda_base = st.text_input('Moeda base:', 'USD').upper()
moeda_destino = st.text_input('Moeda destino:', 'BRL').upper()
valor = st.number_input('valor:')
botao = st.button('Converter')

if botao:
    cotacao1 = cotacao.buscar_cotacao(moeda_base, moeda_destino)
    resultado = cotacao.converter(valor, cotacao1)
    cotacao.registrar_historico('USD-BRL', valor, resultado)
    st.success(f'{valor}{moeda_base} valem {resultado:.2f} {moeda_destino}')

    st.markdown('---')
    st.subheader('Historico de Conversao')
    st.table(cotacao.historico)