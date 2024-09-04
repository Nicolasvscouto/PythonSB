from janela_client import *
from janela_agendamento import *
import customtkinter as ctk


janela_principal = ctk.CTk()
janela_principal.geometry("500x300")
janela_principal.title("Espaço das Gurias - ADMINISTRAÇÃO")

texto_boasvindas = ctk.CTkLabel(janela_principal, text="Bem-vindo!!", font = ("Arial", 24))
texto_boasvindas.pack(padx = 10, pady = 10)

botao_clientela = ctk.CTkButton(janela_principal, text="Cadastrar Clientes", command=janela_clientela)
botao_clientela.pack(padx = 10, pady = 10)

botao_agendas = ctk.CTkButton(janela_principal, text="Marcar Horários", command=janela_agendamento)
botao_agendas.pack(padx = 20, pady = 20)



janela_principal.mainloop()
