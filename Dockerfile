# Указываем базовый образ
FROM python:3.9-slim

# Устанавливаем необходимые пакеты
RUN pip install --no-cache-dir faker

# Устанавливаем переменную среды для отключения буферизации
ENV PYTHONUNBUFFERED=1

# Копируем скрипт в контейнер
COPY generate_logs.py /app/generate_logs.py

# Переходим в рабочую директорию
WORKDIR /app

# Указываем команду запуска
CMD ["python", "generate_logs.py"]
