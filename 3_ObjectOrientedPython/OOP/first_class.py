class Student:

    def __init__(self, name, **kwargs):
        self.name = name

        for key, value in kwargs.items():
            setattr(self, key, value)

        # **kwargs test
        print("{}'s hair is {}".format(self.name, self.hair_color))

    def praise(self):
        print("You're doing a great job, {}".format(self.name))

    def reassurance(self):
        print("Chin up, {}. You'll get it next time!".format(self.name))

    def feedback(self, grade):
        if grade < 50:
            return self.reassurance()
        else:
            return self.praise()

foo = Student("Brian", hair_color = "brown")
foo.feedback(60)