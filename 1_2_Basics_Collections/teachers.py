def num_teachers(teacher_dict):
    teacher_count = 0
    for name in teacher_dict:
        teacher_count += 1
    print(teacher_count)

def num_courses(teacher_dict):
    courses_count = 0
    for i in teacher_dict:
        courses=teacher_dict[i]
        print(courses)
        for j in courses:
            courses_count += 1
    print(courses_count)

def courses(teacher_dict):
    courses_list = []
    for i in teacher_dict:
        courses = teacher_dict[i]
        print(courses)
        for j in courses:
            courses_list.extend([j])
    print(courses_list)

def most_courses(teacher_dict):
    class_count = 0
    most_classes = 0
    teacher = ""
    for i in teacher_dict:
        courses=teacher_dict[i]
        print(courses)
        for j in courses:
            class_count += 1
            if class_count > most_classes:
                most_classes = class_count
                teacher = [i]
        class_count = 0
    best_teacher = ''.join(teacher)
    print(class_count)
    print(most_classes)
    print(teacher)
    print(best_teacher)

def stats(teacher_dict):
    master_list = []
    class_count = 0
    teacher = ""
    for i in teacher_dict:
        courses = teacher_dict[i]
        print(courses)
        for j in courses:
            class_count += 1
            teacher = (i)
            temp_list = [(i), class_count]
        print(temp_list)
        master_list.insert(-1,temp_list)
        class_count = 0
    print(master_list)


stats (teacher_dict={'Kenneth Love':['Python Collections', 'Python Basics'], 'Andrew Whatever':['Javascript', 'jQuery', "Some other class"], 'testkey':['testvalue']})


