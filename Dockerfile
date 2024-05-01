# Используем официальный образ Python как базовый
FROM python:3.8

# Устанавливаем переменные окружения
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Устанавливаем рабочую директорию в контейнере
WORKDIR /prod_project

# Копируем файл с зависимостями
COPY requirements.txt /tmp/

# Устанавливаем зависимости Python
RUN pip3 install --no-cache-dir -r /tmp/requirements.txt

# Копируем весь каталог проекта в контейнер
COPY prod_project/ ./

# Копируем скрипт entrypoint.sh в рабочий каталог
COPY entrypoint.sh ./

# Делаем скрипт entrypoint.sh исполняемым
RUN chmod +x entrypoint.sh

# Копируем скрипт create_superuser.py в рабочий каталог
COPY create_superuser.py ./

# Задаем entrypoint скрипт
ENTRYPOINT ["./entrypoint.sh"]

# Определяем команду по умолчанию (CMD) для запуска веб-сервера Django
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
