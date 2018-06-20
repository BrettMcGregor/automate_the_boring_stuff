
spam = ["apples", "bananas", "tofu", "cats"]


def comma_code(coll):
    return " ".join(coll[:-1]) + " and " + coll[-1]


print(comma_code(spam))
