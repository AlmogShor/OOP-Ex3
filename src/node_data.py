class node_data:
    def __init__(self, key, loc):
        self.__key = key
        self.__point = loc
        self.__weight = 0.0
        self.__info = ""
        self.__tag = -1

    def get_key(self):
        return self.__key

    def get_location(self):
        return self.__point

    def set_location(self, loc):
        self.__point = loc

    def get_weight(self):
        return self.__weight

    def set_weight(self, w):
        self.__weight = w

    def get_info(self):
        return self.__info

    def set_info(self, s):
        self.__info = s

    def get_tag(self):
        return self.__tag

    def set_tag(self, t):
        self.__tag = t

    def equals(self, ot):
        if ot == self:
            return True
        if ot == None or type(ot) != type(self):
            return False
        other = node_data(ot)
        return self.get_key() == other.get_key() and self.get_weight() == other.get_weight() and self.point.equals(
            other.get_location()) and self.tag == other.get_tag() and self.get_info().equals(other.get_info())

