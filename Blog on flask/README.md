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

### Получить все посты: GET /posts

* Получаем список всех сообщений блога.
* Ответ: `200 OK` список всех постов в JSON формате.

Пример:
    http://127.0.0.1:5000/posts
    Response: `200 OK`
    BODY:
    [
     {
        "author_id": "Antonio Banderos",
        "content": "post for first test",
        "id": 1,
        "title": "First_post"
     },
     {
        "author_id": "Burak Chelik",
        "content": "post for second test",
        "id": 2,
        "title": "Second_post"
     }
    ]

### Получаем пост по ID : GET /posts/<int:post_id>

* Получаем определенный пост по ID
* Ответ: `200 OK` в случае если нашли пост, или `404 Not Found` если нет.

Пример:
    GET http://127.0.0.1:5000/posts/2
    Response: `200 OK`
    BODY:
    {
        "author_id": "Burak Chelik",
        "content": "post for second test",
        "id": 2,
        "title": "Second_post"
    }

    GET http://127.0.0.1:5000/posts/3
    Responce: `404 Not found'`
    {
        "error": "Post not found"
    }


### Изменить пост: PUT /posts/<int:post_id>

* Изменить пост по ID
* Привер тела запроса: `{"title": string, "content": string}`.
* Ответ: `200 OK` если нашли и изменили пост, или `404 Not Found` если нет.

Пример:
    PUT http://127.0.0.1:5000/posts/2
    BODY:
        {
            "title": "Change_Second_post",
            "content": "post for second test was change"
        }
    Response `200 OK`
    Ответ:
        {
            "author_id": "Burak Chelik",
            "content": "post for second test was change",
            "id": 2,
            "title": "Change_Second_post"
        }

### Удаление поста: DELETE /posts/<int:post_id>

* Удаляем пост по ID
* Ответ: `200 OK` если нашли и удалили пост, или `404 Not Found` если нет.

Пример:

    DELETE http://127.0.0.1:5000/posts/2

    BODY:
        {
            "success": "Post deleted"
        }