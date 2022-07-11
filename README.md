# gasrocrm-backend

## CI/CD status
[![Scan & Build & Push](https://github.com/Praca-Inzynierska-CDV/gastrocrm-backend/actions/workflows/build.yml/badge.svg)](https://github.com/Praca-Inzynierska-CDV/gastrocrm-backend/actions/workflows/build.yml)

[![Deploy image](https://github.com/Praca-Inzynierska-CDV/gastrocrm-backend/actions/workflows/deploy.yml/badge.svg)](https://github.com/Praca-Inzynierska-CDV/gastrocrm-backend/actions/workflows/deploy.yml)

## Backend aplikacji GastroCRM

| Method | Endpoint                                  | Status         |
|------- | -------------                             |:--------------:|
|`GET`   | [`/api/health`](https://github.com/Praca-Inzynierska-CDV/gastrocrm-backend#get-apihealth)| done |
|`GET`   | [`/api/get-users`](https://github.com/Praca-Inzynierska-CDV/gastrocrm-backend#get-apiget-users) | done |
|`GET`   | [`/api/get-user/<username>`](https://github.com/Praca-Inzynierska-CDV/gastrocrm-backend#get-apiget-userusername) | done |
|`GET`   | [`/api/get-users-by-role/<role>`](https://github.com/Praca-Inzynierska-CDV/gastrocrm-backend#get-apiget-users-by-rolerole) | done |
|`GET`   | [`/api/get-dishes`](https://github.com/Praca-Inzynierska-CDV/gastrocrm-backend#get-apiget-dishes) | done |
|`GET`   | [`/api/get-orders`](https://github.com/Praca-Inzynierska-CDV/gastrocrm-backend#get-apiget-orders) | done |
|`GET`   | [`/api/get-order/<id>`](https://github.com/Praca-Inzynierska-CDV/gastrocrm-backend#get-apiget-orderid) | done |
|`GET`   | [`/api/get-dish/<id>`](https://github.com/Praca-Inzynierska-CDV/gastrocrm-backend#get-apiget-dishid) | done |
|`GET`   | [`/api/get-menu/<id>`](https://github.com/Praca-Inzynierska-CDV/gastrocrm-backend#get-apiget-menuid) | done |
|`GET`   | [`/api/get-all-menu`](https://github.com/Praca-Inzynierska-CDV/gastrocrm-backend#get-apiget-menuid) | done |
|`GET`   | [`/api/get-allergen/<id>`](https://github.com/Praca-Inzynierska-CDV/gastrocrm-backend#get-apiget-allergenid) | done |
|`GET`   | [`/api/get-allergens`](https://github.com/Praca-Inzynierska-CDV/gastrocrm-backend#get-apiget-allergens) | done |
|`GET`   | [`/api/get-active-menu`](https://github.com/Praca-Inzynierska-CDV/gastrocrm-backend#get-apiget-active-menu) | done |
|`GET`   | [`/api/get-get-invoice/<id>`](https://github.com/Praca-Inzynierska-CDV/gastrocrm-backend#get-apiget-invoiceid) | done |
|`GET`   | [`/api/get-get-break-time`](https://github.com/Praca-Inzynierska-CDV/gastrocrm-backend#get-apiget-break-time) | done |
|`GET`   | [`/api/get-holidays`](https://github.com/Praca-Inzynierska-CDV/gastrocrm-backend#get-apiget-holidays) | done |
|`GET`   | [`/api/get-holiday/<username>`](https://github.com/Praca-Inzynierska-CDV/gastrocrm-backend#get-apiget-holidayusername) | done |
|`GET`   | [`/api/get-worktime-statistics`](https://github.com/Praca-Inzynierska-CDV/gastrocrm-backend#get-apiget-worktime-statistics) | done |
|`GET`   | [`/api/get-sales-statistics`](https://github.com/Praca-Inzynierska-CDV/gastrocrm-backend#get-apiget-sales-statistics) | done |
|`GET`   | [`/api/get-waiter-sales-statistics/<id>`](https://github.com/Praca-Inzynierska-CDV/gastrocrm-backend#get-apiget-waiter-sales-statisticsid) | to do |
|`POST`  | [`/api/login`](https://github.com/Praca-Inzynierska-CDV/gastrocrm-backend#post-apilogin) | done |
|`POST`  | [`/api/forgot_password`](https://github.com/Praca-Inzynierska-CDV/gastrocrm-backend#post-apiforgot-password) | done |
|`POST`  | [`/api/add-unavailability`](https://github.com/Praca-Inzynierska-CDV/gastrocrm-backend#put-apiadd-unavailability) | done |
|`PUT`   | [`/api/create-account`](https://github.com/Praca-Inzynierska-CDV/gastrocrm-backend#put-apicreate-account) | done |
|`PUT`   | [`/api/add-user`](https://github.com/Praca-Inzynierska-CDV/gastrocrm-backend#put-apiadd-user) | done |
|`PUT`   | [`/api/add-dish`](https://github.com/Praca-Inzynierska-CDV/gastrocrm-backend#put-apiadd-dish) | done |
|`PUT`   | [`/api/add-menu`](https://github.com/Praca-Inzynierska-CDV/gastrocrm-backend#put-apiadd-menu) | done |
|`PUT`   | [`/api/add-working-time`](https://github.com/Praca-Inzynierska-CDV/gastrocrm-backend#put-apiadd-working-time) | done |
|`PUT`   | [`/api/add-break-time`](https://github.com/Praca-Inzynierska-CDV/gastrocrm-backend#put-apiadd-break-time) | done |
|`PUT`   | [`/api/add-holiday`](https://github.com/Praca-Inzynierska-CDV/gastrocrm-backend#put-apiadd-holiday) | done |
|`PUT`   | [`/api/add-order`](https://github.com/Praca-Inzynierska-CDV/gastrocrm-backend#put-apiadd-order) | done |
|`PATCH` | [`/api/change-password/<username>`](https://github.com/Praca-Inzynierska-CDV/gastrocrm-backend#patch-apichange-passwordusername) | done |
|`PATCH` | [`/api/edit-user/<username>`](https://github.com/Praca-Inzynierska-CDV/gastrocrm-backend#patch-apiedit-userusername) | done |
|`PATCH` | [`/api/edit-dish/<id>`](https://github.com/Praca-Inzynierska-CDV/gastrocrm-backend#patch-apiedit-dishid) | done |
|`PATCH` | [`/api/edit-menu/<id>`](https://github.com/Praca-Inzynierska-CDV/gastrocrm-backend#patch-apiedit-menuid) | done |
|`PATCH` | [`/api/edit-order/<id>`](https://github.com/Praca-Inzynierska-CDV/gastrocrm-backend#put-apiedit-orderid) | done |
|`PATCH` | [`/api/summary-order/<id>`](https://github.com/Praca-Inzynierska-CDV/gastrocrm-backend#put-apiedit-orderid) | done |
|`PATCH` | [`/api/edit-break-time/<id>`](https://github.com/Praca-Inzynierska-CDV/gastrocrm-backend#patch-apiedit-break-timeid) | done |
|`PATCH` | [`/api/edit-holiday/<id>`](https://github.com/Praca-Inzynierska-CDV/gastrocrm-backend#patch-apiedit-holidayid) | done |
|`PATCH` | [`/api/pay-order/<id>`](https://github.com/Praca-Inzynierska-CDV/gastrocrm-backend#patch-apipay-order) | done |
|`DELETE`| [`/api/delete-user/<id>`](https://github.com/Praca-Inzynierska-CDV/gastrocrm-backend#delete-apidelete-userusername) | done |
|`DELETE`| [`/api/delete-dish/<id>`](https://github.com/Praca-Inzynierska-CDV/gastrocrm-backend#delete-apidelete-dishid)  | done |
|`DELETE`| [`/api/delete-menu/<id>`](https://github.com/Praca-Inzynierska-CDV/gastrocrm-backend#delete-apidelete-menuid) | done |
|`DELETE`| [`/api/delete-break-time/<id>`](https://github.com/Praca-Inzynierska-CDV/gastrocrm-backend#delete-apidelete-break-timeid) | done |
|`DELETE`| [`/api/delete-holiday/<id>`](https://github.com/Praca-Inzynierska-CDV/gastrocrm-backend#delete-apidelete-holidayid) | done |
|`DELETE`| [`/api/delete-order/<id>`](https://github.com/Praca-Inzynierska-CDV/gastrocrm-backend#delete-apidelete-orderid) | done |
<!-- |`GET`   | [`/api/get-category`](https://github.com/Praca-Inzynierska-CDV/gastrocrm-backend#get-apiget-category) | done | -->
<!-- |`PUT`   | [`/api/add-dish-to-menu/<id>`](https://github.com/Praca-Inzynierska-CDV/gastrocrm-backend#put-apiadd-dish-to-menuid) | to test | -->
<!-- |`PUT`   | [`/api/add-category`](https://github.com/Praca-Inzynierska-CDV/gastrocrm-backend#put-apiadd-category) | done | -->
<!-- |`PATCH` | [`/api/edit-working-time/<id>`](https://github.com/Praca-Inzynierska-CDV/gastrocrm-backend#patch-apiedit-menuid) | to test | -->
<!-- |`DELETE`| [`/api/delete-category/<name>`](https://github.com/Praca-Inzynierska-CDV/gastrocrm-backend#delete-apidelete-categoryname) | done | -->
<!-- |`DELETE`| [`/api/delete-dish-from-menu/<id>`](https://github.com/Praca-Inzynierska-CDV/gastrocrm-backend#delete-apidelete-dish-from-menuid) | to test | -->


## Uruchaminie aplikacji

Przed uruchomieniem aplikacji trzeba zainstalować biblioteki znajdujące się w `requirements.txt`.

Jeśli korzystasz z lokalnej bazy danych to trzeba ją najpierw stworzyć. Pliki do stworzenia bazy danych znajdują się w folderze `db`.

Uruchamiamy plik `app.py`, jeśli uruchamiasz lokalnie to aplikacja uruchamia się na porcie `5000`.

## Akcje REST API

#### GET `/api/health`
<details>
<p>

Stworzony w celu uruchomienia healthcheck kontenera dockerowego, czy aplikacja prawidłowo odpowiada. Odpowiedź zwraca: `OK`
</p>
</details>

#### GET `/api/get-users`
<details>
<p>




Przykładowa odpowiedz:
```json
{
  "status": "success",
  "message": "Lista użytkowników",
  "result": [
    {
      "username": "jan.kowalski",
      "firstName": "Jan",
      "lastName": "Kowalski",
      "email": "admin@gastrocrm.online",
      "role": "administrator",
      "tempPassword": 0
    },
    {
      "username": "anna.manager",
      "firstName": "Anna",
      "lastName": "Manager",
      "email": "a.manager@gastrocrm.online",
      "role": "manager",
      "tempPassword": 1
    }
  ]
}
```
</p>
</details>

#### GET `/api/get-user/<username>`
<details>
<p>

Funkcja zwraca użytkownika o pdamyn `username` lub `email`. Jako `<username>` można podać `email`

Przykładowa odpowiedz:
```json
{
    "status": "success",
    "message": "Użytkownik admin",
    "result": {
        "role": "admin",
        "tempPassword": false,
        "username": "admin",
        "lastName": "Kowalski",
        "email": "ga.an7213@gmail.com",
        "phoneNumber": "123456789",
        "firstName": "Jan",
        "id": 1
    }
}
```
</p>
</details>

#### GET `/api/get-users-by-role/<role>`
<details>
<p>

Funkcja zwraca listę użytkowników posiadających podaną `role`. 

Przykładowa odpowiedz:
```json
{
    "status": "success",
    "message": "Użytkownik admin",
    "result": {
        "role": "admin",
        "tempPassword": false,
        "username": "admin",
        "lastName": "Kowalski",
        "email": "ga.an7213@gmail.com",
        "phoneNumber": "123456789",
        "firstName": "Jan",
        "id": 1
    }
}
```
</p>
</details>

#### GET `/api/get-dishes`
<details>
<p>

Funkcja zwraca listę wszystkich potraw.


Przykładowa odpowiedz:
```json
{
    "status": "success",
    "message": "Pobrano potrawy",
    "result": [
        {
            "category": "Danie glowne",
            "id": 2,
            "name": "Kotlet",
            "price": 30.0,
            "idAllergen": 1
        },
        {
            "category": "Napoje",
            "id": 4,
            "name": "Woda",
            "price": 5.0,
            "idAllergen": 3
        },
        {
            "category": "Napoje",
            "id": 5,
            "name": "Sok jabłkowy",
            "price": 8.5,
            "idAllergen": 4
        }
    ]
}
```
</p>
</details>

#### GET `/api/get-orders`
<details>
<p>

Funkcja zwraca wszystkie zamówienia.

Można również odfiltrować zamówienie dla `waiterId`.
Należy wtedy wykonać zapytanie `/api/get-orders/<id>`.

Przykładowa odpowiedz:
```json
{
    "status": "success",
    "message": "Wszystkie zamówienia",
    "result": [
        {
            "id": 6,
            "status": "new",
            "tableNumber": 3,
            "clientId": 6,
            "waiterId": 6,
            "orderDate": "2022-05-19T18:54:48",
            "invoice": false
        },
        {
            "id": 7,
            "status": "new",
            "tableNumber": 3,
            "clientId": 7,
            "waiterId": 6,
            "orderDate": "2022-05-19T18:55:07",
            "invoice": false
        }
    ]
}
```
</p>
</details>

#### GET `/api/get-order/<id>`
<details>
<p>

Funkcja zwraca zamówienie podanego `id`

Przykładowa odpowiedz:
```json
{
    "status": "success",
    "message": "Zamówienie",
    "result": {
        "order": {
            "id": 6,
            "status": "new",
            "tableNumber": 3,
            "clientId": 6,
            "waiterId": 6,
            "orderDate": "2022-05-19T18:54:48",
            "invoice": false
        },
        "dishes": [
            {
                "dishId": 15,
                "id": 5,
                "price": 32.5,
                "orderId": 6
            },
            {
                "dishId": 19,
                "id": 6,
                "price": 8.5,
                "orderId": 6
            }
        ]
    }
}
```
</p>
</details>

#### GET `/api/get-dish/<id>`
<details>
<p>

Funkcja zwraca potrawę o podanym `id`.

Przykładowa odpowiedz:
```json
{
    "status": "success",
    "message": "Pobrano potrawę",
    "result": {
        "id": 2,
        "idAllergen": 1,
        "price": 30.0,
        "name": "Kotlet",
        "category": "Danie glowne"
    }
}
```
</p>
</details>

#### GET `/api/get-menu/<id>`
<details>
<p>

Funkcja zwraca menu o podanym `id`.

Przykładowa odpowiedz:
```json
{
    "status": "success",
    "message": "Menu",
    "result": {
        "menu": {
            "menuTo": "2022-12-22T00:00:00",
            "idDishDay": 4,
            "title": "Zimowe",
            "id": 2,
            "menuFrom": "2022-09-23T00:00:00",
            "active": true,
            "idMenuList": 2
        },
        "dishOnTheMenu": [ 3, 24, 5, 8, 10, 12, 45 ]
    }
}
```
</p>
</details>

#### GET `/api/get-all-menu`
<details>
<p>

Funkcja zwraca listę menu.

Przykładowa odpowiedz:
```json
{
    "status": "success",
    "message": "Pobrano menu",
    "result": [
        {
            "idDishDay": 2,
            "menuTo": "2022-06-24T00:00:00",
            "idMenuList": 2,
            "menuFrom": "2022-03-21T00:00:00",
            "title": "Wiosenne",
            "id": 3,
            "active": true
        },
        {
            "idDishDay": 2,
            "menuTo": "2022-06-24T00:00:00",
            "idMenuList": 3,
            "menuFrom": "2022-03-21T00:00:00",
            "title": "Wiosenne",
            "id": 4,
            "active": true
        },
        {
            "idDishDay": 4,
            "menuTo": "2022-06-24T00:00:00",
            "idMenuList": 3,
            "menuFrom": "2022-03-21T00:00:00",
            "title": "Wiosenne",
            "id": 5,
            "active": true
        }
    ]
}
```
</p>
</details>

#### GET `/api/get-allergen/<id>`
<details>
<p>

Funkcja zwraca informacje o tym jakie alergeny są w potrawie po podaniu `id`.

Przykładowa odpowiedz:
```json
{
    "status": "success",
    "message": "Pobrano alergen",
    "result": {
        "shellfish": false,
        "id": 1,
        "fish": false,
        "sesame": true,
        "lactose": false,
        "hazelnuts": true,
        "gluten": false,
        "nuts": true,
        "lupin": false,
        "molluscs": false,
        "sulfate": false,
        "eggs": false,
        "mustard": false,
        "soya": false,
        "celery": false
    }
}
```
</p>
</details>

#### GET `/api/get-allergens`
<details>
<p>

Funkcja zwraca listę alergenów jakie są w potrawach.

Przykładowa odpowiedz:
```json
{
    "status": "success",
    "message": "Pobrano alergeny",
    "result": [
        {
            "shellfish": false,
            "id": 1,
            "fish": false,
            "sesame": true,
            "lactose": false,
            "hazelnuts": true,
            "gluten": false,
            "nuts": true,
            "lupin": false,
            "molluscs": false,
            "sulfate": false,
            "eggs": false,
            "mustard": false,
            "soya": false,
            "celery": false
        },
        {
            "shellfish": false,
            "id": 3,
            "fish": false,
            "sesame": false,
            "lactose": false,
            "hazelnuts": false,
            "gluten": false,
            "nuts": false,
            "lupin": false,
            "molluscs": false,
            "sulfate": false,
            "eggs": false,
            "mustard": false,
            "soya": false,
            "celery": false
        },
        {
            "shellfish": false,
            "id": 4,
            "fish": false,
            "sesame": false,
            "lactose": false,
            "hazelnuts": false,
            "gluten": false,
            "nuts": false,
            "lupin": false,
            "molluscs": false,
            "sulfate": false,
            "eggs": false,
            "mustard": false,
            "soya": false,
            "celery": false
        }
    ]
}
```
</p>
</details>

#### GET `/api/get-active-menu`
<details>
<p>

Funkcja zwraca listę aktywnych menu. Gdzie wartość `active == True`.

Przykładowa odpowiedz:
```json
{
    "status": "success",
    "message": "Aktywne menu",
    "result": [
        {
            "menuFrom": "2022-09-23T00:00:00",
            "active": true,
            "id": 3,
            "title": "Zimowe",
            "menuTo": "2022-12-22T00:00:00",
            "idDishDay": 14,
            "idMenuList": 3
        },
        {
            "menuFrom": "2022-03-23T00:00:00",
            "active": true,
            "id": 4,
            "title": "Wiosenne",
            "menuTo": "2022-06-22T00:00:00",
            "idDishDay": 16,
            "idMenuList": 4
        },
        {
            "menuFrom": "2022-03-23T00:00:00",
            "active": true,
            "id": 6,
            "title": "Blabla",
            "menuTo": "2022-06-22T00:00:00",
            "idDishDay": 16,
            "idMenuList": 6
        }
    ]
}
```
</p>
</details>

#### GET `/api/get-invoice/<id>`
<details>
<p>

Funkcja zwracająca dane do przesłania do faktury. Dodaje informację w bazie o wystawieniu faktury.

Przykładowa odpowiedz:
```json
{
    "status": "success",
    "message": "Przesyłam zamówienie do faktury, uzupełnij o dane klienta",
    "result": { 
        "id": 9,
        "waiterId": 6,
        "status": "new",
        "tableNumber": 3,
        "clientId": 8,
        "invoice": "678563450",
        "orderDate": "2022-05-19T22:50:26"
    }
}
```
</p>
</details>

#### GET `/api/get-break-time`
<details>
<p>

Funkcja zwraca informacje o długości przerwy kelnerskiej.

Przykładowa odpowiedz:
```json
{
    "status": "success",
    "message": "Przerwy kelnerskie",
    "result": [
        {
            "id": 3,
            "time": 30
        }
    ]
}
```
</p>
</details>

#### GET `/api/get-holidays`
<details>
<p>

Funkcja zwraca informacje na temat wszystkich wniosków o urlop.

Przykładowa odpowiedz:
```json
{
    "status": "success",
    "message": "Urlopy",
    "result": [
        {
            "id": 1,
            "status": "accept",
            "timeEnd": "2022-04-28",
            "timeStart": "2022-04-21",
            "workerId": 3
        }
    ]
}
```
</p>
</details>

#### GET `/api/get-holiday/<username>`
<details>
<p>

Funkcja zwraca informacje o wnioskach o urlop pracownika o podanym `username`.

Przykładowa odpowiedz:
```json
{
    "status": "success",
    "message": "Urlopy pracownika Jan Kowalski",
    "result": [
        {
            "id": 1,
            "status": "accept",
            "timeEnd": "2022-04-28",
            "timeStart": "2022-04-21",
            "workerId": 6
        }
    ]
}
```
</p>
</details>

#### POST `/api/get-worktime-statistics`
<details>
<p>

Funkcja zwraca statystyki pracy wszystkich pracowników. Można przesłać w body reqesta `from` i `to` w formacie `YYYY-MM-DD`.
Jeśli nie przesyłane sa daty należy przesłać pusty obiekt. Wtedy zwracane są statystyki z całego okresu.

Przykładowy objekt JSON:
```json
{
    "from": "2022-04-21",
    "to": "2022-04-28"
}
```

Przykładowa odpowiedz:
```json
{
    "status": "success",
    "message": "Statistics work time",
    "result": [
        {
            "userId": 1,
            "username": "admin",
            "firstName": "Administrator",
            "lastName": "Testowy",
            "worktime": "8:00:00"
        },
        {
            "userId": 2,
            "username": "admin2",
            "firstName": "Administrator2",
            "lastName": "Testowy2",
            "worktime": "16:00:00"
        },
        {
            "userId": 6,
            "username": "kelner",
            "firstName": "Konto",
            "lastName": "Kelnera",
            "worktime": "0:00:00"
        },
        {
            "userId": 7,
            "username": "manager",
            "firstName": "Manger",
            "lastName": "Pierwszy",
            "worktime": "0:00:00"
        }
    ]
}
```
</p>
</details>

#### POST `/api/get-worktime-statistics/<id>`
<details>
<p>

Funkcja zwraca statystyki pracy pracownika o podanym `id`. Można przesłać w body reqesta `from` i `to` w formacie `YYYY-MM-DD`.
Jeśli nie przesyłane sa daty należy przesłać pusty obiekt. Wtedy zwracane są statystyki z całego okresu.

Przykładowy objekt JSON:
```json
{
    "from": "2022-04-21",
    "to": "2022-04-28"
}
```

Przykładowa odpowiedz:
```json
{
    "status": "success",
    "message": "Statistics work time",
    "result": [
        {
            "userId": 1,
            "username": "admin",
            "firstName": "Administrator",
            "lastName": "Testowy",
            "worktime": "8:00:00"
        }
    ]
}
```
</p>
</details>

#### POST `/api/get-sales-statistics`
<details>
<p>

Funkcja zwraca statystyki sprzedaży potraw wszystkich zamówień . Można przesłać w body reqesta `from` i `to` w formacie `YYYY-MM-DD`.
Jeśli nie przesyłane sa daty należy przesłać pusty obiekt. Wtedy zwracane są statystyki z całego okresu.

Przykładowy objekt JSON:
```json
{
    "from": "2022-04-21",
    "to": "2022-04-28"
}
```

Przykładowa odpowiedz:
```json
{
    "status": "success",
    "message": "Statistics sales",
    "result": {
        "summarySales": 388.5,
        "sales": [
            {
                "orderId": 6,
                "tableNumber": 3,
                "status": "paid",
                "totalSales": 41.0,
                "orders": [
                    {
                        "disheId": 15,
                        "dishName": "Kotlet schabowy",
                        "dishPrice": 32.5
                    },
                    {
                        "disheId": 19,
                        "dishName": "Mirinda",
                        "dishPrice": 8.5
                    }
                ]
            },
            {
                "orderId": 7,
                "tableNumber": 3,
                "status": "new",
                "totalSales": 41.0,
                "orders": [
                    {
                        "disheId": 15,
                        "dishName": "Kotlet schabowy",
                        "dishPrice": 32.5
                    },
                    {
                        "disheId": 19,
                        "dishName": "Mirinda",
                        "dishPrice": 8.5
                    }
                ]
            },
            {
                "orderId": 9,
                "tableNumber": 3,
                "status": "new",
                "totalSales": 41.0,
                "orders": [
                    {
                        "disheId": 15,
                        "dishName": "Kotlet schabowy",
                        "dishPrice": 32.5
                    },
                    {
                        "disheId": 19,
                        "dishName": "Mirinda",
                        "dishPrice": 8.5
                    }
                ]
            },
            {
                "orderId": 22,
                "tableNumber": 0,
                "status": "new",
                "totalSales": 0,
                "orders": []
            },
            {
                "orderId": 28,
                "tableNumber": 0,
                "status": "new",
                "totalSales": 0,
                "orders": []
            },
            {
                "orderId": 29,
                "tableNumber": 0,
                "status": "new",
                "totalSales": 0,
                "orders": []
            },
            {
                "orderId": 30,
                "tableNumber": 4,
                "status": "new",
                "totalSales": 32.5,
                "orders": [
                    {
                        "disheId": 15,
                        "dishName": "Kotlet schabowy",
                        "dishPrice": 32.5
                    }
                ]
            },
            {
                "orderId": 31,
                "tableNumber": 3,
                "status": "new",
                "totalSales": 41.0,
                "orders": [
                    {
                        "disheId": 15,
                        "dishName": "Kotlet schabowy",
                        "dishPrice": 32.5
                    },
                    {
                        "disheId": 19,
                        "dishName": "Mirinda",
                        "dishPrice": 8.5
                    }
                ]
            },
            {
                "orderId": 32,
                "tableNumber": 1,
                "status": "new",
                "totalSales": 76.5,
                "orders": [
                    {
                        "disheId": 15,
                        "dishName": "Kotlet schabowy",
                        "dishPrice": 32.5
                    },
                    {
                        "disheId": 19,
                        "dishName": "Mirinda",
                        "dishPrice": 8.5
                    },
                    {
                        "disheId": 14,
                        "dishName": "Kotlet sojowy",
                        "dishPrice": 35.5
                    }
                ]
            },
            {
                "orderId": 33,
                "tableNumber": 1,
                "status": "new",
                "totalSales": 115.5,
                "orders": [
                    {
                        "disheId": 15,
                        "dishName": "Kotlet schabowy",
                        "dishPrice": 32.5
                    },
                    {
                        "disheId": 14,
                        "dishName": "Kotlet sojowy",
                        "dishPrice": 35.5
                    },
                    {
                        "disheId": 16,
                        "dishName": "Kotlet drobiowy",
                        "dishPrice": 30.5
                    },
                    {
                        "disheId": 19,
                        "dishName": "Mirinda",
                        "dishPrice": 8.5
                    },
                    {
                        "disheId": 20,
                        "dishName": "7up",
                        "dishPrice": 8.5
                    }
                ]
            }
        ]
    }
}
```
</p>
</details>

#### POST `/api/get-waiter-sales-statistics/<id>`
<details>
<p>

Funkcja do zrobienia.

Funkcja zwraca statystyki sprzedaży potraw wszystkich zamówień kelnera o danym `id` . Można przesłać w body reqesta `from` i `to` w formacie `YYYY-MM-DD`.
Jeśli nie przesyłane sa daty należy przesłać pusty obiekt. Wtedy zwracane są statystyki z całego okresu.

Przykładowy objekt JSON:
```json
{
    "from": "2022-04-21",
    "to": "2022-04-28"
}
```

Przykładowa odpowiedz:
```json
{
    "status": "success",
    "message": "kelner waiter's sales statistics",
    "result": {
        "waiterSummarySales": 164.0,
        "sales": [
            {
                "orderId": 6,
                "tableNumber": 3,
                "status": "paid",
                "totalSales": 41.0,
                "orders": [
                    {
                        "disheId": 15,
                        "dishName": "Kotlet schabowy",
                        "dishPrice": 32.5
                    },
                    {
                        "disheId": 19,
                        "dishName": "Mirinda",
                        "dishPrice": 8.5
                    }
                ]
            },
            {
                "orderId": 7,
                "tableNumber": 3,
                "status": "new",
                "totalSales": 41.0,
                "orders": [
                    {
                        "disheId": 15,
                        "dishName": "Kotlet schabowy",
                        "dishPrice": 32.5
                    },
                    {
                        "disheId": 19,
                        "dishName": "Mirinda",
                        "dishPrice": 8.5
                    }
                ]
            },
            {
                "orderId": 9,
                "tableNumber": 3,
                "status": "new",
                "totalSales": 41.0,
                "orders": [
                    {
                        "disheId": 15,
                        "dishName": "Kotlet schabowy",
                        "dishPrice": 32.5
                    },
                    {
                        "disheId": 19,
                        "dishName": "Mirinda",
                        "dishPrice": 8.5
                    }
                ]
            },
            {
                "orderId": 31,
                "tableNumber": 3,
                "status": "new",
                "totalSales": 41.0,
                "orders": [
                    {
                        "disheId": 15,
                        "dishName": "Kotlet schabowy",
                        "dishPrice": 32.5
                    },
                    {
                        "disheId": 19,
                        "dishName": "Mirinda",
                        "dishPrice": 8.5
                    }
                ]
            }
        ]
    }
}
```
</p>
</details>

#### POST `/api/login`
<details>
<p>

Funkcja logująca użytkownika. W przypadku poprawnego logowania zwraca token.

Logowanie można wykonać poprzez podanie w JSONie wartości `username` lub `email` oraz `password`.

Przykładowy wymagany objekt JSON zapytania:
```json
{
    "username": "jan.kowalski",
    "password": "haslo123"
}
```
Przykładowa odpowiedz:
```json
{
    "status": "success",
    "message": "Zalogowanio użytkonika admin",
    "result": {
        "id": 1,
        "firstName": "Jan",
        "lastName": "Kowalski",
        "role": "admin",
        "token": "eyJ0eXAiOiJKV1QiLCJhbGcdasdiOiJIUzI1NiJ9.eyJ0b2tlbiI6ImoxQ2liaGpLNdISXAzYzR6VG52QTZQbEJrdlJCWDBDIn0.V8jzA-caYBc-5Lhw-EYwDi8OUNS0XHoJ8M_xVwaLW9k"
    }
}
```
</p>
</details>


#### POST `/api/forgot-password`
<details>
<p>

Funkcja wysyłająca maila z linkiem do resetowania hasła. W przypadku poprawnego wysłania maila zwraca status `success`.

Przykładowy wymagany objekt JSON zapytania:
```json
{
    "email": "jan.kowalski@gastrocmr.online",
}
```
Odpowiedz:
```json
{
    "status": "success",
    "message": "Wysłano wiadomość z hasłem tymczasowym na adres admin@gastrocrm.online",
    "result": "admin@gastrocrm.online"
}
```
</p>
</details>


#### POST `/api/add-unavailability`
<details>
<p>

Funkcja przesyła podaną datę i powód niedostęności do managera na adres email przechowywany w bazie.

Przykładowy wymagany objekt JSON zapytania:
```json
{
   "username": "kelner",
   "startDate": "2022-04-21T00:00:00.000",
   "endDate": "2022-04-21T00:00:00.000",
   "reason": "Złamna ręka"
}
```
</p>
</details>

#### PUT `/api/add-user`
<details>
<p>

Funkcja dodająca użytkownika. W przypadku poprawnego dodania zwraca status `success`.

Przykładowy wymagany objekt JSON zapytania:
```json
{
    "username": "jan.kowalski",
    "firstName": "Jan",
    "lastName": "Kowalski",
    "phoneNumber": "123456789",
    "email": "jan.kowalski@gastrocrm.online",
    "role": "admin"
}
```
</p>
</details>

#### PUT `/api/create-account`
<details>
<p>

Funkcja dodająca użytkownika. W przypadku poprawnego dodania zwraca status `success`.

`/api/create-account` jest nie zabezpieczona tokenem forma dodawania **pierwszego** użytkownika.
Przykładowy wymagany objekt JSON zapytania:
```json
{
    "username": "jan.kowalski",
    "firstName": "Jan",
    "lastName": "Kowalski",
    "phoneNumber": "123456789",
    "email": "jan.kowalski@gastrocrm.online",
    "role": ""
}
```
</p>
</details>

#### PUT `/api/add-dish`
<details>
<p>

Funkcja dodająca potrawę. W przypadku poprawnego dodania zwraca status `success`.

Przykładowy wymagany objekt JSON zapytania:
```json
{
    "name": "Sok pomarańczowy",
    "price": "8.50",
    "category": "Napoje",
    "gluten" : 0,
    "lactose" : 0,
    "eggs" : 0,
    "fish" : 0,
    "shellfish" : 0,
    "nuts" : 0,
    "hazelnuts" : 0,
    "soya" : 0,
    "sesame" : 0,
    "sulfate" : 0,
    "mustard" : 0,
    "lupin" : 0,
    "celery" : 0,
    "molluscs" : 0
}

```
</p>
</details>


<!-- #### PUT `/api/add-category`
<details>
<p>

Funkcja dodająca kategorię. W przypadku poprawnego dodania zwraca status `success`.

Przykładowy wymagany objekt JSON zapytania:
```json
{
    "name": "Danie główne"
}
```
</p>
</details> -->


#### PUT `/api/add-menu`
<details>
<p>

Funkcja dodająca menu. W przypadku poprawnego dodania zwraca status `success`.

Przykładowy wymagany objekt JSON zapytania:
```json
{
    "title": "Zimowe",
    "active": 1,
    "menuFrom": "2022-09-23",
    "menuTo": "2022-12-22",
    "idDishDay": 4,
    "dishOnTheMenu": [3, 24, 5, 8, 10, 12, 45]
}
```
</p>
</details>

#### PUT `/api/add-working-time`
<details>
<p>

Funkcja dodaje czas pracy pracownika do bazy

Przykładowy wymagany objekt JSON zapytania:
```json
{
   "username": "admin2",
   "timeStart": "2022-04-21T07:00:00.000",
   "timeEnd": "2022-04-21T15:00:00.000"
}
```
</p>
</details>

#### PUT `/api/add-break-time`
<details>
<p>

Funkcja definiująca długość przerwy.

Przykładowy wymagany objekt JSON zapytania:
```json
{
   "time": 30
}
```
</p>
</details>

#### PUT `/api/add-holiday`
<details>
<p>

Funkcja do składania wniosku o urlop. Przesyła ona informację do mangera na adres email przechowywany w bazie

Przykładowy wymagany objekt JSON zapytania:
```json
{
    "username": "kelner",
    "timeStart": "2022-04-21",
    "timeEnd": "2022-04-28",
    "reason": "Nie mogę pracować"
}
```
</p>
</details>

#### PUT `/api/add-order`
<details>
<p>

Funkcja dodaje zamawiane danie do zamówienia.

Przykładowy wymagany objekt JSON zapytania:
```json
{
    "waiterId": 6,
    "tableNumber": 3,
    "invoice": 5674563212,
    "orderedDishes": [15,19,15,19]
}
```

Zwracana wartość:
```json
{
    "status": "success",
    "message": "Dodano produkt do zamówienia",
    "result": {
        "order": {
            "waiterId": 6,
            "status": "new",
            "orderDate": "2022-05-19T19:07:14",
            "invoice": 5674563212,
            "id": 8,
            "tableNumber": 3,
            "clientId": 8
        },
        "dishes": [
            {
                "dishId": 15,
                "name": "Kotlet schabowy",
                "number": 2,
                "price_per_dish": 32.5,
                "price_summary": 65.0
            },
            {
                "dishId": 19,
                "name": "Mirinda",
                "number": 2,
                "price_per_dish": 8.5,
                "price_summary": 17.0
            }
        ]
    }
}
```
</p>
</details>

<!-- #### PUT `/api/add-dish-to-menu/<id>`
<details>
<p>

Funkcja niegotowa.

Przykładowy wymagany objekt JSON zapytania:
```json
{
    "dishNumber": 1,
    "dishOnTheMenu": 4
}
```
</p>
</details> -->

#### PATCH `/api/change-password/<username>`
<details>
<p>

Zmienia hasło podanego użytkownika (`username`). W przypadku poprawnego zmiany zwraca status `success`.

Przykładowy wymagany objekt JSON zapytania:
```json
{
    "password": "haslo123",
    "new_password": "password321"
}
```

Odpowiedź:
```json
{
    "status": "success",
    "message": "Hasło uzytkownika admin zostało zmienione",
    "result": []
}
```
</p>
</details>


#### PATCH `/api/edit-user/<username>`
<details>
<p>

Pozwala edytować dane użytkownika o podanym `username`. W przypadku poprawnego edycji zwraca status `success`.

W obiekcie JSON można podać tylko jedną wartość do zmiany.

Przykładowy wymagany objekt JSON zapytania:
```json
{
    "firstName": "Jan",
    "lastName": "Kowalski",
    "phoneNumber": "123456789",
    "email": "jan.kowalski@gastrocrm.online",
    "role": "admin"
}
```
</p>
</details>

#### PATCH `/api/edit-dish/<id>`
<details>
<p>

Funkcja pozwala edytować dane potrawy o podanym `id`. W przypadku poprawnego edycji zwraca status `success`.

W obiekcie JSON można podać tylko jedną wartość do zmiany.

Przykładowy wymagany objekt JSON zapytania:
```json
{
    "name": "Sok jabłkowy",
    "price": "8.50",
    "category": "Napoje",
    "gluten" : 0,
    "lactose" : 0,
    "eggs" : 0,
    "fish" : 0,
    "shellfish" : 0,
    "nuts" : 0,
    "hazelnuts" : 0,
    "soya" : 0,
    "sesame" : 0,
    "sulfate" : 0,
    "mustard" : 0,
    "lupin" : 0,
    "celery" : 0,
    "molluscs" : 0
}
```
</p>
</details>

#### PATCH `/api/edit-menu/<id>`
<details>
<p>

Funkcja edytuje dane menu o podanym `id`. W przypadku poprawnego edycji zwraca status `success`.

W obiekcie JSON można podać tylko jedną wartość do zmiany.

Przykładowy wymagany objekt JSON zapytania:
```json
{
    "title": "Zimowe",
    "active": 1,
    "menuFrom": "2022-12-23",
    "menuTo": "2022-03-22",
    "idDishDay": 5,
    "idMenuList": 2
}
```
</p>
</details>

#### PATCH `/api/edit-order/<id>`
<details>
<p>

Funkcja edytuje istniejące zamówienie. Pozwala na dodawanie lub odejmowanie dań.

W obiekcie JSON można podać tylko jedną wartość do zmiany.

Przykładowy wymagany objekt JSON zapytania:
```json
{
    "tableNumber": 3,
    "waiterId": 7,
    "status": "in progress",
    "orderedDishes": [15,20]
}
```

Przykładowa zwracana wardość:
```json
{
    "status": "success",
    "message": "Edytowano zamówienie",
    "result": {
        "order": {
            "tableNumber": 3,
            "invoice": false,
            "orderDate": "2022-05-19T18:46:55",
            "clientId": 5,
            "id": 5,
            "waiterId": 7,
            "status": "in progress"
        },
        "dishes": [
            {
                "dishId": 15,
                "name": "Kotlet schabowy",
                "number": 1,
                "price_per_dish": 32.5,
                "price_summary": 32.5
            },
            {
                "dishId": 20,
                "name": "7up",
                "number": 1,
                "price_per_dish": 8.5,
                "price_summary": 8.5
            }
        ]
    }
}
```
</p>
</details>

#### PATCH `/api/summary-order/<id>`
<details>
<p>

Funkcja zwraca podsumowaną wartość zamówienia

W obiekcie JSON można podać tylko jedną wartość do zmiany.

Przykładowa zwracana wardość:
```json
{
    "status": "success",
    "message": "Podsumowanie zamówienia",
    "result": {
        "id": "6",
        "summary": 41.0,
        "dishes": [
            {
                "dishId": 15,
                "name": "Kotlet schabowy",
                "number": 1,
                "price_per_dish": 32.5,
                "price_summary": 32.5
            },
            {
                "dishId": 19,
                "name": "Mirinda",
                "number": 1,
                "price_per_dish": 8.5,
                "price_summary": 8.5
            }
        ]
    }
}
```
</p>
</details>

<!-- #### PATCH `/api/edit-working-time`
<details>
<p>

Funkcja do zmian w czasie pracy pracownika. Zwraca informację o udanej akcji

Przykładowy wymagany objekt JSON zapytania:
```json
{
    "username": "admin",
    "timeStart": "2022-04-21T00:00:00.000",
    "timeEnd": "2022-04-21T00:00:00.000"
}
```
</p>
</details> -->

#### PATCH `/api/edit-break-time/<id>`
<details>
<p>

Funkcja do zmiany długość przerwy. Zwraca informację o udanej akcji

Przykładowy wymagany objekt JSON zapytania:
```json
{
   "time": 45
}
```
</p>
</details>

#### PATCH `/api/edit-break-time/<id>`
<details>
<p>

Funkcja do aktualizacji statusu wniosku przez managera. Po zmianie wysyłany jest email do wnioskodawcy z aktualnym statusem.

Przykładowy wymagany objekt JSON zapytania:
```json
{
    "status": "accept"
}
```
</p>
</details>

#### PATCH `/api/pay-order/<id>`
<details>
<p>

Funkcja zapisuje status `paid` po potwierdzeniu płatności.

Przykładowy wymagany objekt JSON zapytania:
```json
{
   "payment_system_response": "OK"
}
```

Przykładowa zwracana wartość:
```json
{
    "status": "success",
    "message": "Zamówienie zostało opłacone",
    "result": {
        "orderDate": "2022-05-19T18:54:48",
        "tableNumber": 3,
        "id": 6,
        "status": "paid",
        "clientId": 6,
        "invoice": false,
        "waiterId": 6
    }
}
```
</p>
</details>

#### PATCH `/api/add-invoice/<id>`
<details>
<p>

Funkcja zapisuje dane do faktury.

Przykładowy wymagany objekt JSON zapytania:
```json
{
   "invoice": 5674563212
}
```

Przykładowa zwracana wartość:
```json
{
    "status": "success",
    "message": "Przesyłam zamówienie do faktury, uzupełnij o dane klienta",
    "result": {
        "status": "new",
        "invoice": "5674563212",
        "id": 1,
        "waiterId": 2,
        "tableNumber": 1,
        "clientId": 1,
        "orderDate": "2022-05-24T16:11:57"
    }
}
```
</p>
</details>

#### DELETE `/api/delete-user/<username>`
<details>
<p>

Funkcja zwraca informację o usunięciu użytkownika o podanym `username`.
```json
{
    "status": "success",
    "message": "Użytkownik jan.kowalski został usunięty",
    "result": []
}
```
</p>
</details>

<!-- #### DELETE `/api/delete-category/<name>`
<details>
<p>

Obiekt zwraca informację o usunięciu użytkownika o podanym `name`.
```json
{
    "status": "success",
    "message": "Kategoria została usunięta",
    "result": []
}
```
</p>
</details> -->

#### DELETE `/api/delete-dish/<id>`
<details>
<p>

Funkcja zwraca informację o usunięciu potrawy o podanym `id`.
```json
{
    "status": "success",
    "message": "Potrawa została usunięta",
    "result": []
}
```
</p>
</details>

<!-- #### DELETE `/api/delete-dish-from-menu/<id>`
<details>
<p>

Funkcja usuwająca zamówione potrawy z zamówienia.

Obiekt zwraca informację o usunięciu użytkownika o podanym `id`.
```json
{
    "status": "success",
    "message": "Usunięto danie z zamówienia",
    "result": []
}
```
</p>
</details> -->

#### DELETE `/api/delete-menu/<id>`
<details>
<p>

Funkcja usuwająca menu.

Zwracany jest obiekt JSON z informacjami usuniętymi o menu o podanym `id`.
```json
{
    "status": "success",
    "message": "Usunięto menu",
    "result": {
        "menuFrom": "2022-03-21T00:00:00",
        "active": true,
        "title": "Wiosenne",
        "idMenuList": 3,
        "id": 4,
        "menuTo": "2022-06-24T00:00:00",
        "idDishDay": 2
    }
}
```
</p>
</details>

#### DELETE `/api/delete-break-time/<id>`
<details>
<p>

Funkcja usuwa zdefiniowany czas przerwy kelnerskiej.

Obiekt zwraca informację o usunięciu `break-time` o podanym `id`.
```json
{
    "status": "success",
    "message": "",
    "result": "Przerwa kelnerska została usunięta"
}
```
</p>
</details>

#### DELETE `/api/delete-holiday/<id>`
<details>
<p>

Funkcja usuwa wniosek o urlop.

Obiekt zwraca informację o usunięciu wniosku.
```json
{
    "status": "success",
    "message": "Urlop został usunięty",
    "result": {
        "id": 2,
        "status": "accept",
        "timeEnd": "2022-04-28",
        "timeStart": "2022-04-21",
        "workerId": 3
    }
}
```
</p>
</details>

#### DELETE `/api/delete-order/<id>`
<details>
<p>

Funkcja usuwa zamówienie z bazy.

Obiekt zwraca informację o usunięciu zamówienia o podanym `id`.
```json
{
    "status": "success",
    "message": "",
    "result": "Przerwa kelnerska została usunięta"
}
```
</p>
</details>
