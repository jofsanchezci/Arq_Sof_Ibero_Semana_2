class MessageService:
    def __init__(self, user_service):
        self.user_service = user_service

    def send_message(self, sender, recipient, message):
        sender_user = self.user_service.get_user(sender)
        recipient_user = self.user_service.get_user(recipient)

        if sender_user and recipient_user:
            recipient_user["inbox"].append((sender, message))
            return f"Message from {sender} to {recipient}: {message} sent successfully."
        else:
            return "Either the sender or recipient does not exist."

    def read_inbox(self, username):
        user = self.user_service.get_user(username)
        if user:
            return user["inbox"]
        else:
            return f"User {username} does not exist."
