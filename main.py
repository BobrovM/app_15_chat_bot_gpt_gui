from PyQt6.QtWidgets import QMainWindow, QTextEdit, QLineEdit, QPushButton, QApplication
import sys
from backend import Chatbot
import threading


class ChatbotWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.chatbot = Chatbot()

        self.setFixedHeight(400)
        self.setFixedWidth(500)

        self.chat_area = QTextEdit(self)
        self.chat_area.setGeometry(10, 10, 480, 300)
        self.chat_area.setReadOnly(True)

        self.input_field = QLineEdit(self)
        self.input_field.setGeometry(10, 320, 400, 70)
        self.input_field.returnPressed.connect(self.send_message)

        self.button = QPushButton("Send", self)
        self.button.setGeometry(420, 320, 70, 70)
        self.button.clicked.connect(self.send_message)

        self.show()

    def send_message(self):
        user_input = self.input_field.text().strip()
        if len(user_input) != 0:
            self.chat_area.append(f"<p>Me: {user_input}</p>")
            self.input_field.clear()

            thread = threading.Thread(target=self.get_bot_response, args=(user_input,))
            thread.start()

    def get_bot_response(self, user_input):
        response = self.chatbot.get_response(user_input)
        self.chat_area.append(f"<p style='background-color:#e3e3e3'>Bot: {response}</p>")


app = QApplication(sys.argv)
window = ChatbotWindow()
sys.exit(app.exec())