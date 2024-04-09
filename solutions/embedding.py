import logging
from lib.variables import get_environment_variable
from lib.openaiutils import openai_get_authenticated_client, get_openai_models


logger = logging.getLogger(__name__)

def get_answer(task_details_response: dict):
    client = openai_get_authenticated_client()
    logger.info("Solving lesson 8 task 1")

    models = get_openai_models()

    task_response = client.embeddings.create(
        input="Hawaiian pizza",
        model=models.text_embedding_ada_002.name
    )

    logger.info(f"OpenAI Response for embedding { task_response.data[0].embedding }")

    return task_response.data[0].embedding
    