# Diploma
Необходим PosgreSQL. Создаем БД с именем 'server_main' пароль устанавливаем fedor123. И заливаем с backup данные.

1.http://localhost:8000/driver//active/sit/?idstop=3 (запрос возвращает количество пассажиров которые должны сесть в салон, передается остановки idstop)#не работает пока =)
2.http://localhost:8000/driver/active/out/?iddriver=2 (запрос возвращает количество пассажиров которые выйдут передается id водилы)#не работает пока =)
3. http://localhost:8000/driver/active/edit/2/ (редактируется статус водителя где находится, активный или нет,номер маршрута, количество пассажиров)
4. http://localhost:8000/driver/active/create/ (создание водителя в БД. Высшел на маршрут)

1.http://localhost:8000/client/active/all/ (список всех пассажиров, ожидающих)
2.http://localhost:8000/client/active/create/ (создание пассажира, ожидающего)
3.http://localhost:8000/client/active/edit/1/ (редактирование пассажира, напиример id = 1)

1.http://localhost:8000/route/stop/all (список всех остановок)
2.http://localhost:8000/route/route/all (список всех маршрутов)
3.http://localhost:8000/route/1 (вывод первого маршрута по id)
4.http://localhost:8000/route/stop/1 (вывод первого остановки по id)
5.http://localhost:8000/route/edit_route/1 (редактирование первого маршрута по id)
6.http://localhost:8000/route/edit_stop/1 (редактирование первого останова по id)

1.http://localhost:8000/statistic/statistic/create/ (создание статистика)
2.http://localhost:8000/statistic/statistic/1 (редактирование статистика)
3.http://localhost:8000/statistic/schedule/add/ (добавление расписания)
4.http://localhost:8000/statistic/schedule/edit/1 (редактирование расписания)

1.http://localhost:8000//auth/users/ (создание пользавателя или водилы {
    "email": "",
    "username": "",
    "password": ""
})
2.После регистрации необходимо аутентифицироватся: http://127.0.0.1:8000/auth/token/ передаем:
{
    "username": "zasik",
    "password": "123"
}
Если все good приходит токен с двумя полями, нам нужен "access" копируем :
{
    "refresh": "",
    "access": ""
}
И передаем этот токен. Пример:
GET /route/stop/all HTTP/1.1
Host: 127.0.0.1:8000
Authorization: Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNTkwMDc5OTgxLCJqdGkiOiI4ODBiNTRkZTQ1NzA0ODMwOWNiMjg0ODUxZmFhZjczNCIsInVzZXJfaWQiOjF9.vLQZQmcH3qWENZYNTkbsImA_NQjA5ekRPCY7AktY3Ho
Cookie: csrftoken=PkUX9AKN8kyy6GWD78V5MR8EW4v5jNmzMg2LzS94gUzsc4PzKV4oKqVqAjpRiGiB

