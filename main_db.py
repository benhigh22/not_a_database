from db import DBReader

db_reader = DBReader()
username_input = input("Enter your username: ")
password_input = input("Enter your password: ")
print(db_reader.get_by_username(username_input))
print(db_reader.get_by_password(password_input))