

class DBReader:


    def __init__(self, file_contents=[]):
        if not file_contents:
            file_contents = self.read_file()
        self.cleaned_data = self.clean_file(file_contents)


    def read_file(self):
        with open("database") as infile:
            data = infile.readlines()
        return data


    @staticmethod
    def clean_file(file_contents):
        return [line.split(",") for line in file_contents]


    def filter_by_username(self, username):
        return [line[0:1] for line in self.cleaned_data if line[0].lower() == username.lower()]


    def filter_by_password(self, password):
        return[line[2:] for line in self.cleaned_data if line[1].lower() == password.lower()]


    def get_by_username_password(self, username, password):
        username_results = self.filter_by_username(username)
        password_results = self.filter_by_password(password)
        if len(username_results) == 1 and len(password_results) == 1:
            return(password_results[0])
        else:
            return("Either your username or password is incorrect.")


    def add_to_file(self):
        with open("database", "a") as outfile:
            outfile.write("\n" + input("Enter a username: ").lower())
            outfile.write("," + input("Enter a password: ").lower())
            outfile.write("," + input("Enter the user's full name: ").lower())
            outfile.write("," + input("Enter the user's age: ").lower())
            outfile.write("," + input("Enter the user's weight: ").lower())
        return("Awesome, you added a new user!")

    def input_direction(self):
        while True:
            next_input = input("Would you like to add a new user? Enter y to add or n to logout. ")
            if next_input == "y":
                print(self.add_to_file())
                continue
            elif next_input == "n":
                return "You are now logged out. "
            else:
                print("That's not a valid option. ")
                continue

