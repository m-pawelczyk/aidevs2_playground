Wykonaj zadanie o nazwie functions zgodnie ze standardem zgłaszania odpowiedzi opisanym na tasks.aidevs.pl. Zadanie polega na zdefiniowaniu funkcji o nazwie addUser, która przyjmuje jako parametr obiekt z właściwościami: imię (name, string), nazwisko (surname, string) oraz rok urodzenia osoby (year, integer). Jako odpowiedź musisz wysłać jedynie ciało funkcji w postaci JSON-a. Jeśli nie wiesz, w jakim formacie przekazać dane, rzuć okiem na hinta: https://tasks.aidevs.pl/hint/functions 

```json
{"answer": {
            "name": "orderPizza",
            "description": "select pizza in pizzeria based on pizza name",
            "parameters": {
                "type": "object",
                "properties": {
                    "name": {
                        "type": "string",
                        "description": "provide name of the pizza"
                    }
                }
            }
        }
}
```