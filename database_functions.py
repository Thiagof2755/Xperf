import mysql.connector
from mysql.connector import Error

class EquipmentInfo:
    def __init__(self, host, user, password, database):
        self.host = host
        self.user = user
        self.password = password
        self.database = database

    def insert_data_to_db(self, equipment_info, ping_results):
        try:
            # Conectar ao banco de dados
            connection = mysql.connector.connect(
                host=self.host,
                user=self.user,
                password=self.password,
                database=self.database
            )

            # Inserir dados na tabela 'equipamento'
            cursor = connection.cursor()
            equipamento_query = "INSERT INTO equipamento (marca, modelo, mac) VALUES (%s, %s, %s)"
            cursor.execute(equipamento_query, equipment_info)
            equipamento_id = cursor.lastrowid

            # Inserir dados na tabela 'ping'
            ping_query = "INSERT INTO ping (equipamento, ms1, ms2, ms3, data_hora_ping) VALUES (%s, %s, %s, %s, %s)"
            for ping_result in ping_results:
                cursor.execute(ping_query, (equipamento_id, ping_result[0], ping_result[1], ping_result[2], ping_result[3]))

            # Confirmar a transação
            connection.commit()
            print("Dados inseridos com sucesso!")

        except Error as e:
            print("Erro ao inserir dados no banco de dados:", e)

        finally:
            if connection.is_connected():
                cursor.close()
                connection.close()
