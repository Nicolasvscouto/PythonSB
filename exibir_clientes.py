from db_operations import *
import customtkinter as ctk
from tkinter import messagebox
from customtkinter import CTkFrame
from janela_client import *
def exibir_clientes():
    #JanelaPrincipal
    janela_exibirCliente = ctk.CTk()
    janela_exibirCliente.geometry("500x300")
    janela_exibirCliente.title("Clientes cadastrados")

    #FramePrincipal que é scrollavel
    tela = ctk.CTkScrollableFrame(janela_exibirCliente)
    tela.pack(pady=20, padx=20, fill="both", expand=False)
    colunas = ["ID", "Nome", "Telefone"]
    for j, col in enumerate(colunas):
        e = ctk.CTkLabel(tela, text=col, font=("Arial", 12, "bold"), anchor="center")
        e.grid(row=0, column=j, padx=5, pady=5)

    #botao para cadastrar cliente
    botao_cadastrarCliente = ctk.CTkButton(janela_exibirCliente, text="Cadastrar Cliente", command=janela_clientela)
    botao_cadastrarCliente.place(relx=1.0, rely=1.0, anchor="se", x=-10, y=-10)

    #Comando para buscar usuarios
    c.execute("Select * from cliente")
    for i, row in enumerate(c):
        for j, val in enumerate(row):
            e = ctk.CTkLabel(tela, text=val, anchor="center")
            e.grid(row=i + 1, column=j, padx=5, pady=5)

    janela_exibirCliente.mainloop()



