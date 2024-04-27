Первая задача
Не стал добавлять файл .gitignore
В данном проекте реализованы endpoints по обновлению и записи данных write_data_endpoint и получение данных check_data_endpoint

Для изменения и обновления данных используется метод post. При записи данных срабатывает endpoint write_data_endpoint и вызывается асинхронная функция write_data, в которой происходит подключение к серверу redis и устнавление ключа(телефон в формате str)
и значения (адрес в формате строки) 

Для получения данных используется endpoint check_data_endpoint. При получении данных по номеру телефона срабатывает  асинхронная функция check_data, в которой происходит получение данных из redis. Если данных нет возвращается None и падает кастомное исключение
StartHoursException. Исключение StartHoursException наследеутеся от MainException. Мы передаем только статус кода и описание исключения. При успешном получении данных возвращается адрес

Классы pydantic находятся в pydantic_schemas.py и используется в write_data_endpoint

Приложение обернуто в docker
Для запуска нужно подлключиться к серверу. Прописать sudo apt-get update для обновления сервера. Если нуждно установить docker и docker-compose.
Для запуска через docker-compose используйте команду docker-compose up --build -d либо docker-compose up --build


Решение воторой задачи
Объединение таблиц с помощью SQL JOIN
UPDATE full_names AS f
SET status = s.status
FROM short_names AS s
WHERE f.name = s.name;

Использование временной таблицы второй вариант
CREATE TEMP TABLE common_names AS
SELECT name FROM short_names
INTERSECT
SELECT name FROM full_names;

UPDATE full_names AS f
SET status = s.status
FROM short_names AS s
WHERE f.name = s.name
  AND s.name IN (SELECT name FROM common_names);
