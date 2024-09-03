"""
Arquivo que é responsavel pela janela de agendamentos de horários
"""



import customtkinter as ctk
from tkinter import messagebox

import psycopg2.sql
from db_operations import *



def janela_agendamento():
    window_agendamento = ctk.CTkToplevel()
    window_agendamento.geometry("500x300")
    window_agendamento.title("Agendamento de Horários")

    # ID do Cliente
    id_cliente_text = ctk.CTkLabel(window_agendamento, text="ID do Cliente")
    id_cliente_text.grid(row=0, column=0, padx=10, pady=5, sticky="e")

    global id_cliente_entrada
    id_cliente_entrada = ctk.CTkEntry(window_agendamento)
    id_cliente_entrada.grid(row=0, column=1, padx=10, pady=5, sticky="w")

    
    id_servico_text = ctk.CTkLabel(window_agendamento, text="ID do Serviço Ofertado")
    id_servico_text.grid(row=1, column=0, padx=10, pady=5, sticky="e")

    global id_servico_entrada
    id_servico_entrada = ctk.CTkEntry(window_agendamento)
    id_servico_entrada.grid(row=1, column=1, padx=10, pady=5, sticky="w")

   
    data_hora_text = ctk.CTkLabel(window_agendamento, text="Data e Hora [D/M/A HH:MM]")
    data_hora_text.grid(row=2, column=0, padx=10, pady=5, sticky="e")

    global data_hora_entrada
    data_hora_entrada = ctk.CTkEntry(window_agendamento)
    data_hora_entrada.grid(row=2, column=1, padx=10, pady=5, sticky="w")

   
    botao_enviar_agendamento = ctk.CTkButton(window_agendamento, text="Agendar Horário", command=enviar_agendamentos_DB)
    botao_enviar_agendamento.grid(row=3, columnspan=2, pady=20)


def enviar_agendamentos_DB():
    id_cliente = id_cliente_entrada.get()
    id_servico = id_servico_entrada.get()
    data_hora = data_hora_entrada.get()
    if not id_cliente_entrada.get() or not id_servico_entrada.get() or not data_hora_entrada.get():
        messagebox.showwarning("Campos Obrigatórios", "Por favor, preencha todos os campos")
    c.execute("SELECT * FROM agendamento WHERE data_hora = %s", (data_hora,))
    if c.fetchone():
        messagebox.showerror("Erro", "Horário Ocupado já, tente outro!")
    else:
        add_agendamento(id_cliente, id_servico, data_hora)
        messagebox.showinfo("Parabens", "Voce agendou seu horário")









