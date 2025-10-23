class Hello:
    def __init__(self, name: str):
        self.__name: str = name

    def __del__(self):
        del self.__name

    def get_name(self):
        return self.__name

    def set_name(self, new_name):
        self.__name = new_name

    def say(self):
        print(f"Hello {self.__name}!")
