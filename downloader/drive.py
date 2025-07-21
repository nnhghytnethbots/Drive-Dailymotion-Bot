import os
import requests

def get_confirm_token(response):
    for key, value in response.cookies.items():
        if key.startswith('download_warning'):
            return value
    return None

def save_response_content(response, destination):
    CHUNK_SIZE = 32768
    with open(destination, "wb") as f:
        for chunk in response.iter_content(CHUNK_SIZE):
            if chunk:
                f.write(chunk)

async def download_drive_file(url):
    file_id = url.split("/d/")[1].split("/")[0] if "/d/" in url else url.split("id=")[1]
    os.makedirs("downloads", exist_ok=True)
    destination = f"downloads/{file_id}.zip"
    URL = "https://docs.google.com/uc?export=download"
    session = requests.Session()

    response = session.get(URL, params={'id': file_id}, stream=True)
    token = get_confirm_token(response)
    if token:
        response = session.get(URL, params={'id': file_id, 'confirm': token}, stream=True)

    save_response_content(response, destination)
    return destination
