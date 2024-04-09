import logging
import json
import requests

from datetime import datetime

from lib.openaiutils import openai_get_authenticated_client, get_openai_models

logger = logging.getLogger(__name__)

_CHAT_MSGS=[]

def get_answer(task_details_response: dict):
    logger.info("We will solve some 1st World problem ! - c-04l01")

    client = openai_get_authenticated_client()
    models = get_openai_models()

    today_date = datetime.today().strftime('%Y-%m-%d')
    day_name = datetime.today().strftime('%A')

    print(day_name)

    today_context = "Today is {} in YYYY-MM-DD format and it is {}".format(today_date, day_name)

    system_message = {
        "role": "system",
        "content": '''
            Describe the message as tool of 'ToDo' which or an 'Calendar', and respond with proper JSON object releated to tool.

            tools###
            - "ToDo" will be chosen when a user ask about some task, reminder, but not specify date
            - "Calendar" will be chosen if a user would like to setup some event with specified date or day.

            context###
            TODAY_CONTEXT

            examples###
            Przypomnij mi, że mam kupić mleko
            {"tool":"ToDo","desc":"Kup mleko"}
            'Jutro mam spotkanie z Marianem
            {"tool":"Calendar","desc":"Spotkanie z Marianem","date":"2024-04-10"}
        '''.replace("TODAY_CONTEXT", today_context)
    }

    user_message = {
        "role": "user",
        "content": str({task_details_response['question']})
    }

    _CHAT_MSGS.append(system_message)
    _CHAT_MSGS.append(user_message)

    print(_CHAT_MSGS)

    task_response = client.chat.completions.create(
        model=models.gpt_4_0125_preview.name,
        response_format={"type": "json_object"},
        messages=_CHAT_MSGS,
        temperature=1,
        max_tokens=200,
        top_p=1
    )

    json_task_response = json.loads(task_response.choices[0].message.content)

    print(json_task_response)

    return json_task_response