from datetime import datetime

# import pandas as pd

# from src.utils import get_operations


def main_page(date: str):
    """Функция для страницы «Главная» принимает на вход строку с датой и временем в формате
    YYYY-MM-DD HH:MM:SS"""
    date = datetime.strptime(date, __format="YYYY-MM-DD HH:MM:SS")
    return date


def get_card_number(card_number: str) -> str:
    """Функция принимает на вход номер счета и возвращает его маску"""

    return f" **{card_number[-4:]}"
