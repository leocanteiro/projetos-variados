import tkinter as tk
from tkinter import simpledialog, messagebox
import json
import os
#----------------------------------------------------------------------------------#
# Esse código é apenas um esboço de um projeto que estou desenvolvendo 
# para eu utilizar na empresa onde eu trabalho, a ideia é criar um software
# de gerenciamento de estoque onde eu consiga dar entrada, alterar ou remover
# um produto do estoque.
# Futuramente penso em fazer algo bem mais implementado com uma interface gráfica
# mais desenvolvida e com mais recuros.
#----------------------------------------------------------------------------------#


# func para adicionar produto ao estoque
def adicionar_produto():
    chave = simpledialog.askstring("Adicionar Produto", "Digite o nome do produto:")
    if chave:
        valor = simpledialog.askinteger("Adicionar Produto", "Digite a quantidade do produto:")
        if valor is not None:
            meu_dicionario[chave] = valor
            atualizar_lista()
            salvar_dados()
            
# func para remover um produto já existente
def remover_produto():
    chave = simpledialog.askstring("Remover Produto", "Digite o nome do produto a ser removido:")
    if chave in meu_dicionario:
        del meu_dicionario[chave]
        atualizar_lista()
        salvar_dados()
    else:
        messagebox.showerror("Erro", "Produto não encontrado!")

# func para alterar a quantidade de um produto existente
def alterar_quantidade():
    chave = simpledialog.askstring("Alterar Quantidade", "Digite o nome do produto:")
    if chave in meu_dicionario:
        valor = simpledialog.askinteger("Alterar Quantidade", "Digite a nova quantidade do produto:")
        if valor is not None:
            meu_dicionario[chave] = valor
            atualizar_lista()
            salvar_dados()
    else:
        messagebox.showerror("Erro", "Produto não encontrado!")

def atualizar_lista():
    lista_produtos.delete(0, tk.END)
    for chave, valor in meu_dicionario.items():
        lista_produtos.insert(tk.END, f"{chave}: {valor}")

# salvando os dados inputados em um arquivo .json
def salvar_dados():
    with open('produtos.json', 'w') as f:
        json.dump(meu_dicionario, f)

# ao abrir o programa se um arquivo .json existir no diretório, o programa vai carregar e ler os dados
def carregar_dados():
    if os.path.exists('produtos.json'):
        with open('produtos.json', 'r') as f:
            return json.load(f)
    return {}

def sair():
    janela.destroy()

# iniciando o dicionário de produtos
meu_dicionario = carregar_dados()

# janela principal do programa
janela = tk.Tk()
janela.title("Gerenciamento de Produtos")

# botões 
btn_adicionar = tk.Button(janela, text="Adicionar Produto", command=adicionar_produto)
btn_remover = tk.Button(janela, text="Remover Produto", command=remover_produto)
btn_alterar = tk.Button(janela, text="Alterar Quantidade", command=alterar_quantidade)
btn_sair = tk.Button(janela, text="Sair", command=sair)

# lista para exibição dos produtos (pretendo alterar futuramente e fazer em forma de tabela)
lista_produtos = tk.Listbox(janela, width=50, height=15)
atualizar_lista()

# posicionando os botões criados no programa
lista_produtos.pack(pady=10)
btn_adicionar.pack(pady=5)
btn_remover.pack(pady=5)
btn_alterar.pack(pady=5)
btn_sair.pack(pady=5)


janela.mainloop()
