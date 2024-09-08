import customtkinter as ctk
import psycopg2
from janela_client import *

# Conexão com o banco de dados PostgreSQL
conn = psycopg2.connect(
    dbname="salao_cabeleireiro",
    user="postgres",
    password="8455",
    host="localhost",
    port="5432"
)
cursor = conn.cursor()

# Consulta para obter os dados dos usuários
cursor.execute("SELECT * FROM cliente")
rows = cursor.fetchall()

# Função para criar a tabela na interface gráfica
# Função para criar a tabela na interface gráfica
def criar_tabela():
    # Cabeçalhos das colunas
    colunas = ["ID", "Nome", "Email", "Idade"]
    for j, col in enumerate(colunas):
        e = ctk.CTkLabel(master=frame, text=col, font=("Arial", 12, "bold"), anchor="center")
        e.grid(row=0, column=j, padx=5, pady=5)

    # Dados dos usuários
    for i, row in enumerate(rows):
        for j, val in enumerate(row):
            e = ctk.CTkLabel(master=frame, text=val, anchor="center")
            e.grid(row=i+1, column=j, padx=5, pady=5)

# Função para abrir a janela de cadastro
def abrir_janela_cadastro():
    janela_cadastro = ctk.CTkToplevel(app)
    janela_cadastro.title("Cadastrar Usuário")
    janela_cadastro.geometry("300x200")

    # Campos de entrada
    ctk.CTkLabel(janela_cadastro, text="Nome:").pack(pady=5)
    entrada_nome = ctk.CTkEntry(janela_cadastro)
    entrada_nome.pack(pady=5)

    ctk.CTkLabel(janela_cadastro, text="Email:").pack(pady=5)
    entrada_email = ctk.CTkEntry(janela_cadastro)
    entrada_email.pack(pady=5)

    ctk.CTkLabel(janela_cadastro, text="Idade:").pack(pady=5)
    entrada_idade = ctk.CTkEntry(janela_cadastro)
    entrada_idade.pack(pady=5)

    # Função para salvar os dados no banco de dados
    def salvar_usuario():
        nome = entrada_nome.get()
        email = entrada_email.get()
        idade = entrada_idade.get()
        cursor.execute("INSERT INTO usuarios (nome, email, idade) VALUES (%s, %s, %s)", (nome, email, idade))
        conn.commit()
        janela_cadastro.destroy()
        # Atualizar a tabela principal
        cursor.execute("SELECT * FROM usuarios")
        rows = cursor.fetchall()
        criar_tabela()

    # Botão para salvar
    ctk.CTkButton(janela_cadastro, text="Salvar", command=salvar_usuario).pack(pady=20)

# Configuração da janela principal
app = ctk.CTk()
app.title("Dados dos Usuários")
app.geometry("600x400")

# Frame para a tabela
frame = ctk.CTkFrame(master=app)
frame.pack(pady=20, padx=20, fill="both", expand=False)

# Botão para abrir a janela de cadastro
botao_cadastrar = ctk.CTkButton(app, text="Cadastrar Usuário", command=janela_clientela)
botao_cadastrar.place(relx=1.0, rely=1.0, anchor="se", x=-10, y=-10)

# Chamando a função para criar a tabela
criar_tabela()

# Executando a aplicação
app.mainloop()

# Fechando a conexão com o banco de dados
cursor.close()
conn.close()