1. Название проекта
2. Краткое описание
3. Как запустить проект(создать venv, активировать venv, установить зависимости, команда для запуска)
4. Тестирование проекта ( Все Url, так же готовые данные для тестирование, какой запрос отправлять)

## Простой API блог:

Блог использующий стек Flask и JSON. 
API иметь 2 сущности:

    - Пользователь
    - Пост

Возможности пользователя:

    - создать
    - прочитать
    - изменить
    - удалить пост 

## Настройка:

# Cоздать venv
- Откройте терминал или командную строку
- Перейдите в каталог, где вы хотите создать виртуальное окружение
- Введите следующую команду:

python3 -m venv myenv

# Активация виртуального окружения

Для активации виртуального окружения используйте следующие команды:

    Windows:
        myenv\Scripts\activate
        
    macOS и Linux:
        source myenv/bin/activate
    
После активации окружения ваш терминал или командная строка изменятся, и вы увидите имя виртуального окружения в начале строки.

(myenv) user@host:~$

# Установка пакетов и зависимостей

Чтобы установить пакеты в активированном виртуальном окружении, используйте команду pip install.
Для текущего проекта нам понадобится библиотека Flask. - `https://flask.palletsprojects.com/en/3.0.x/installation/`

Для установки используйте следующую команду:

    pip install Flask


## Использование блога:
После запуска приложения выведет сообщение:

 * Serving Flask app 'blog'
 * Debug mode: on
WARNING: This is a development server. Do not use it in a production deployment. Use a production WSGI server instead.
 * Running on http://127.0.0.1:5000
Press CTRL+C to quit
 * Restarting with stat
 * Debugger is active!
 * Debugger PIN: 133-704-822

Наш сервер запущен на `http://127.0.0.1:5000`
Для проверки при переходе получим сообщение Start page

# Возможности приложения:

    - создать
    - прочитать
    - изменить
    - удалить пост 
## Endpoints

### Создать: POST /posts 

* Создает новый пост в блоге.
* Пример тела запроса: `{"title": string, "content": string, "author_id": string}`.
* После успешной отправки получаем ответ: `201 Created` и пост с номером согласно порядку размещения.

Пример:
    Отправили - {
        "title": "First_post",
        "content": "post for first test",
        "author_id": "Antonio Banderos"
        }
    
    Получили - {
    "author_id": "Antonio Banderos",
    "content": "post for first test",
    "id": 1,
    "title": "First_post"
    }

### GET /posts

* Retrieves a list of all blog posts.
* Response: `200 OK` with a list of all posts in JSON format.

### GET /posts/<int:post_id>

* Retrieves a specific blog post by ID.
* Response: `200 OK` with the post data if found, or `404 Not Found` if not.

### PUT /posts/<int:post_id>

* Updates a specific blog post by ID.
* Request body: `{"title": string, "content": string}`.
* Response: `200 OK` with the updated post data if found, or `404 Not Found` if not.

### DELETE /posts/<int:post_id>

* Deletes a specific blog post by ID.
* Response: `200 OK` with a success message if found, or `404 Not Found` if not.

## Notes

* This is a simple proof-of-concept API and should not be used in production without additional security measures.
* The `posts` list is stored in memory, so data is lost when the application restarts.
* The API uses JSON encoding and decoding to communicate with clients.

I hope this helps! Let me know if you have any questions or need further clarification.