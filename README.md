Сервис уведомлений
Тестовое задание для кандидатов-разработчиков



запуск
sudo docker-compose -f docker-compose.yml up web



для доступа либо

'Authorization: Token f3a527cd037b3a1e4d41f9e1afd7db26b6ba9cda' в заголовке запроса

либо для веб интерфейса drf:

username adminaccount
password adminpass





доп задания: 3,8


===================================================================================================================

добавления нового клиента в справочник со всеми его атрибутами

curl -X POST http://0.0.0.0:8000/Clients/  -H 'Authorization: Token 

f3a527cd037b3a1e4d41f9e1afd7db26b6ba9cda' -d phone_number=79774053329

json
{
    "phone_number": "string",   required  unique
    "tag": "string",
    "timezone": "string"
}


"phone_number" - уникальная строка(есть валидация номеров в формате 79XXXXXXXXX) X = 0-9

код оператора парсится автоматически (9XX) X=0-9

"timezone" - строка поддерживающая любой часовой пояс из pytz common_timezones

default = UTC

http://pytz.sourceforge.net/index.html?highlight=common_timezones#helpers


===================================================================================================

обновления данных атрибутов клиента by id

curl -X PATCH http://0.0.0.0:8000/Clients/{id}/  -H 'Authorization: Token

f3a527cd037b3a1e4d41f9e1afd7db26b6ba9cda' -d phone_number=79774053328


{id} = int

json
{
    "phone_number": "string",
    "tag": "string",
    "timezone": "string"
}


===========================================================================================

удаления клиента из справочника by id

curl -X DELETE http://0.0.0.0:8000/Clients/{id}/  -H 'Authorization: Token f3a527cd037b3a1e4d41f9e1afd7db26b6ba9cda'

{id} = int

===================================================================================================================

добавления новой рассылки со всеми её атрибутами

curl -X POST http://0.0.0.0:8000/Mailing/  -H 'Authorization: Token f3a527cd037b3a1e4d41f9e1afd7db26b6ba9cda' -d datetime_end=2022-08-20T21:42:16 -d datetime_start=2022-08-22T22:42:16 -d message_text=123123123



json
{
    "datetime_start": "string",   required
    "message_text": "string",     requires
    "datetime_end": "string",     required
    "filter_tag": "string",
    "filter_op_codes": "string"
}





datetime_start, message_text = строки в формате python datetime.datetime

filter_tag, filter_op_codes = строка где теги/коды 
разделены запятой или строка с 1м тегом/кодом пример "977,921,925" |  "тег3"




======================================================================================

получения общей статистики по созданным рассылкам и количеству отправленных 
сообщений по ним с группировкой по статусам


curl -X GET http://0.0.0.0:8000/Stats/  -H 'Authorization: Token f3a527cd037b3a1e4d41f9e1afd7db26b6ba9cda'




=========================================================================================

получения детальной статистики отправленных сообщений по конкретной рассылке by id

curl -X GET http://0.0.0.0:8000/Stats/{id}/  -H 'Authorization: Token f3a527cd037b3a1e4d41f9e1afd7db26b6ba9cda'

{id} = int

==============================================================================================

обновления атрибутов рассылки by id

curl -X PATCH http://0.0.0.0:8000/Mailing/{id}/  -H 'Authorization: Token f3a527cd037b3a1e4d41f9e1afd7db26b6ba9cda' -d datetime_end=2022-08-22T22:42:16

{id} = int

json

{

    "datetime_start": "string",

    "message_text": "string",
    
    "datetime_end": "string"


}

=======================================================

удаления рассылки by id


curl -X DELETE http://0.0.0.0:8000/Mailing/{id}/  -H 'Authorization: Token f3a527cd037b3a1e4d41f9e1afd7db26b6ba9cda'

{id} = int


