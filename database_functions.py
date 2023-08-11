import mysql.connector
from datetime import datetime
import PySimpleGUI as sg

class EquipmentInfo:
    def __init__(self, host, user, password, database):
        self.host = host
        self.user = user
        self.password = password
        self.database = database
        self.window = None

    def insert_data_to_db(self, equip_info, ping_results, speed_results):
        modelo, marca, mac = equip_info

        try:
            db_connection = mysql.connector.connect(
                host=self.host,
                user=self.user,
                password=self.password,
                database=self.database
            )

            cursor = db_connection.cursor()

            insert_equipment_query = "INSERT INTO equipamento (marca, modelo, mac) VALUES (%s, %s, %s)"
            equipment_values = (marca, modelo, mac)
            cursor.execute(insert_equipment_query, equipment_values)

            equip_id = cursor.lastrowid

            insert_ping_query = "INSERT INTO ping (equipamento, ms1, ms2, ms3, data_hora_ping) VALUES (%s, %s, %s, %s, %s)"
            ping_values = [(equip_id, ms1, ms2, ms3, data_hora_ping) for ms1, ms2, ms3, data_hora_ping in ping_results]
            cursor.executemany(insert_ping_query, ping_values)

            insert_speed_query = "INSERT INTO speedtest (equipamento, download_speed, upload_speed, data_hora_speedtest) VALUES (%s, %s, %s, %s)"
            speed_values = [(equip_id, download_speed, upload_speed, data_hora_speedtest) for download_speed, upload_speed, data_hora_speedtest in speed_results]
            cursor.executemany(insert_speed_query, speed_values)

            db_connection.commit()

            print("\nDados inseridos no banco de dados com sucesso!")

        except mysql.connector.Error as error:
            print(f"Erro ao conectar ao banco de dados: {error}")

        finally:
            if cursor:
                cursor.close()
            if db_connection:
                db_connection.close()


