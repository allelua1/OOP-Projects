class SecureMessenger:
    def __init__(self, username, password = "secure123"):
        self.username = username
        self.__password = password
        self.__messages = []
        self.__login_attempts = 0
        self.__is_logged_in = False

    def add_message(self, message):
        if self.__is_logged_in:
            self.__messages.append(message)
            return f"Message added: {message}"
        return "Error: You must be logged in add messages. "
    def login(self, password):
        self.__login_attempts =+ 1
        if password == self.__password:
            self.__is_logged_in = True
            return "Login successful"
        return "Login failed: Incorrect password"

    def get_message(self):
         # TODO: Check if user is logged in using the private __is_logged_in attribute
        # TODO: If logged in but __messages list is empty, return exactly: "No messages"
        # TODO: If logged in and messages exist, return all messages joined with newlines
        #       using: "\n".join(self.__messages)
        # TODO: If not logged in, return exactly: "Error: You must be logged in to view messages"
        if self.__is_logged_in: 
           if not self.__messages:
                return "No messages"
           
           return "\n".join(self.__messages)
        return "Error: You must be logged in to view messages"

    def get_login_attempts(self):
        return f"Login attempts: {self.__login_attempts}"

messenger = SecureMessenger("user1")

# try to add messages before login
print(messenger.add_message("Hello World"))

# attempt login with wrong password
print(messenger.login("wrongpassword"))

# login with correct password
print(messenger.login("secure123"))

# add a message after succesfl login
print(messenger.add_message("secure message"))

# retrieve messages
print(messenger.get_message())
        