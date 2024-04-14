import logging

logger = logging.getLogger(__name__)

def get_answer(task_details_response: dict):
    logger.info("We will solve some 1st World problem !")
    logger.info("Trigger openapipro")

    url = "https://hook.eu2.make.com/7ykv62tbo1jb751cgu883e3gjaa1xqjc"
    return url