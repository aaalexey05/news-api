# News API - REST API для управления новостями

REST API для новостного портала, построенное на Flask и PostgreSQL.

## Описание

Простое REST API для управления новостями с поддержкой CRUD-операций, пагинации и валидации данных.

### Технологический стек
- **Flask** 
- **PostgreSQL** 
- **SQLAlchemy** 
- **Flask-Migrate** 
- **psycopg** 
- **Marshmallow**

---

## Установка и запуск
#### macOS
- Установка через Homebrew
```brew install postgresql```
- Запуск службы
```brew services start postgresql```
- Добавление в PATH
```echo 'export PATH="/opt/homebrew/opt/postgresql/bin:$PATH"' >> ~/.zshrc```
```source ~/.zshrc```

#### Windows
1. Скачайте установщик PostgreSQL с [официального сайта](https://www.postgresql.org/download/windows/)
2. Запустите установщик и следуйте инструкциям
3. Запомните пароль для пользователя `postgres`
4. После установки PostgreSQL будет доступен через меню Пуск

#### Linux (Ubuntu/Debian)
1. Обновление пакетов ```sudo apt update```
2. Установка PostgreSQL ```sudo apt install postgresql postgresql-contrib```
3. Запуск службы ```sudo systemctl start postgresql```
```sudo systemctl enable postgresql```
4. Проверка статуса ```sudo systemctl status postgresql```

---
### Шаг 2: Клонирование проекта
```git clone https://github.com/yourusername/news-api.git```
```cd news-api```


---

### Шаг 3: Создание виртуального окружения
#### macOS / Linux
- Создание виртуального окружения ```python3 -m venv .venv```
- Активация ```source .venv/bin/activate```

#### Windows
- Создание виртуального окружения ```python -m venv .venv```
- Активация (PowerShell) ```.venv\Scripts\Activate.ps1```
- Или для CMD ```.venv\Scripts\activate.bat```

---

### Шаг 4: Установка зависимостей
```pip install -r requirements.txt```
**Если возникает ошибка с psycopg:**
- Альтернативная установка
```pip install --upgrade pip```
```pip install "psycopg[binary]"```

---

### Шаг 5: Создание базы данных

#### macOS / Linux
1. Подключение к PostgreSQL ```psql postgres```
2. Для Linux: ```sudo -u postgres psql```


#### Windows
1. Через командную строку
```psql -U postgres```
2. Введите пароль, который указали при установке



#### Создание БД (для всех ОС)
В консоли `psql` необходимо выполнить следующее:

```CREATE DATABASE newsdb;```
```CREATE USER newsdbuser WITH PASSWORD 'root';```
```ALTER DATABASE newsdb OWNER TO newsdbuser;```
```GRANT ALL PRIVILEGES ON DATABASE newsdb TO newsdbuser;```

- Выход: ```\q```


---

### Шаг 6: Настройка `.env` файла
Создайте файл `.env` в корне проекта (news-api):

#### macOS / Linux
- Создание файла 
```touch .env```
```nano .env```

#### Windows
- Создание файла
```New-Item .env -ItemType File```
```notepad .env```

#### Содержимое `.env` (для всех ОС)
```FLASK_ENV=development```
```SECRET_KEY=your-secret-key-here```
````DATABASE_URL=postgresql+psycopg://username:password@localhost:5432/database-name```

---

### Шаг 7: Установка переменных окружения

#### macOS / Linux
```export FLASK_APP=run.py```
```export FLASK_ENV=development```

#### Windows (PowerShell)
```$env:FLASK_APP="run.py"```
```$env:FLASK_ENV="development"```

#### Windows (CMD)
```set FLASK_APP=run.py```
```set FLASK_ENV=development```

---

### Шаг 8: Инициализация базы данных
1. Инициализация миграций
```flask db init```
2. Создание миграции
```flask db migrate -m "Initial migration"```
3. Применение миграции
```flask db upgrade```

**Если возникает ошибка "Directory migrations already exists":**
- Необходимо удалить папку migrations и попробовать снова
```rm -rf migrations``` # macOS/Linux
```rmdir /s migrations``` # Windows

### Шаг 9: Запуск приложения
```python run.py```
В основной директории есть файл run.py, в случае, если порт уже занят, его можно поменять:

```python
if __name__ == '__main__':
    app.run(
        host='0.0.0.0', 
        port=5050  # изменить тут (любое значение, например, port=5000)
    )
```

Приложение будет доступно по адресу: [**http://127.0.0.1:5050**](http://127.0.0.1:5050)
