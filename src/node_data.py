class node_data:
    def __init__(self, key, loc):
        self.__key = key
        self.__point = loc
        self.in_count = 0
        self.out_count = 0

    def get_key(self):
        return self.__key

    def get_location(self):
        return self.__point

    def set_location(self, loc):
        self.__point = loc

    def __str__(self):
        return "id: " + str(self.get_key()) + "location: " + self.get_location()

    def __repr__(self):
        return str(self.get_key()) + ": |edges_out| " + str(self.out_count) + " |edges in| " + str(self.in_count)
