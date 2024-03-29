import logging
import requests
from lib.variables import get_environment_variable
from lib.openaiutils import openai_get_authenticated_client, get_openai_models


logger = logging.getLogger(__name__)

def download_file(url, file_path):
    # Send HTTP GET request to download the file
    response = requests.get(url)
    
    # Check if the request was successful
    if response.status_code == 200:
        # Write the response content to the file
        with open(file_path, 'wb') as file:
            file.write(response.content)
        print(f"File downloaded successfully to '{file_path}'")
    else:
        print(f"Failed to download file from '{url}'. Status code: {response.status_code}")

def get_answer(task_details_response: dict):
    client = openai_get_authenticated_client()
    logger.info("Solving lesson 9 task 1")

    models = get_openai_models()

    download_file("https://tasks.aidevs.pl/data/mateusz.mp3", "/Users/michal/Downloads/mateusz.mp3")

    audio_file= open("/Users/michal/Downloads/mateusz.mp3", "rb")    
    transcription = client.audio.transcriptions.create(
        file = audio_file,
        model = models.whisper_1.name
    )

    logger.info(f"OpenAI Response for embedding { transcription.text }")

    return transcription.text
