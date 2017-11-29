class Letter:
    def __init__(self, pattern=None):
        self.pattern = pattern

    def __str__(self):
        new_string = []
        for i in self.pattern:
            if i == '.':
                new_string.append('dot')
            elif i == '_':
                new_string.append('dash')
        return('-'.join(new_string))

    def __iter__(self):
        yield from self.pattern

    #classmethod code challenge
    @classmethod

    def from_string(cls, string2):
        new_string2 = []
        for i in string2.split('-'):
            if i == 'dot':
                new_string2.append('.')
            elif i == 'dash':
                new_string2.append('_')
        print(new_string2)
        return cls(new_string2)


class S(Letter):
    def __init__(self):
        pattern = ['.', '.', '.']
        super().__init__(pattern)

#test Letter
#print(Letter(['.', '_', '.']))
test = Letter()
print(test.from_string('dash-dot'))
