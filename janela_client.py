import customtkinter as ctk
from db_operations import *
from tkinter import messagebox

def janela_clientela():
    janela_clientela = ctk.CTkToplevel()
    janela_clientela.geometry("500x300")
    janela_clientela.title("Registrar novos clientes")

    janela_clientela.grid_columnconfigure(0, weight=1)
    janela_clientela.grid_columnconfigure(1, weight=1)

    nome_texto = ctk.CTkLabel(janela_clientela, text="Nome") #Indicativo do que a caixa de texto se refere
    nome_texto.grid(row=0, column=0, padx=10, pady=10, sticky="e")

    global nome_entrada
    nome_entrada = ctk.CTkEntry(janela_clientela) #Caixa de texto para inserir os nomes e enviar pro banco de dados
    nome_entrada.grid(row=0, column=1, padx=10, pady=10, sticky="w")

    telefone_texto = ctk.CTkLabel(janela_clientela, text="Telefone")
    telefone_texto.grid(row=2, column=0, padx=10, pady=10, sticky="e")

    global telefone_entrada
    telefone_entrada = ctk.CTkEntry(janela_clientela) 
    telefone_entrada.grid(row=2, column=1, padx=10, pady=10, sticky="w")

    enviarValores = ctk.CTkButton(janela_clientela, text="Cadastrar novo usuário", command=enviar_clientes_BD)
    enviarValores.grid(row=3, columnspan=2, pady=20)

def enviar_clientes_BD():
    nome = nome_entrada.get()
    telefone = telefone_entrada.get()
    if not nome_entrada.get() or not telefone_entrada.get():
        messagebox.showerror("Campos obrigatórios", "Por favor, preencha todos os campos")
    else:
        add_cliente(nome,telefone)
        messagebox.showinfo("Parabens", "Você cadastrou um usuário")