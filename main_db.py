from db import DBReader

db_reader = DBReader()
while True:
    username_input = input("Enter your username: ")
    password_input = input("Enter your password: ")
    db_reader.get_by_username_password(username_input, password_input)
    if type(db_reader.get_by_username_password(username_input, password_input)) == list:
        print(db_reader.get_by_username_password(username_input, password_input))
    else:
        print(db_reader.get_by_username_password(username_input, password_input))
        continue

    while True:
        print(db_reader.input_direction())
        break