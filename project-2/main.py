from tabulate import tabulate
import tkinter as tk
from tkinter import simpledialog, scrolledtext
import random
from datetime import datetime

# Agent names and responses
agent_names = ["Amik", "Nischal", "Ram", "Sita", "Hari"]
keywords_response = {
    "eca": "Yes, the college provides extracurricular activities.",
    "courses": "We offer a variety of courses. What are you interested in?",
    "computing": "We have a well-structured computing program.",
    "cyber security": "Our cybersecurity courses are cutting-edge.",
    "ai": "We provide specialized courses in Artificial Intelligence.",
    "bca": "Our BCA program is designed to develop IT professionals.",
    "college time": "The college operates from 8:00 AM to 4:00 PM.",
    "admission": "Admissions are open for the next semester.",
    "college fee": "The college fee structure varies based on the course.",
    "scholarship": "We offer scholarships based on merit and need.",
    "canteen": "Our canteen offers a variety of meals and snacks.",
    "date": "Intake dates are January/February and October/November.",
}


def random_response():
    '''Random fallback responses.'''
    responses = [
        "I'm not sure about that. Can you ask me something else?",
        "Interesting question! But I have no answer to that.",
        "Could you please clarify your question?",
        "Sorry, I am not allowed to answer that.",
    ]
    return random.choice(responses)


def add_message(sender, message):
    '''Add a message to the chat display.'''
    time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    final_message = f"{sender} : {message}"
    chat_display.configure(state="normal")
    chat_display.insert(tk.END, final_message + "\n")
    chat_display.see(tk.END)
    chat_history.append([sender, message, time])


def handle_user_input(event=None):
    '''Handle user input.'''
    user_message = user_input.get().strip()
    if not user_message:
        return

    add_message(user_name, user_message)
    user_input.delete(0, tk.END)

    if user_message.lower() in ["bye", "exit", "quit","thank you"]:
        add_message(agent_name, "Goodbye! Have a great day!")
        save_and_exit()
        return

    responses = []
    for keyword, response in keywords_response.items():
        if keyword.lower() in user_message.lower():
            responses.append(response)

    if responses:
        for response in responses:
            add_message(agent_name, response)
    else:
        add_message(agent_name, random_response())

def save_and_exit():
    '''Save the chat history and exit.'''
    date_str = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    filename = f"conversation_{date_str}.txt"

    formatted_history = []
    for sender, message, time in chat_history:
        role = "(agent)" if sender == agent_name else "(user)"
        formatted_history.append([role, sender, message, time])

    headers = ["Role", "Sender", "Message", "Time"]
    formatted_log = tabulate(formatted_history, headers=headers, tablefmt="grid")
     
    with open(filename, "w") as file:
        file.write(formatted_log)
        file.write("\n")

    print(f"Conversation saved to {filename}")
    root.quit()

# Initialize the chatbot GUI
root = tk.Tk()
root.title("Chatbot - University of Poppleton")

user_name = simpledialog.askstring("User Name", "Please enter your name:")
if not user_name:
    user_name = "User"

agent_name = random.choice(agent_names)

chat_display = scrolledtext.ScrolledText(root, wrap=tk.WORD, state="disabled", height=20, width=50)
chat_display.grid(row=0, column=0, columnspan=2, padx=10, pady=10)

user_input = tk.Entry(root, width=40)
user_input.grid(row=1, column=0, padx=10, pady=10)
user_input.bind("<Return>", handle_user_input)

send_button = tk.Button(root, text="Send", command=handle_user_input)
send_button.grid(row=1, column=1, padx=10, pady=10)

exit_button = tk.Button(root, text="Exit", command=save_and_exit)
exit_button.grid(row=2, column=1, padx=10, pady=10)

chat_history = []
add_message(agent_name, f"Hello, {user_name}! I'm {agent_name}, your virtual assistant. How can I help you today?")

root.mainloop()
