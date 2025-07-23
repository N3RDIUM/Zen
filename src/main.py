from ollama import ChatResponse, chat
import logging

SYSTEM = """You are a friendly, helpful assistant.
Your name is Copilot. You are to talk to users in a friendly manner.
Also, remember that you are in a realtime environment.
So, you can only spend ONE SENTENCE for thinking purposes.
Your responses will also be short and minimal in one sentence, with no emojis.
"""

def get_time() -> str:
    """
    Returns the current time.

    Args:
        None

    Returns:
        str: the current time in 24-hour format
    """

    return "03:00"

def search_google(query: str) -> list[str]:
    """
    Retrieves results from the Google search engine.

    Args:
        query: str

    Returns:
        list[str]: Search results
    """

    return [
        "The meaning of life",
        "Hitchhiker's Guide to the Galaxy",
        "So long and thanks for all the fish"
    ]

available_functions = {
    "get_time": get_time,
    "search_google": search_google
}
tools = list(available_functions.values())
model = "qwen3:4b"
messages = [{
    "role": "system",
    "content": SYSTEM
}]

while True:
    messages.append({
        "role": "user",
        "content": input("> "),
    })

    in_toolchain = True

    while in_toolchain:
        response: ChatResponse = chat(
            model,
            messages=messages,
            tools=tools,
            think=True
        )
        messages.append(response.message)

        calls = response.message.tool_calls
        if calls:
            for tool in calls:
                if function := available_functions.get(tool.function.name):
                    output = function(**tool.function.arguments)
                    messages.append({
                        "role": "tool",
                        "content": str(output),
                        "tool_name": tool.function.name
                    })
                else:
                    messages.append({
                        "role": "tool",
                        "content": f"Tool not found: {tool.function.name}",
                        "tool_name": "not_found"
                    })
        else:
            in_toolchain = False

    print(messages[-1]["content"])

