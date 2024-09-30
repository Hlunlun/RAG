import socket


# currently support model:
# jcai/llama3-taide-lx-8b-chat-alpha1:Q4_K_M
# llama3
def startChat(model="jcai/llama3-taide-lx-8b-chat-alpha1:Q4_K_M"):
    s = socket.socket()
    host = "140.116.154.86"
    port = 50000

    try:
        s.connect((host, port))
        print("Connected to server")
        s.send(model.encode("utf-8"))
        response = s.recv(1024).decode("utf-8")
        print("SERVER >>", response)
        while True:
            msg = input("CLIENT >> ")
            s.send(msg.encode("utf-8"))

            if msg.lower() == "exit":
                break

            response = s.recv(1024).decode("utf-8")
            print("SERVER >>", response)

    except Exception as e:
        print("An error occurred:", e)
    finally:
        s.close()
        print("Connection closed")


def startChat(model="jcai/llama3-taide-lx-8b-chat-alpha1:Q4_K_M"):
    """
    Connects to a server and starts a chat session.

    Args:
        model (str): The model to use for the chat session. Default is "jcai/llama3-taide-lx-8b-chat-alpha1:Q4_K_M".

    Returns:
        None
    """
    s = socket.socket()
    host = "140.116.154.86"
    port = 50000

    try:
        s.connect((host, port))
        print("Connected to server")
        s.send(model.encode("utf-8"))
        response = s.recv(1024).decode("utf-8")
        print("SERVER >>", response)
        while True:
            msg = input("CLIENT >> ")
            s.send(msg.encode("utf-8"))

            if msg.lower() == "exit":
                break

            response = s.recv(1024).decode("utf-8", errors="ignore")
            print("SERVER >>", response)

    except Exception as e:
        print("An error occurred:", e)
    finally:
        s.close()
        print("Connection closed")


def api_mode(
    model="llama3",
    prompt=[
        {"role": "user", "content": "Hellow!"},
    ],
):
    """
    Connects to a server and enters API mode for a single API call.

    Args:
        model (str): The model to use for the chat session. Default is "llama3".
        prompt (str): The conversation prompt in a specific format. Default is an empty string.

    Returns:
        None
    """
    prompt = symbol_correction(prompt)
    s = socket.socket()
    host = "140.116.154.86"
    port = 50001

    try:
        s.connect((host, port))
        print("Connected to server")
        s.send(model.encode("utf-8"))
        response = s.recv(1024).decode("utf-8")
        print("SERVER >>", response)
        print("Your prompt >>", str(prompt))
        s.send(str(prompt).encode("utf-8"))
        response = s.recv(1024).decode("utf-8", errors="ignore")
        print("SERVER >>", response)
        s.close()
    except Exception as e:
        s.close()
    print("Connection closed")


def symbol_correction(prompt):
    """
    Corrects symbols in the conversation prompt.

    Args:
        prompt (list): The conversation prompt in json format.

    Returns:
        list: The corrected conversation prompt.
    """
    for pro in prompt:
        if "'" in pro["content"]:
            pro["content"] = pro["content"].replace("'", "\\'")
        if '"' in pro["content"]:
            pro["content"] = pro["content"].replace('"', "\\''")
    return prompt


if __name__ == "__main__":
    # Example for API mode
    # prompt = [
    #     {'role': 'user', 'content': 'My name is Tina'},
    #     {'role': 'assistant', 'content': "Nice to meet you, Tina! What brings you here today? Do you have a specific question or topic you'd like to chat about? I'm all ears!"},
    #     {'role': 'user', 'content': 'Who am I?'}
    #     ]

    # api_mode(prompt=prompt)

    # Example for chat mode
    startChat()
