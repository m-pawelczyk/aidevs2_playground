import logging

logger = logging.getLogger(__name__)

def get_answer(task_details_response: dict):
    logger.info("We will solve some 1st World problem !")

    	# {'code': 0, 'msg': 'send me definition of function named addUser that require 3 params: name (string), 
        # surname (string) and year of born in field named "year" (integer). Set type of function to "object"', '
        # hint1': "send this definition as correct JSON structure inside 'answer' field (as usual)"}

    function_definition = {
        "name": "addUser",
        "description": "Add user with name, surname and date of birth",
        "parameters": {
            "type": "object",
            "properties": {
                "name": {
                    "type": "string",
                    "description": "Name of user."
                },
                "surname": {
                    "type": "string",
                    "description": "Surname of user."
                },
                "year": {
                    "type": "integer",
                    "description": "Year of birth"
                }
            },
            "required": [
                "type", "tags", "command"
            ]
        }
    }

    logger.info(f"Function definition { function_definition }")

    return function_definition
