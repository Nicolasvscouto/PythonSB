from db_operations import *
from janela_agendamento import *
import customtkinter as ctk
from janela_client import *
from exibir_clientes import *
from exibir_horario import *
from customtkinter import CTkFrame


janela_principal = ctk.CTk()
janela_principal.geometry("500x300")
janela_principal.title("Espaço das Gurias - ADMINISTRAÇÃO")

texto_boasvindas = ctk.CTkLabel(janela_principal, text="Seja bem-vindo!", font = ("Arial", 24))
texto_boasvindas.pack(padx = 10, pady = 10)

botao_agendas = ctk.CTkButton(janela_principal, text="Visualizar clientes", command=exibir_clientes)
botao_agendas.pack(padx = 10, pady = 10)

botao_agendas = ctk.CTkButton(janela_principal, text="Marcar Horários", command=exibir_horario)
botao_agendas.pack(padx = 20, pady = 20)



janela_principal.mainloop()
