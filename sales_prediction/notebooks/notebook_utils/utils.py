import os


class Directory:
    def __init__(self, __file__):
        self.__file__ = __file__
        self.THIS_DIR = os.path.dirname(os.path.abspath(__file__))
        self.BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
        self.DATA_DIR = os.path.join(os.path.join(self.BASE_DIR, 'data'))

    def __str__(self):
        return f'''Directory(__file__ = {self.__file__},
        THIS_DIR = {self.THIS_DIR},
        BASE_DIR = {self.BASE_DIR},
        DATA_DIR = {self.DATA_DIR})'''
