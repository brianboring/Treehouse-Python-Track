def string_factory(dicts):
    string = "My name is {name} and my favorite food is {food}!"
    result = []
    for i in dicts:
        result.append(string.format(**i))
    print (result)


string_factory(dicts = [{"name":"John", "food":"pizza"},{"name":"Brian", "food":"soup"}])