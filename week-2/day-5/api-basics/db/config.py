
class BsConfig:
    def __init__(self):
        self.dt = 'hi'


class NwConfig:
    def __init__(self):
        self.ip = 'localhost'
        self.bs = BsConfig()


class Config:
    def __init__(self):
        self.url = 'db://anc'
        self.port = 1244
        self.nw = NwConfig()
        self.lst = ['abc', 'pqr', 'lmn']
