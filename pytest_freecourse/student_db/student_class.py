import json

class StudentDB:
    def __init__(self):
        self.__data = None

    def connect(self, data_file):
        with open(data_file) as jf:
            self.__data = json.load(jf)

    def get_data(self, name):
        for student in self.__data['students']:
            if student['name'] == name:
                return student

    def close(self):
        pass