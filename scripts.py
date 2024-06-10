import random

def get_datas():

    data_array = []
    
    for i in range(10):
        intervalo_pressao = random.randint(1000, 1020)
        intervalo_temperatura = random.randint(30, 50) 

        data = {
            "id": i,
            "pressure": intervalo_pressao,
            "temperature": intervalo_temperatura,
        }
        
        data_array.append(data)

    return data_array
    
def compare_pressure_data():
    data_array = get_datas()
    change_limit = 10

    current_pressure_data = data_array[-1]['pressure']
    previous_pressure_data = data_array[-2]['pressure']

    diferenca_dos_dados = abs(current_pressure_data - previous_pressure_data)

    if diferenca_dos_dados > change_limit:
        return f'[ALERTA] A pressão aumentou repentinamente! De {current_pressure_data}hPa foi para {previous_pressure_data}hPa em 5 minutos'
    else:
        return f'Está tudo ok!'


def compare_temperature_data():
    data_array = get_datas()
    change_limit = 10

    current_temperature_data = data_array[-1]['temperature']
    previous_temperature_data = data_array[-2]['temperature']

    diferenca_dos_dados = abs(current_temperature_data - previous_temperature_data)

    if diferenca_dos_dados > change_limit:
        return f'[ALERTA] A temperatura aumentou repentinamente! de {current_temperature_data}°C foi para {previous_temperature_data}°C em 5 minutos'
    else:
        return f'Está tudo ok!'

def monitorar_dados():
    status_pressure = compare_pressure_data()
    status_temparature = compare_temperature_data()
    print(f'Status pressão: {status_pressure}. Status temperatura: {status_temparature}')

monitorar_dados()