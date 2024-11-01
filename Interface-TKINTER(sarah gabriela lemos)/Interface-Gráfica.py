import tkinter as tk
from tkinter import ttk

janela = tk.Tk()

janela.title("Cotaçaõ de Moedas")

janela.rowconfigure(0, weight=1)
janela.columnconfigure(0, weight=1)

mensagem = tk.Label(text='Sistema de busca de cotação de moedas', fg= 'white', bg= '#7E40C8', width=35 ,height=5)
# mensagem.pack()
mensagem.grid(row=0, column=0, columnspan=2, sticky= "NSEW")

mensagem2 = tk.Label(text='selecione a moeda desejada')
# mensagem2.pack()
mensagem2.grid(row=1, column=0)

mensagem3 = tk.Label(text='caso voce queira pegar mais de uma cotação ao mesmo tempo, favor encrever abaixo.')
mensagem3.grid(row=4, column=0, columnspan=2)
caixa_texto= tk.Text(width=10, height=5)
caixa_texto.grid(row=5, column=0, sticky='nswe')


dicionario_cotacoes= {
    'Dólar': 5.47,
    'Euro': 6.68,
    'Bitcoin': 20000
}

moedas= list(dicionario_cotacoes.keys())
moeda= ttk.Combobox(janela, values=moedas)
moeda.grid(row=1, column=1)
def buscarCotacao():
    #print(moeda.get())
    moeda_preenchida = moeda.get()
    cotacao_moeda = dicionario_cotacoes.get(moeda_preenchida)
    mensagem_cotacao= tk.Label(text='Cotação não encontrada')
    mensagem_cotacao.grid(row=3, column=0)
    if cotacao_moeda:
        mensagem_cotacao['text'] = f'Cotação do {moeda_preenchida} é de {cotacao_moeda} reais.'

def buscar_cotacoes():
    texto = caixa_texto.get("1.0", tk.END)
    lista_moedas = texto.split('\n')
    mensagem_cotacoes = []
    for item in lista_moedas:
        cotacao = dicionario_cotacoes.get(item)
        if cotacao:
            mensagem_cotacoes.append(f'{item}:{cotacao}')
    mensagem4 = tk.Label(text='\n'.join(mensagem_cotacoes))
    mensagem4.grid(row=6, column=1)


botao_multiplicacoes = tk.Button(text= 'Buscar Cotações', command=buscar_cotacoes)
botao_multiplicacoes.grid(row=5, column=1)

botao = tk.Button(text="Buscar Cotação", command=buscarCotacao)
botao.grid(row=2, column=1)

# moeda = tk.Entry()
# moeda.grid(row=1, column=1)
# moeda.pack()
janela.mainloop()