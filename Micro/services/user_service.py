class UserService:
    def __init__(self):
        self.users = {}

    def register_user(self, username):
        if username in self.users:
            return f"Username {username} is already taken."
        else:
            self.users[username] = {"username": username, "inbox": []}
            return f"User {username} registered successfully."

    def get_user(self, username):
        return self.users.get(username, None)
