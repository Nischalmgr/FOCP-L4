# University Chatbot - Readme

This project is a graphical chatbot application built using Python and Tkinter. It simulates a conversation between a user and a virtual assistant (agent) and provides responses based on keywords entered by the user. The chatbot is tailored for a fictional university, "University of Poppleton," and addresses common queries related to courses, admission, fees, and more.

---

## Features

- **Keyword-Based Responses**:
  The chatbot detects keywords in the user input and provides predefined responses.

- **Fallback Responses**:
  If the chatbot does not understand a query, it provides random fallback responses.

- **Chat Logging**:
  All conversations are saved in a formatted text file with timestamps for future reference.

- **Graphical User Interface (GUI)**:
  The application features a user-friendly interface with a text box for conversation and buttons for sending messages and exiting.

- **Random Agent Selection**:
  The chatbot's name is randomly chosen from a predefined list of agent names.

---

## Prerequisites

1. **Python 3.x**:
   Ensure Python 3.x is installed on your system.

2. **Dependencies**:
   Install the `tabulate` library using pip:
   ```bash
   pip install tabulate
   ```

---

## Usage

### Running the Program
To start the chatbot, run the script in a Python environment:
```bash
python chatbot.py
```

### Interacting with the Chatbot
- Upon launch, the chatbot will prompt the user to enter their name.
- The conversation starts with a greeting from the chatbot.
- Users can ask questions or type commands in the input field.
- To exit, users can type "bye," "exit," "quit," or click the **Exit** button.

### Saving the Chat History
When exiting, the chat history is automatically saved to a text file in the following format:
```
conversation_YYYY-MM-DD_HH-MM-SS.txt
```
The file includes the sender, message, and timestamp in a tabular format.

---

## Keyword Responses
The chatbot recognizes the following keywords and provides specific responses:
 

## Files

### Main Script
`chatbot.py`: The main Python script that runs the chatbot application.

### Log Files
`conversation_YYYY-MM-DD_HH-MM-SS.txt`: Saved conversation logs with timestamps.

---

## Example Interaction
**User:** What courses do you offer?

**Agent:** We offer a variety of courses. What are you interested in?

**User:** Tell me about AI.

**Agent:** We provide specialized courses in Artificial Intelligence.

**User:** Bye.

**Agent:** Goodbye! Have a great day!

---

## Notes
- Ensure that the `tabulate` library is installed before running the script.
- The chatbot saves logs in the current working directory.
- Responses are limited to predefined keywords; fallback responses handle unknown queries.

---

## License
This project is licensed under the MIT License. Feel free to use, modify, and distribute it.
