import logging
import json
import requests
from lib.openaiutils import openai_get_authenticated_client, get_openai_models

logger = logging.getLogger(__name__)

_CHAT_MSGS=[
    {
        "role": "system",
        "content": '''Masz za zadanie skrócić opis osoby by był trzy razy krótszy. Mozesz usuwać ozdowniki ale musisz zachować wszystkie informacje. Mozesz zmienić kolejność, ale musisz zachować informacje o zainteresowaniach i róznych szczegółach. Nie pomijaj nazw ulubionych filmów, tańców hobby itd. Opis nie musi być gramatycznie poprawny, Moesz po prostu przygotować listę faktów na temat osoby.
        
        Zwróć przygotowany opis i nic więcej. Opis będzie wykorzystywany jako baza danych dla innego modelu, który ma niewielki kontekst.
'''
    }
]

def get_answer(task_details_response: dict):
    logger.info("Solving lesson 2 week 5 task blogger")

    client = openai_get_authenticated_client()
    models = get_openai_models()

    logger.debug(task_details_response)

    database = requests.get("https://tasks.aidevs.pl/data/3friends.json").json()
    zygfryd = " ".join(database['zygfryd'])
    stefan = " ".join(database['stefan'])
    ania = " ".join(database['ania'])

    # Zygfryd
    system_json_data = _CHAT_MSGS
    user_json_data = {
        "role": "user",
        "content": zygfryd
    }
    system_json_data.append(user_json_data)
 
    zygfryd_summary = client.chat.completions.create(
        model="gpt-3.5-turbo-16k-0613",
        messages=system_json_data,
        temperature=1,
        max_tokens=10000,
        top_p=1
    ).choices[0].message.content

    # Stefan
    system_json_data = _CHAT_MSGS
    user_json_data = {
        "role": "user",
        "content": stefan
    }
    system_json_data.append(user_json_data)
 
    stefan_summary = client.chat.completions.create(
        model="gpt-3.5-turbo-16k-0613",
        messages=system_json_data,
        temperature=1,
        max_tokens=9050,
        top_p=1
    ).choices[0].message.content

    # Ania
    system_json_data = _CHAT_MSGS
    user_json_data = {
        "role": "user",
        "content": ania
    }
    system_json_data.append(user_json_data)
 
    ania_summary = client.chat.completions.create(
        model="gpt-3.5-turbo-16k-0613",
        messages=system_json_data,
        temperature=1,
        max_tokens=8000,
        top_p=1
    ).choices[0].message.content

    print("######")
    print(zygfryd_summary)
    print("######")
    print(stefan_summary)
    print("######")
    print(ania_summary)
    print("######")

    optimal_database = database
    optimal_database['zygfryd'] = [zygfryd_summary]
    optimal_database['stefan'] = [stefan_summary]
    optimal_database['ania'] = [ania_summary]

    print("######")
    print(optimal_database)

    return str(optimal_database)
