# Используем официальный образ Python
FROM python:3.10-slim

# Устанавливаем зависимости
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /app
COPY requirements.txt .
RUN pip install --upgrade pip && pip install -r requirements.txt

COPY . .

# Прогон миграций при запуске
CMD ["gunicorn", "projectname.wsgi:application", "--bind", "0.0.0.0:8080"]
