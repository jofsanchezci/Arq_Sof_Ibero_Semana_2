from services.message_service import MessageService
from services.user_service import UserService

class MessagingApp:
    def __init__(self):
        self.user_service = UserService()
        self.message_service = MessageService(self.user_service)

    def register_user(self, username):
        return self.user_service.register_user(username)

    def send_message(self, sender, recipient, message):
        return self.message_service.send_message(sender, recipient, message)

    def show_inbox(self, username):
        inbox = self.message_service.read_inbox(username)
        if isinstance(inbox, list):
            return f"Inbox of {username}: {inbox}"
        else:
            return inbox

# Ejemplo de uso
app = MessagingApp()
print(app.register_user("Alice"))
print(app.register_user("Bob"))

print(app.send_message("Alice", "Bob", "Hola, Bob!"))
print(app.show_inbox("Bob"))
