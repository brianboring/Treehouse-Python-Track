from peewee import *

db = SqliteDatabase('students.db')
#above makes a database connection called students.db that is assigned to the variable db

class Student(Model):
    username = CharField(max_length=255, unique=True)
    #above can allow creation of a username up to 255 characters and no two usernames can be the same
    points = IntegerField(default=0)
    #username and points are called fields

    class Meta:
        #class inside of our class that tells the model what db it belongs to
        database = db


students = [
    {'username': 'kennethlove',
     'points': 14888},
    {'username': 'chalkers',
     'points': 11912},
    {'username': 'joykesten2',
     'points': 7363},
    {'username': 'craigsdennis',
     'points': 4079},
    {'username': 'davemcfarland',
     'points': 14717},
]
#above is our list of dictionaries

def add_students():
    for student in students:
        try:
            Student.create(username=student['username'],
                       points=student['points'])
            # above is a function for iterating through our list of dictionaries called students
            # and making an instance of Student class/model out of each student
        except IntegrityError:
            student_record = Student.get(username=student['username'])
            student_record.points = student['points']
            student_record.save()
            # this will overwrite the unique username
            # for the purpose of updating records/running the program more than once

def top_student():
    student = Student.select().order_by(Student.points.desc()).get()
    #sorts all students by descending order of points and gets the first record
    return student

if __name__ == '__main__':
    #this makes the code only run when the script is run and not when it's imported
    db.connect()
    #method called on our db to create a connection to it
    db.create_tables([Student], safe=True)
    #method to create our table
    add_students()
    #calls the add_students function
    print("Our top student right now is: {0.username} who has {0.points} points.".format(top_student()))