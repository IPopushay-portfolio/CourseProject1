import csv
import json
import logging
import os
from datetime import datetime, timedelta

import pandas as pd
from black import datetime

from src.config import BASE_DIR
from src.external_api import conversion_currency

CURRENT_DIR = os.path.dirname(__file__)
LOGS_DIR = os.path.join(CURRENT_DIR, "..", "logs")
log_file_path = os.path.join(LOGS_DIR, "utils.logs.log")
logger = logging.getLogger("utils.logs")
"""Создание объекта логгера"""
file_handler = logging.FileHandler(log_file_path, mode="w")
"""Создание обработчика"""
logger.setLevel(logging.DEBUG)
"""Установка уровня логгирования"""

file_formater = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s : %(message)s")
"""Создание форматтера"""
file_handler.setFormatter(file_formater)
"""Привязка форматтера к обработчику"""
logger.addHandler(file_handler)
"""Привязка обработчика к логгеру"""

logger = logging.getLogger("transactions.csv")


def get_data_from_csv(path_file_from_csv: str):
    """Функция для считывания финансовых операций из CSV принимает путь к файлу CSV в качестве аргумента"""
    try:
        logger.info(f"Получение данных из файла {path_file_from_csv}")
        with open("transactions.csv") as f:
            reader = csv.reader(f)
            next(reader)
            for row in reader:
                print(row)
    except FileNotFoundError:
        return []


OPERATION_PATH = BASE_DIR.joinpath("data", "operations.csv")


def get_operations() -> pd.DataFrame:
    df = pd.read_csv(OPERATION_PATH)
    df["Дата операции"] = pd.to_datetime(df["Дата операции"], format="YYYY-MM-DD HH:MM:SS")
    df["Дата платежа"] = pd.to_datetime(df["Дата платежа"], format="%d.%m.%Y")
    return df


def filter_by_date(df: pd.DataFrame, date: datetime) -> pd.DataFrame:
    start_date = date.replace(day=1).date()
    print(start_date)

    end_date = (date + timedelta(days=1)).date()
    print(end_date)

    df = df.loc[(df["Дата операции"] >= start_date) & (df["Дата операции"] < end_date)]
    return df


def get_greeting() -> str:
    """Функция принимает на вход строку с датой и временем в формате
    YYYY-MM-DD HH:MM:SS и возвращает приветствие:"""

    current_time = datetime.now()
    if datetime(2020, 5, 1, 4, 1, 1) < current_time <= datetime(2020, 5, 1, 12, 0, 0):
        return "Доброе утро"
    elif datetime(2020, 5, 1, 12, 0, 1) < current_time <= datetime(2020, 5, 1, 17, 0, 0):
        return "Добрый день"
    elif datetime(2020, 5, 1, 17, 0, 1) < current_time <= datetime(2020, 5, 1, 23, 0, 0):
        return "Добрый вечер"
    elif datetime(2020, 5, 1, 23, 0, 1) < current_time <= datetime(2020, 5, 2, 3, 59, 59):
        return "Доброй ночи"


def get_cards_number(card_number: str) -> str:
    """Функция принимает на вход номер карты и возвращает ее маску"""
    logger.info("Маскируем карту клиента")
    return f"{card_number[:4]} {card_number[4:6]}** **** {card_number[12:]}"


def get_transactions(path_file):
    """Функция для получения данных из json-файла"""
    try:
        logger.info(f"Получение данных из файла {path_file}")
        with open(path_file, "r", encoding="UTF-8") as f:
            try:
                data = json.load(f)
            except json.decoder.JSONDecodeError:
                logger.error(f"Ошибка при чтении json_файла {path_file}")
                return []
            if (len(data) == 0) or type(data) is not list:
                return []
    except FileNotFoundError:
        logger.error(f"Ошибка, файл {path_file} не найден")
        return []


def get_sum():
    data = get_transactions("C:\\Users\\user\\Desktop\\Python\\my_prj\\test_poetry\\data\\operations.json")
    lst_str = []
    amount = []
    for i in data:
        if len(i) == 0:
            continue
        elif i["OperationAmount"]["Currency"]["Code"] != "RUB":
            conversion_currency("RUB", i["OperationAmount"]["Currency"]["Code"], i["OperationAmount"]["amount"])
            lst_str.append(i["OperationAmount"]["amount"])
            for j in lst_str:
                amount.append(float(j))
            return sum(amount)


if __name__ == "__utils__":
    print(conversion_currency("RUB", "USD", "200000"))
