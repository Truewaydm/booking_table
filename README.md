## Test task

### API documentation
Open Postman or browser http://127.0.0.1:8000/

GET tables/ - Returns a list of all tables in the restaurant, has an optional **datetime** parameter that returns free tables
```
Params:
datetime:29.06.2023T20:00
```
POST booking/ - Reserves a table with the following parameters: **name**, **phone_number**, **datetime**, **table**
```
Body:
{
    "name":"Name and Surname",
    "phone_number":"0790987812",
    "datetime":"29.06.2023T20:00",
    "table": 2
}
```

### Project run
```sh
python manage.py makemigrations
```
```sh
python manage.py migrate
```
```sh
python manage.py runserver
```