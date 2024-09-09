class User:
    def __init__(self, username):
        self.username = username
        self.inbox = []

    def send_message(self, recipient, message):
        print(f"Sending message from {self.username} to {recipient.username}: {message}")
        recipient.inbox.append((self.username, message))

    def read_inbox(self):
        print(f"Inbox of {self.username}:")
        for sender, message in self.inbox:
            print(f"From {sender}: {message}")

class MessagingApp:
    def __init__(self):
        self.users = {}

    def register_user(self, username):
        if username in self.users:
            print(f"Username {username} is already taken.")
        else:
            self.users[username] = User(username)
            print(f"User {username} registered successfully.")

    def send_message(self, sender, recipient, message):
        if sender in self.users and recipient in self.users:
            self.users[sender].send_message(self.users[recipient], message)
        else:
            print("Either the sender or recipient does not exist.")

    def show_inbox(self, username):
        if username in self.users:
            self.users[username].read_inbox()
        else:
            print(f"User {username} does not exist.")

# Ejemplo de uso
app = MessagingApp()
app.register_user("Alice")
app.register_user("Bob")

app.send_message("Alice", "Bob", "Hola, Bob!")
app.show_inbox("Bob")
