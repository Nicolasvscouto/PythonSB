"""
Arquivo dedicado para as operações que são realizadas (cadastrar usuario e realizar agendamento)
"""

import psycopg2

DATABASE = "salao_cabeleireiro"
USER = "postgres"
PASSWORD = "8455"
HOST = "localhost"
PORT = "5432"

def connect_db():
    return psycopg2.connect(
        dbname=DATABASE,
        user=USER,
        password=PASSWORD,
        host=HOST,
        port=PORT
    )

conn = connect_db()
c = conn.cursor()

def add_cliente(nome, email, telefone):
    with connect_db() as conn:
        with conn.cursor() as cursor:
            cursor.execute(
                "INSERT INTO cliente (nome, email, telefone) VALUES (%s, %s, %s)",
                (nome, email, telefone)
            )
            conn.commit()

def add_agendamento(id_cliente, id_servico, data_hora):
    with connect_db() as conn:
        with conn.cursor() as cursor:
            cursor.execute(
                "INSERT INTO agendamento (id_cliente, id_servico, data_hora, status) VALUES (%s, %s, %s, %s)",
                (id_cliente, id_servico, data_hora, 'Agendado')
            )
            conn.commit()

def check_cliente_existente(id_cliente):
    with connect_db() as conn:
        with conn.cursor() as cursor:
            cursor.execute("SELECT 1 FROM cliente WHERE id_cliente = %s", (id_cliente,))
            return cursor.fetchone() is not None

