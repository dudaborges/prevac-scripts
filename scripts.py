import datetime
import time
import random

def get_datas(existing_data_array=None):
    if existing_data_array is None:
        existing_data_array = []

    new_data = {
        "id": len(existing_data_array),
        "temperature": random.randint(21, 27),
        "pressure": random.randint(1000, 1100),
        'timestamp': datetime.datetime.now().isoformat()
    }
    existing_data_array.append(new_data)
    return existing_data_array

def compare_pressure_data(data_array, pressure_change_limit):
    current_pressure_data = data_array[-1]['pressure']
    previous_pressure_data = data_array[-2]['pressure']

    diferenca_dos_dados = abs(current_pressure_data - previous_pressure_data)

    if diferenca_dos_dados > pressure_change_limit:
        return f'[ALERTA] A pressão aumentou repentinamente! De {previous_pressure_data}hPa foi para {current_pressure_data}hPa em 5 minutos'
    else:
        return 'Pressão estável.'

def compare_temperature_data(data_array, temperature_change_limit):
    current_temperature_data = data_array[-1]['temperature']
    previous_temperature_data = data_array[-2]['temperature']

    diferenca_dos_dados = abs(current_temperature_data - previous_temperature_data)

    if diferenca_dos_dados > temperature_change_limit:
        return f'[ALERTA] A temperatura aumentou repentinamente! De {previous_temperature_data}°C foi para {current_temperature_data}°C em 5 minutos'
    else:
        return 'Temperatura estável.'
    


def check_data_within_range(data_array, pressure_range, temperature_range):
    current_data = data_array[-1]
    current_pressure = current_data['pressure']
    current_temperature = current_data['temperature']

    if not (pressure_range[0] <= current_pressure <= pressure_range[1]):
        return f'[ALERTA] Pressão fora do intervalo! Pressão atual: {current_pressure}hPa'
    if not (temperature_range[0] <= current_temperature <= temperature_range[1]):
        return f'[ALERTA] Temperatura fora do intervalo! Temperatura atual: {current_temperature}°C'

    return 'Dados dentro do intervalo esperado.'

def send_notification(message):
    print(message)

def monitorar_dados():
    pressure_change_limit = 1110 #valores alterados para permanecerem estaveis 
    temperature_change_limit = 28  #valores alterados para permanecerem estaveis 
    pressure_range = (1000, 1100)
    temperature_range = (21, 27)

    data_array = get_datas()  

    while True:
        data_array = get_datas(data_array)  

        status_pressure = compare_pressure_data(data_array, pressure_change_limit)
        status_temperature = compare_temperature_data(data_array, temperature_change_limit)
        range_check = check_data_within_range(data_array, pressure_range, temperature_range)

        send_notification(f'Status pressão: {status_pressure}')
        send_notification(f'Status temperatura: {status_temperature}')
        send_notification(range_check)

        time.sleep(5) 

monitorar_dados()
