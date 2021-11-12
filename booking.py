'''
Here we create a class Booking with four attributes with the help of decorators"
'''
class Booking:

    def __init__(self, name, phone, start, end):
        self.name = name
        self.phone = phone
        self.start = start
        self.end = end

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        self.__name = name

    @property
    def phone(self):
        return self.__phone

    @phone.setter
    def phone(self, phone):
        if len(phone) != 10:
            raise ValueError("Invalid phone number")
        else:
            self.__phone = phone

    @property
    def start(self):
        return self.__start

    @start.setter
    def start(self, start):
        self.__start = start

    @property
    def end(self):
        return self.__end

    @end.setter
    def end(self, end):
        self.__end = end