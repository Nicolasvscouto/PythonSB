from db_operations import *
import customtkinter as ctk
from janela_agendamento import *
import datetime


def exibir_horario():
    #Janela principal
   janela_exibirhorario = ctk.CTk()
   janela_exibirhorario.geometry("500x300")
   janela_exibirhorario.title("Clientes cadastrados")

   #Frame Principal que é scrollavel
   tela = (ctk.CTkScrollableFrame(janela_exibirhorario))
   tela.pack(pady=20, padx=20, fill="both", expand=False)
   colunas = ["ID", "ID_Cliente", "ID_Servico", "Horario Marcado", "Situacao"]
   for j, col in enumerate(colunas):
      e = ctk.CTkLabel(tela, text=col, font=("Arial", 12, "bold"), anchor="center")
      e.grid(row=0, column=j, padx=5, pady=5)


   #botao para cadastro
   botao_cadastrarHorario = ctk.CTkButton(janela_exibirhorario, text="Agendar Horario", command=janela_agendamento)
   botao_cadastrarHorario.place(relx=1.0, rely=1.0, anchor="se", x=-10, y=-10)

   #Comando para buscar os agendamentos e mostra-los
   c.execute("SELECT * FROM agendamento")
   for i, row in enumerate(c):
       for j, val in enumerate(row):
           if j == 3:  # Supondo que a coluna de data seja a quarta coluna (índice 3)
               if isinstance(val, datetime.datetime):
                   val = val.strftime("%d/%m/%y")
               else:
                   val = datetime.datetime.strptime(val, "%Y-%m-%d").strftime("%d/%m/%y")
           e = ctk.CTkLabel(tela, text=val, anchor="center")
           e.grid(row=i + 1, column=j, padx=5, pady=5)

   janela_exibirhorario.mainloop()



