import mysql.connector
from datetime import datetime

def input_equipment_info():
    print("\nINFORMAÇÕES DO EQUIPAMENTO:")
    modelo = input("Digite o MODELO: ")
    marca = input("Digite a MARCA: ")
    mac = input("Digite o MAC: ")
    return modelo, marca, mac
def insert_data_to_db(host, user, password, database, equip_info, ping_results, speed_results):
    modelo, marca, mac = equip_info

    try:
        # Estabelecer conexão com o banco de dados
        db_connection = mysql.connector.connect(
            host=host,
            user=user,
            password=password,
            database=database
        )

        # Criar o cursor para executar as operações SQL
        cursor = db_connection.cursor()

        # Incluir os dados da tabela Equipamento
        insert_equipment_query = "INSERT INTO equipamento (marca, modelo, mac) VALUES (%s, %s, %s)"
        equipment_values = (marca, modelo, mac)
        cursor.execute(insert_equipment_query, equipment_values)

        # Obter o ID do equipamento inserido
        equip_id = cursor.lastrowid

        # Incluir os dados da tabela Ping para ms1, ms2 e ms3
        insert_ping_query = "INSERT INTO ping (equipamento, ms1, ms2, ms3, data_hora_ping) VALUES (%s, %s, %s, %s, %s)"
        ping_values = [(equip_id, ms1, ms2, ms3, data_hora_ping) for ms1, ms2, ms3, data_hora_ping in ping_results]
        cursor.executemany(insert_ping_query, ping_values)

        # Incluir os dados da tabela SpeedTest para download, upload e data_hora_speedtest
        insert_speed_query = "INSERT INTO speedtest (equipamento, download_speed, upload_speed, data_hora_speedtest) VALUES (%s, %s, %s, %s)"
        speed_values = [(equip_id, download_speed, upload_speed, data_hora_speedtest) for download_speed, upload_speed, data_hora_speedtest in speed_results]
        cursor.executemany(insert_speed_query, speed_values)

        # Efetivar as alterações no banco de dados
        db_connection.commit()

        print("\nDados inseridos no banco de dados com sucesso!")

    except mysql.connector.Error as error:
        print(f"Erro ao conectar ao banco de dados: {error}")

    finally:
        # Fechar cursor e conexão
        if cursor:
            cursor.close()
        if db_connection:
            db_connection.close()
