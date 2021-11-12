'''
Here we create a class Table. It includes the usage of decorators and characterized
by its attributes and three methods: busy (it checks if a table is busy or not),
add (adds a booking with a specific table) and release (releases a table, i.e. leaves a list of free tables)
'''
class Table:
    def __init__(self, name, seats):
        self.__name = name
        self.__seats = seats
        self.__bookings = []

    @property
    def bookings(self):
        return self.__bookings

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        self.__name = name

    @property
    def seats(self):
        return self.__seats

    @seats.setter
    def seats(self, seats):
        self.__seats = seats

    def busy(self, start, end):
        for booking in self.__bookings:
            if start >= booking.start and start < booking.end:
                return True
            if end > booking.start and end <= booking.end:
                return True
            if start <= booking.start and end > booking.end:
                return True
        return False
                
    def add(self, booking):
        if self.busy(booking.start, booking.end):
            return False
        self.__bookings.append(booking)
        return True
    
    def release(self, time):
        self.__bookings = [booking for booking in self.__bookings
                           if time < booking.start or time > booking.end]
