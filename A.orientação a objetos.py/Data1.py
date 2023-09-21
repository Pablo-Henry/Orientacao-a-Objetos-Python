

class Data:
    def __init__(self, dia , mes, ano):
        self.__dia = dia
        self.__mes = mes
        self.__ano = ano

    def dataf(self):
        print("{:02d}/{:02d}/{}".format(self.__dia, self.__mes, self.__ano))

    @property
    def dia(self):
        return self.__dia

    @property
    def mes(self):
        return self.__mes

    @property
    def ano(self):
        return self.__ano