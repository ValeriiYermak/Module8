import collections


Cat = collections.namedtuple("Cat", ["nickname", "age", "owner"])

def convert_list(cats):

    result = []

    for element in cats:
        if isinstance(element, dict) == True:
            result.append(Cat(element["nickname"], element["age"], element["owner"]))
           
        if isinstance(element, tuple) == True:
            result.append({"nickname": element.nickname, "age": element.age, "owner": element.owner})
           
    return result
    