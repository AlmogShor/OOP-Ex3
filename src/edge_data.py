class edge_data:
    def __init__(self, src, dst, tag, info):
        self.__src = src
        self.__dst = dst
        self.__weight = 0.0
        self.__tag = tag
        self.__info = info

    def __init__(self, src, dst, weight):
        self.__src = src
        self.__dst = dst
        self.__weight = weight
        self.__tag = 0
        self.__info = "0"

    def get_src(self):
        return self.__src

    def get_dest(self):
        return self.__dst

    def get_weight(self):
        return self.__weight

    def get_info(self):
        return self.__info

    def set_info(self, s):
        self.__info = s

    def get_tag(self):
        return self.__tag

    def set_tag(self, tag):
        self.__tag = tag
