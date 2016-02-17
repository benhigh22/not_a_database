

class DBReader:


    def __init__(self, file_contents=[]):
        if not file_contents:
            file_contents = self.read_file()
        self.cleaned_data = self.clean_file(file_contents)


    def read_file(self):
        with open("database") as infile:
            data = infile.readlines()
        return data


    def add_to_file(self):
        with open("database") as infile:
            pass


    @staticmethod
    def clean_file(file_contents):
        return [line.split(",") for line in file_contents]


    def filter_by_username(self, username):
        return [line[0:1] for line in self.cleaned_data if line[0].lower() == username.lower()]


    def get_by_username(self, username):
        username_results = self.filter_by_username(username)
        if len(username_results) > 1:
            print("That username already exists, choose a different username.")
            return self.get_by_username()
        elif len(username_results) == 0:
            return("No records found for that username.")
        else:
            return username_results[0]


    def filter_by_password(self, password):
        return [line[2:] for line in self.cleaned_data if line[1].lower() == password.lower()]


    def get_by_password(self, password):
        password_results = self.filter_by_password(password)
        if len(password_results) == 1:
            return password_results[0]
        else:
            return(self.get_by_username())






