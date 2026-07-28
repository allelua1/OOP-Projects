class User:
    
    def __init__(self, password):
        # TODO: Store the password as a private attribute using double underscore (__)
        #This makes it harder to access from outside the class
        self.__password = password
    def check_password(self, input_password):
        # TODO: Return True if input_password matches the stored private password
        #       Return False otherwise
        if input_password == self.__password:
            return True
        return False
    def change_password(self, old_password, new_password):
         # TODO: Check if old_password is correct using the check_password method
        # TODO: If old_password is correct, update the private password to new_password and return True
        # TODO: If old_password is incorrect, return False without changing the password
        if self.check_password(old_password):
            self.__password = new_password
            return True
        return False

user = User("secure123")
print("User Created with initial password")

if user.check_password("secure123"):
    print("Inital password verification successfu;")

if not user.check_password("wrongpass"):
    print("Incorect password properly rejected")

#  Test changing password from "secure123" to "newpass456"
if user.change_password("secure123", "newpass123"):
    print("Password successfully changed")

#TODO: Verify old password no longer works 
if user.check_password("secure123"):
    print("Old password no longer works")

# TODO: Verify the new password works
if user.check_password("newpass123"):
    print("New password works correctly")

# TODO: Try changing password with incorrect old password
if user.change_password("wrongold", "hackerpw"):
    print("Security maintained: wrong old password rejected")

# TODO: Verify password is still secure after failed change attempt
if user.check_password("newpass123"):
    print("Password remains secure after failed change attempt")  
