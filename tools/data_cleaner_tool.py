



class data_cleaner():
    def __init__(self):
        self.name = "Data Cleaning Tool v0.1"
        self.author = "Justin Hagerty"
        self.current_file = list()
        self.data_to_remove = list()
        self.data_left_over = list()
        self._example_words = ('Nuclear', 'Power', 'Plant', 'Argentina')

    def __repr__(self):
        return self.name

    def open_file(self, file_location):
        with open(file_location) as f:
            return f.readlines()

    def print_file(self, func_file):
        for line in func_file:
            print(line)

    def parse_file(self, list_of_lines):
        temp_line = ""
        for line in list_of_lines:
            for word in line.split():
                if(word in self.data_to_remove):
                    print(word)
                else:
                    temp_line = temp_line + " "
            self.data_left_over.append(temp_line)

    def check_input(self, func_user_input):
        print("check: ")
        if(func_user_input == 'n'):
            return False
        else:
            return True


data_cleaner_instance = data_cleaner()
data_cleaner_instance.open_file("./example.txt")