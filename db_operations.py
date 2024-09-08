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


def add_cliente(nome, telefone):
    with connect_db() as conn:
        with conn.cursor() as cursor:
            cursor.execute(
                "INSERT INTO cliente (nome, telefone) VALUES (%s, %s)",
                (nome, telefone)
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

def check_cliente_existente(nome):
    with connect_db() as conn:
        with conn.cursor() as cursor:
            cursor.execute("SELECT 1 FROM cliente WHERE nome = %s", (nome,))
            return cursor.fetchone() is not None


def get_clientes_BD():
    with connect_db() as conn:
        with conn.cursor() as cursor:
            cursor.execute("SELECT ID_CLIENTE, NOME FROM CLIENTE")
            cliente_nomes = cursor.fetchall()
            return cliente_nomes


def get_servico_DB():
    with connect_db() as conn:
        with conn.cursor() as cursor:
            cursor.execute("SELECT ID_SERVICO, NOME FROM SERVICO")
            servico_nomes = cursor.fetchall()
            return servico_nomes
