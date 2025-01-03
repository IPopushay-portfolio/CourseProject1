# Проект1 "Приложение для анализа банковских операций"
## Описание:
Разработка приложения для анализа транзакций, которые находятся в Excel-файле. 
Приложение будет генерировать JSON-данные для веб-страниц, формировать Excel-отчеты,
а также предоставлять другие сервисы.
## Ключевые навыки проекта:
1. Организация проекта:
создание и установка всех необходимых инструментов в PyCharm:
- установка менеджера пакетов Python
- создание ВО в модуле .venv, активация ВО
- установка библиотеки Poetry
- создание нового проекта со всеми зависимостями
- оформление кодов по правилам PEP8
- установка инструментов из группы lint для проверки кода
- добавление docstring в коды для объяснения работы функций
## Установка:
1. Клонируйте репозиторий:
 git clone https://github.com/IPopushay-portfolio/CourseProject1
2. Установите зависимости:
 pip install -r requirements.txt
3. Создайте базу данных и выполните миграции:
 python manage.py migrate
## Команды для проверки тестов:
1. Добавьте пакеты проверок в линтеры (flake8, mypy, black, isort) и проверяйте рабочие файлы
перед обновлением в GitHub
 flake8(mypy, black, isort) 'название рабочей папки'
 git add .
 git commit -m 'add linters' -> Pushing -> GitHub
2. Создайте генераторы списков и используйте их при тестировании каждого элемента
 'выражение for переменная in источник if условие'
## Использование:
1. Откройте приложение в веб-браузере.
2. Создайте новый проект и начните добавлять задачи.
3. Назначайте сроки выполнения и приоритеты для задач, чтобы эффективно управлять проектами.
## Документация:
Для получения дополнительной информации обратитесь к [документации].
## Лицензия:
Проект лицензирован по [лицензии MIT].