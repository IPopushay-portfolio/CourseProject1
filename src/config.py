from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

import os

import requests
from dotenv import load_dotenv

load_dotenv()
github_token = os.getenv("GITHUB_TOKEN")
headers = {"Authorization": f"token {github_token}"}
response = requests.get("https://api.github.com/user", headers=headers)


# Обработка ответа
print(response.json())
