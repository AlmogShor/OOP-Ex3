class node_data:
    def __init__(self, key, loc):
        self.__key = key
        self.__point = loc

    def get_key(self):
        return self.__key

    def get_location(self):
        return self.__point

    def set_location(self, loc):
        self.__point = loc

    def equals(self, ot):
        if ot == self:
            return True
        if ot == None or type(ot) != type(self):
            return False
        other = node_data(ot.get_key(),ot.get_location())
        return (self.get_key() == other.get_key() and self.get_location() == other.get_location()
                and self.get_tag() == other.get_tag() and self.get_info() == other.get_info())
