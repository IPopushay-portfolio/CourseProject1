import requests


def conversion_currency(tr_cur, pay_cur, amount):
    url = "https://api.github.com/user"
    params = {"data": "operations.csv", "datepay": "Дата платежа"}
    response = requests.get(url, params=params)
    status_code = response.status_code
    print(f"Статус код: {status_code}")
    if status_code == 200:
        content = response.text
        print(f"Содержимое сайта:\n{content}")
    else:
        print(f"Запрос не был успешным. Возможная причина: {response.reason}")

    result = response.json()
    return result


if __name__ == "__main__":
    print(conversion_currency("RUB", "USD", "200000"))
