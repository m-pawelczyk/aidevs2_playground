import logging

from lib.openaiutils import openai_get_authenticated_client, get_openai_models

logger = logging.getLogger(__name__)

_CHAT_MSGS=[
    {
        "role": "system",
        "content": '''Podaj w języku polskim jaki kolor czapki ma gnom. Jeśli na obrazku nie znajduje się gnom, albo nie ma czapki zwróć ERROR 

        Example###
        user: gnom w czapce czerwonej
        AI:czerwony

        user: coś innego niz gnom w czapce
        AI:ERROR

        user: brak czapki
        AI:ERROR
'''
    }
]

def get_answer(task_details_response: dict):
    logger.info("We will solve some 1st World problem!")
    logger.info("What color of hat has gnome?")


    client = openai_get_authenticated_client()
    models = get_openai_models()

    image_url = task_details_response['url']
    logger.debug(task_details_response['url'])

    user_msg = {
                "role": "user",
                "content": [
                    {
                        "type": "image_url",
                        "image_url": {
                            "url": image_url,
                        },
                    },
                ],
            }
    
    _CHAT_MSGS.append(user_msg)

    response = client.chat.completions.create(
        model="gpt-4-turbo",
        messages=_CHAT_MSGS,
        max_tokens=300,
    )

    color = response.choices[0]
    print(color)

    return str(color)   