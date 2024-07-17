
# The lines `import nltk`, `from nltk.chat.util import Chat, reflections`, and `import tkinter as tk`
# are importing necessary libraries for the Python script.
import nltk
from nltk.chat.util import Chat, reflections
import tkinter as tk

# The `faq_pairs` variable in the Python script is a list of lists containing pairs of user input
# patterns and corresponding responses for a chatbot. Each inner list represents a pair where the
# first element is a regular expression pattern that the user might input, and the second element is a
# list of possible responses that the chatbot can provide based on that input pattern.
faq_pairs = [
    [
        r"what is your name?",
        ["My name is ChatBot and I'm here to assist you."]
    ],
    [
        r"how can you help me?",
        ["I can provide information, answer questions, or just have a friendly chat. What do you need help with today?"]
    ],
    [
        r"who created you?",
        ["I was created by Hamidur."]
    ],
    [
        r"how old are you?",
        ["I'm a computer program, so I don't have an age."]
    ],
    [
        r"tell me a joke",
        ["Why don't scientists trust atoms? Because they make up everything!"]
    ],
    [
        r"working hours?",
        ["I'm available 24/7 to assist you."]
    ],
    [
        r"contact support",
        ["For support inquiries, please visit our website or contact us at [support email/phone]."]
    ],
    [
        r"hobbies?",
        ["I enjoy chatting with users like you and learning new things!"]
    ],
    [
        r"secure information",
        ["Your privacy and security are important. I do not store any personal information."]
    ],
    [
        r"recommend a restaurant",
        ["Sure! What type of cuisine are you interested in?"]
    ],
    [
        r"weather today",
        ["Let me check that for you."]  # Integrate with weather API to provide current weather information
    ],
    [
        r"change password|account settings",
        ["Please visit your account settings on our website to update your password and account details."]
    ],
    [
        r"delete account",
        ["To delete your account, please contact our support team at [support email/phone]."]
    ],
    [
        r"languages do you speak?",
        ["I primarily communicate in English, but I can try to understand other languages too."]
    ],
    [
        r"are you a human?",
        ["No, I'm a chatbot powered by artificial intelligence and natural language processing."]
    ],
    [
        r"start using your services",
        ["Simply start typing your questions or statements, and I'll do my best to assist you."]
    ],
    [
        r"tips for staying healthy",
        ["Sure! Eating balanced meals, staying active, and getting enough sleep are key to staying healthy."]
    ],
    [
        r"provide information about next24tech Technology and services",
        ["Next24tech specializes in developing custom software solutions for businesses of all sizes."]
    ],
    [
        r"exit",
        ["Bye! Take care. See you soon :)", "It was nice talking to you. Goodbye!"]
    ]
]

# The line `chatbot = Chat(faq_pairs, reflections)` in the Python script is creating an instance of a
# chatbot using the `Chat` class provided by the `nltk` library. The `Chat` class requires two
# parameters:
chatbot = Chat(faq_pairs, reflections)

def get_response(user_input):
    """
    The function `get_response` takes user input, uses a chatbot to generate a response, and handles
    KeyError exceptions by returning a default message.
    
    :param user_input: The `user_input` parameter is the input provided by the user that will be used as
    an input to the `chatbot.respond()` function in the `get_response` function. The `chatbot.respond()`
    function is expected to return a response based on the user input. If an error occurs during
    :return: The function `get_response` will return the response generated by the chatbot for the user
    input. If a KeyError is raised during the response generation process, the function will return the
    message "I'm sorry, I'm not sure how to respond to that."
    """
    try:
        response = chatbot.respond(user_input)
        return response
    except KeyError:
        return "I'm sorry, I'm not sure how to respond to that."

def send_message():
    """
    The `send_message` function takes user input, gets a response from a chatbot, and displays the
    conversation in a chat transcript area.
    """
    user_input = entry.get()
    response = get_response(user_input)
    chat_transcript_area.insert('end', 'You: ' + user_input + '\n')
    chat_transcript_area.insert('end', 'Chatbot: ' + response + '\n')
    entry.delete(0, 'end')

# The lines `root = tk.Tk()` and `root.title("Chatbot")` in the Python script are creating a new
# Tkinter window for the chatbot interface and setting the title of the window to "Chatbot".

root = tk.Tk()
root.title("Chatbot")

# The code snippet `entry = tk.Entry(root, width=50)` is creating an entry widget within the Tkinter
# window that was previously created. This entry widget serves as a text input field where the user
# can type their messages or questions to interact with the chatbot.
entry = tk.Entry(root, width=50)
entry.pack(padx=10, pady=10)

# The code snippet `send_button = tk.Button(root, text="Send", command=send_message)` is creating a
# button widget within the Tkinter window that was previously created. This button widget is labeled
# "Send" as specified by the `text="Send"` parameter.
send_button = tk.Button(root, text="Send", command=send_message)
send_button.pack(padx=10, pady=10)

# The code snippet `chat_transcript_area = tk.Text(root, width=50, height=10)` is creating a text
# widget within the Tkinter window that was previously created. This text widget is used to display
# the conversation between the user and the chatbot.
chat_transcript_area = tk.Text(root, width=50, height=10)
chat_transcript_area.pack(padx=10, pady=10)

# `root.mainloop()` is a method in Tkinter that starts the main event loop of the Tkinter window. This
# method listens for events such as user inputs, button clicks, and updates to the GUI elements. It
# keeps the window running and responsive to user interactions until the window is closed by the user.
root.mainloop()
