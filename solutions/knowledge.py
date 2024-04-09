import logging
import json
import requests

from lib.openaiutils import openai_get_authenticated_client, get_openai_models

logger = logging.getLogger(__name__)

_CHAT_MSGS=[]

def get_answer(task_details_response: dict):
    logger.info("We will solve some 1st World problem ! - c-04l01")

    client = openai_get_authenticated_client()
    models = get_openai_models()


    system_message = {
        "role": "system",
        "content": '''
            Help me to set cattegory for following question. You can use one of three cattegories: CURRENCY, POPULATION, OTHER. Respond with JSON which contains category and name of country in English with small letters and cca2 code

            ```Example

            {
                "category": "POPULATION",
                "country": "poland",
                "cca2": "PL"
            }
        '''
    }

    user_message = {
        "role": "user",
        "content": str({task_details_response['question']})
    }

    _CHAT_MSGS.append(system_message)
    _CHAT_MSGS.append(user_message)

    response = client.chat.completions.create(
        model=models.gpt_4_0125_preview.name,
        response_format={"type": "json_object"},
        messages=_CHAT_MSGS,
        temperature=1,
        max_tokens=200,
        top_p=1
    )

    content_json = json.loads(response.choices[0].message.content)
    category = content_json['category']
    cca2 = content_json['cca2']
    print(response)
    print(content_json)
    print(category)

    context = ""
    
    if category == "CURRENCY":
        print("cat CURRENCY")
        context = requests.get("https://api.nbp.pl/api/exchangerates/tables/A/").text
    elif category == "POPULATION":
        print("cat POPULATION")
        url = "https://restcountries.com/v3.1/alpha?codes=" + cca2
        context = requests.get(url).text
    else:
        print("Option 4: This should not happen, something is wrong!")

    print(context)

    if category == "CURRENCY":
        system_message = {
            "role": "system",
            "content": '''
                "Respond shortly in Polish to question in one sentence. Your respond should be based only on following context which contain current currencies rates in comparisson to PLN"

                ```Context
                {context}
            '''
        }
    elif category == "POPULATION":
        system_message = {
            "role": "system",
            "content": '''
                "Respond shortly in Polish to question in one sentence. Your respond should be based only on following context"

                ```Context
                {context}
            '''
        }
    else:
        system_message = {
            "role": "system",
            "content": "Respond shortly to question in one sentence."
        }


    

    user_message = {
        "role": "user",
        "content": str({task_details_response['question']})
    }

    print(system_message)


    _CHAT_MSGS_2 = []
    _CHAT_MSGS_2.append(system_message)
    _CHAT_MSGS_2.append(user_message)

    task_response = client.chat.completions.create(
        model=models.gpt_4_0125_preview.name,
        messages=_CHAT_MSGS_2,
        temperature=1,
        max_tokens=200,
        top_p=1
    )


    print(response)
    return task_response.choices[0].message.content