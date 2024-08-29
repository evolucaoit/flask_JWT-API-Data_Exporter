import requests
import json
import yaml
import xml.etree.ElementTree as ET
import logging

# Configuração de logs
logging.basicConfig(filename='client.log', level=logging.INFO)

def get_token():
    """Função para obter o token JWT do servidor."""
    try:
        response = requests.post('http://localhost:666/login', json={'username': 'user', 'password': 'pass'})
        response.raise_for_status()
        return response.json()['token']
    except requests.exceptions.HTTPError as err:
        logging.error(f'HTTP error occurred during login: {err}')
        return None
    except KeyError:
        logging.error('Token not found in response')
        return None

def fetch_data(token, id):
    """Função para obter dados da API usando o token JWT."""
    headers = {'Authorization': token}
    try:
        response = requests.get(f'http://localhost:666/data/{id}', headers=headers)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.HTTPError as err:
        logging.error(f'HTTP error occurred during data fetch: {err}')
        return None
    except ValueError as err:
        logging.error(f'Error decoding JSON: {err}')
        return None

def save_to_files(data):
    """Função para salvar os dados em vários formatos de arquivo."""
    if data is None:
        logging.error('No data to save')
        return

    # Salvando em JSON
    try:
        with open('data.json', 'w') as f:
            json.dump(data, f)
        logging.info('Data saved to JSON file')
    except Exception as e:
        logging.error(f'Error saving data to JSON: {e}')

    # Salvando em YAML
    try:
        with open('data.yaml', 'w') as f:
            yaml.dump(data, f)
        logging.info('Data saved to YAML file')
    except Exception as e:
        logging.error(f'Error saving data to YAML: {e}')

    # Salvando em XML
    try:
        root = ET.Element("root")
        for item in data:
            elem = ET.SubElement(root, "item")
            for key, val in item.items():
                child = ET.SubElement(elem, key)
                child.text = str(val)
        tree = ET.ElementTree(root)
        tree.write('data.xml')
        logging.info('Data saved to XML file')
    except Exception as e:
        logging.error(f'Error saving data to XML: {e}')

    # Salvando em TXT
    try:
        with open('data.txt', 'w') as f:
            for item in data:
                f.write(f"{item}\n")
        logging.info('Data saved to TXT file')
    except Exception as e:
        logging.error(f'Error saving data to TXT: {e}')

def main():
    """Função principal para executar o cliente."""
    try:
        token = get_token()
        if token:
            data = fetch_data(token, 1)  # Substitua 1 pelo ID desejado
            save_to_files(data)
            logging.info('Data fetched and saved successfully')
        else:
            logging.error('Failed to retrieve token')
    except Exception as e:
        logging.error(f'Unexpected error: {e}')

if __name__ == '__main__':
    main()
