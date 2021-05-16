
# use this to get common lines from data and get common words to see what might need to be removed from the data to help clean it up

class common_words():
    def __init__(self):
        self.unique_words = dict()
        self.unique_lines = dict()

    def open_file(self, file_location):
        with open(file_location) as f:
            return f.readlines()

    def get_file_unique_lines(self, file_name):
        for line in self.open_file(file_name):
            if(line in self.unique_lines):
                self.unique_lines[line] = self.unique_lines[line] + 1
            else:
                self.unique_lines[line] = 1

    def get_file_unique_words(self, list_of_lines):
        for line in list_of_lines:
            for word in line.split(' '):
                if (word in self.unique_words):
                    self.unique_words[word] = self.unique_words[word] + 1
                else:
                    self.unique_words[word] = 1