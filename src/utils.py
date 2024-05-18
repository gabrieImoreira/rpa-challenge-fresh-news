import requests
import shutil
import uuid
import os
import datetime

def clear_and_create_directory(directory_path: str):
    """ Limpa e cria diretório"""

    # Verifica se o diretório já existe
    if os.path.exists(directory_path):
        # Limpa o conteúdo do diretório
        shutil.rmtree(directory_path)
    
    # Cria o diretório
    os.makedirs(directory_path)

    return True

def download_image(url: str, output_path: str):
    image_name = str(uuid.uuid4())
    with open(f"{output_path}/{image_name}.jpg", "wb") as handler:
        handler.write(requests.get(url).content)
    
    return f"{output_path}/{image_name}.jpg"

def get_month_range(number_of_months: int):
    today = datetime.date.today()
    if number_of_months < 2:
        end_data = today.replace(day=1).strftime("%m/%d/%Y")
    else:
        end_data = today - datetime.timedelta(days=30 * (number_of_months - 1))
        end_data = end_data.replace(day=1).strftime("%m/%d/%Y")
    return end_data