import logging
import json
from lib.openaiutils import openai_get_authenticated_client, get_openai_models

logger = logging.getLogger(__name__)

_CHAT_MSGS=[
    {
        "role": "system",
        "content": "md2html"
    }
]


def get_answer(task_details_response: dict):
    logger.info("Solving lesson 24 task md2html")

    client = openai_get_authenticated_client()
    models = get_openai_models()

    user_json_data = {
        "role": "user",
        "content": str(task_details_response['input'])
    }

    _CHAT_MSGS.append(user_json_data)

    print(_CHAT_MSGS)

    task_response = client.chat.completions.create(
        model="ft:gpt-3.5-turbo-0125:personal::9IIydFuD",
        messages=_CHAT_MSGS,
        temperature=1,
        max_tokens=4096,
        top_p=1
    )

    logger.debug(f"OpenAI Response { task_response }")

    answer = task_response.choices[0].message.content
    print(answer)
    return answer
