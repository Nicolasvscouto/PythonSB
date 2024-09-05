import customtkinter as ctk
from tkinter import messagebox
from db_operations import *
import datetime


def janela_agendamento():
    window_agendamento = ctk.CTkToplevel()
    window_agendamento.geometry("500x300")
    window_agendamento.title("Agendamento de Horários")

    # Configurar grid
    window_agendamento.grid_columnconfigure(0, weight=1)
    window_agendamento.grid_columnconfigure(1, weight=1)

    # ID do Cliente
    nome_cliente_text = ctk.CTkLabel(window_agendamento, text="Nome do Cliente: ")
    nome_cliente_text.grid(row=0, column=0, padx=10, pady=5, sticky="e")

    global nome_cliente_entrada
    nome_cliente_entrada = ctk.CTkComboBox(window_agendamento, state='readonly')
    client_data = get_clientes_BD()
    client_dict = {name: id for id, name in client_data}
    client_names = list(client_dict.keys())
    nome_cliente_entrada.configure(values=client_names)
    nome_cliente_entrada.grid(row=0, column=1, padx=10, pady=5, sticky="w")

    # ID do Serviço
    nome_servico_text = ctk.CTkLabel(window_agendamento, text="Qual serviço deseja? ")
    nome_servico_text.grid(row=1, column=0, padx=10, pady=5, sticky="e")

    global nome_servico_entrada
    nome_servico_entrada = ctk.CTkComboBox(window_agendamento, state='readonly')
    servico_data = get_servico_DB()
    servico_dict = {name: id for id, name in servico_data}
    servico_names = list(servico_dict.keys())
    nome_servico_entrada.configure(values=servico_names)
    nome_servico_entrada.grid(row=1, column=1, padx=10, pady=5, sticky="w")

    # Horário
    data_hora_text = ctk.CTkLabel(window_agendamento, text="Data e Hora [D/M/A HH:MM]")
    data_hora_text.grid(row=2, column=0, padx=10, pady=5, sticky="e")

    global data_hora_entrada
    data_hora_entrada = ctk.CTkEntry(window_agendamento)
    data_hora_entrada.grid(row=2, column=1, padx=10, pady=5, sticky="w")

    # Botão de Agendamento
    botao_enviar_agendamento = ctk.CTkButton(window_agendamento, text="Agendar Horário", command=lambda:enviar_agendamentos_DB(client_dict, servico_dict))
    botao_enviar_agendamento.grid(row=3, column=0, columnspan=2, pady=20)



def enviar_agendamentos_DB(client_dict,  servico_dict):
    cliente_id = client_dict.get(nome_cliente_entrada.get())  
    servico_id = servico_dict.get(nome_servico_entrada.get())
    data_hora = data_hora_entrada.get()
    data_hora_formatada = datetime.datetime.strptime(data_hora, '%d/%m/%Y %H:%M')
    if not cliente_id or not servico_id or not data_hora:
        messagebox.showwarning("Campos Obrigatórios", "Por favor, preencha todos os campos")
        return
    c.execute("SELECT * FROM agendamento WHERE data_hora = %s", (data_hora,))
    if c.fetchone():
            messagebox.showerror("Erro", "Horário Ocupado já, tente outro!")
    else:
            add_agendamento(cliente_id, servico_id, data_hora)
            messagebox.showinfo("Parabéns", "Você agendou seu horário")