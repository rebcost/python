import tkinter as tk
from tkinter import ttk  # para usar lista suspensa
from tkcalendar import DateEntry  # para usar o calendario
import requests
from tkinter.filedialog import askopenfilename
import pandas as pd
from datetime import datetime
import numpy as np


def data_cotacao(calendario):
    data = calendario
    ano = data[6:]
    mes = data[3:5]
    dia = data[:2]
    return ano, mes, dia


def pegar_cotacao():
    moeda = combobox_selecionarmoeda.get()

    data = data_cotacao(calendario_moeda.get())
    ano, mes, dia = data

    link = f"https://economia.awesomeapi.com.br/{moeda}-BRL/?start_date={ano}{mes}{dia}&end_date={ano}{mes}{dia}"

    requisicao_moeda = requests.get(link)
    cotacao = requisicao_moeda.json()
    valor_moeda = cotacao[0]["bid"]
    label_textocotacao["text"] = f"A cotacao da {moeda} no dia {dia}/{mes}/{ano} foi de R${valor_moeda}"


def selecionar_arquivo():
    caminho_arquivo = askopenfilename(title="Selecione o Arquivo de Moeda")
    var_caminhoArquivo.set(caminho_arquivo)

    if caminho_arquivo:
        label_arquivoSelecionado["text"] = f"Arquivo selecionado: {caminho_arquivo}"


def atualizar_cotacoes():
    try:
        # ler o dataframe
        df = pd.read_excel(var_caminhoArquivo.get())
        moedas = df.iloc[:, 0]

        # pegar a data de inicio e de fim da cotacoes
        data_inicial = data_cotacao(calendario_selecionarDataInicial.get())
        data_final = data_cotacao(calendario_selecionarDataFinal.get())

        ano_inicial, mes_inicial, dia_inicial = data_inicial
        ano_final, mes_final, dia_final = data_final

        # para cada moeda
        # pegar todas as cotacoes daquela moeda
        # criar uma nova coluna em um novo dataframe com todas as cotacoes daquela moeda
        for moeda in moedas:
            link = f"https://economia.awesomeapi.com.br/{moeda}-BRL/?" \
                   f"start_date={ano_inicial}{mes_inicial}{dia_inicial}&" \
                   f"end_date={ano_final}{mes_final}{dia_final}"
            requisicao_moeda = requests.get(link)
            cotacoes = requisicao_moeda.json()

            print(cotacoes)

            for cotacao in cotacoes:
                timestamp = int(cotacao['timestamp'])
                bid = float(cotacao['bid'])
                data = datetime.fromtimestamp(timestamp)
                data = data.strftime('%d/%m/%Y')

                if data not in df:
                    df[data] = np.nan

                df.loc[df.iloc[:, 0] == moeda, data] = bid

        # criar um novo arquivo com todas as cotaocoes
        df.to_excel("Teste.xlsx")
        label_atualizar['text'] = "Arquivo Atualizado com Sucesso"

    except:
        label_atualizar['text'] = "Selecione um arquivo Excel no formato correto"


requisicoes = requests.get("https://economia.awesomeapi.com.br/json/all")
dicionario_moedas = requisicoes.json()
lista_moedas = list(dicionario_moedas.keys())

janela = tk.Tk()
janela.title("Ferramenta de Cotação de Moedas")

label_cotacaomoeda = tk.Label(text="Cotação de 1 moeda específica", borderwidth=2, relief='solid')
label_cotacaomoeda.grid(row=0, column=0, padx=10, pady=10, sticky='nswe', columnspan=3)

label_selecionarmoeda = tk.Label(text="Selecionar Moeda", anchor='e')
label_selecionarmoeda.grid(row=1, column=0, padx=10, pady=10, sticky='nswe', columnspan=2)

combobox_selecionarmoeda = ttk.Combobox(values=lista_moedas)
combobox_selecionarmoeda.grid(row=1, column=2, padx=10, pady=10, sticky='nsew')

label_selecionardia = tk.Label(text="Selecione o dia que deseja pegar a cotação", anchor='e')
label_selecionardia.grid(row=2, column=0, padx=10, pady=10, sticky='nswe', columnspan=2)

calendario_moeda = DateEntry(year=2021, locale='pt_br')
calendario_moeda.grid(row=2, column=2, padx=10, pady=10, sticky='nsew')

label_textocotacao = tk.Label(text="")
label_textocotacao.grid(row=3, column=0, columnspan=2, padx=10, pady=10, sticky='nsew')

botao_pegarcotacao = tk.Button(text="Pegar Cotação", command=pegar_cotacao)
botao_pegarcotacao.grid(row=3, column=2, padx=10, pady=10, sticky='nsew')

# varias moedas
label_variasmoedas = tk.Label(text="Cotação de Multiplas Moedas", borderwidth=2, relief="solid")
label_variasmoedas.grid(row=4, column=0, padx=10, pady=10, sticky="nsew", columnspan=3)

label_selecionarArquivo = tk.Label(text="Selecione um arquivo em Excel com as Moedas na Coluna A:")
label_selecionarArquivo.grid(row=5, column=0, padx=10, pady=10, sticky="nsew", columnspan=2)

var_caminhoArquivo = tk.StringVar()

botao_selecionarArquivo = tk.Button(text="Selecionar Arquivo", command=selecionar_arquivo)
botao_selecionarArquivo.grid(row=5, column=2, padx=10, pady=10, sticky="nsew")

label_arquivoSelecionado = tk.Label(text="Nenhum arquivo selecionado", anchor="e")
label_arquivoSelecionado.grid(row=6, column=0, columnspan=3, padx=10, pady=10, sticky="nsew")

label_dataInicial = tk.Label(text="Data Inicial", anchor="e")
label_dataInicial.grid(row=7, column=0, padx=10, pady=10, sticky="nsew")

calendario_selecionarDataInicial = DateEntry(year=2021, locale='pt_br')
calendario_selecionarDataInicial.grid(row=7, column=1, padx=10, pady=10, sticky="nsew")

label_dataFinal = tk.Label(text="Data Final", anchor="e")
label_dataFinal.grid(row=8, column=0, padx=10, pady=10, sticky="nsew")

calendario_selecionarDataFinal = DateEntry(year=2021, locale='pt_br')
calendario_selecionarDataFinal.grid(row=8, column=1, padx=10, pady=10, sticky="nsew")

botao_atualizar = tk.Button(text="Atualizar Cotações", command=atualizar_cotacoes)
botao_atualizar.grid(row=9, column=0, padx=10, pady=10, sticky="nsew")

label_atualizar = tk.Label(text="")
label_atualizar.grid(row=9, column=2, padx=10, pady=10, sticky="nsew")

botao_fechar = tk.Button(text="Fechar", command=janela.quit)
botao_fechar.grid(row=10, column=2, padx=10, pady=10, sticky="nsew")

janela.mainloop()
