import tkinter as tk
from tkinter import simpledialog, messagebox
import json
import os

# Funções para manipular o dicionário de produtos
def adicionar_produto():
    chave = simpledialog.askstring("Adicionar Produto", "Digite o nome do produto:")
    if chave:
        valor = simpledialog.askinteger("Adicionar Produto", "Digite a quantidade do produto:")
        if valor is not None:
            meu_dicionario[chave] = valor
            atualizar_lista()
            salvar_dados()

def remover_produto():
    chave = simpledialog.askstring("Remover Produto", "Digite o nome do produto a ser removido:")
    if chave in meu_dicionario:
        del meu_dicionario[chave]
        atualizar_lista()
        salvar_dados()
    else:
        messagebox.showerror("Erro", "Produto não encontrado!")

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

def salvar_dados():
    with open('produtos.json', 'w') as f:
        json.dump(meu_dicionario, f)

def carregar_dados():
    if os.path.exists('produtos.json'):
        with open('produtos.json', 'r') as f:
            return json.load(f)
    return {}

def sair():
    janela.destroy()

# Inicialização do dicionário de produtos
meu_dicionario = carregar_dados()

# Criação da janela principal
janela = tk.Tk()
janela.title("Gerenciamento de Produtos")

# Criação dos botões
btn_adicionar = tk.Button(janela, text="Adicionar Produto", command=adicionar_produto)
btn_remover = tk.Button(janela, text="Remover Produto", command=remover_produto)
btn_alterar = tk.Button(janela, text="Alterar Quantidade", command=alterar_quantidade)
btn_sair = tk.Button(janela, text="Sair", command=sair)

# Criação da lista para exibir os produtos
lista_produtos = tk.Listbox(janela, width=50, height=15)
atualizar_lista()

# Posicionamento dos widgets na janela
lista_produtos.pack(pady=10)
btn_adicionar.pack(pady=5)
btn_remover.pack(pady=5)
btn_alterar.pack(pady=5)
btn_sair.pack(pady=5)

# Execução da janela principal
janela.mainloop()
