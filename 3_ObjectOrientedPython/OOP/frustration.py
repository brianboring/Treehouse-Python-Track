class Liar(list):
    def __len__(self):
        return super().__len__() + 5

test = Liar([1, "seven"])
print(len(test))