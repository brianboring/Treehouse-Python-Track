class Protected:
    __name = "Security"

    def __method(self):
        return self.__name

prot = Protected()
print (dir(prot))
print (prot._Protected__method())