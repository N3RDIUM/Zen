from logging import INFO

from logger import logger

tool_export = {
    "type": "function",
    "function": {
        "name": "google_search",
        "description": "Search google for anything!",
        "parameters": {
            "type": "object",
            "properties": {
                "query": {
                    "type": "string",
                    "description": "The query to be searched on google.",
                },
            },
            "required": ["message"],
        },
    },
}


def function(args):
    logger.log(
        INFO,
        f"INFO  [ function  ]  Google search requested: {args[list(args.keys())[0]]}",
    )
    logger.log(
        INFO, f"INFO  [ function  ]  Google search returned: {'The answer is: Potato!'}"
    )
    return {
        "role": "tool",
        "content": "Search results: { 'answer`: 'The answer is: Potato!' }",
    }
