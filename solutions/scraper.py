import logging
import json
import requests
import time
from lib.openaiutils import openai_get_authenticated_client, get_openai_models

logger = logging.getLogger(__name__)

_CHAT_MSGS=[]

def get_answer(task_details_response: dict):
    logger.info("Solving lesson 4 task blogger")

    client = openai_get_authenticated_client()
    models = get_openai_models()


    system_content_template = '''
    Return answer for the question in POLISH language. Maximum length of your response should have 200 characters. You answer have to be based on this article:

    ARTICLE_TEMPLATE
    '''


    url = task_details_response['input']  # URL of the text file
    max_retries = 5  
    user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.99 Safari/537.36"

    headers = {
        "User-Agent": user_agent
    }

    for retry in range(max_retries):
        response = requests.get(url, timeout=60, headers=headers)
        
        if response.status_code == 200:
            article = response.text
            print("File downloaded successfully")
            break  
        else:
            print(f"Failed to download the file (Status Code: {response.status_code})")
            if retry < max_retries - 1:
                print(f"Retrying in {retry_delay} seconds...")
                time.sleep(retry_delay) 
                retry_delay = retry_delay * 2
            else:
                print("Maximum retries exceeded")


    system_content_template = system_content_template.replace("ARTICLE_TEMPLATE", article)
    system_json_data = {
        "role": "system",
        "content": system_content_template
    }

    user_json_data = {
        "role": "user",
        "content": str(task_details_response['question'])
    }

    _CHAT_MSGS.append(system_json_data)
    _CHAT_MSGS.append(user_json_data)

    print(_CHAT_MSGS)
 
    task_response = client.chat.completions.create(
        model=models.gpt_3_5_turbo.name,
        messages=_CHAT_MSGS,
        temperature=1,
        max_tokens=2000,
        top_p=1
    )

    logger.debug(f"OpenAI Response { task_response }")

    print(task_response.choices[0].message.content)
    return task_response.choices[0].message.content