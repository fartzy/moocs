"""
User - doing the two for loops creates a strign that is stored in a collection 
    So 100 x 100 means 10,000 names are stored. 
User2 - storing only 200 names (100 first and 100 last) and the __str__ method 
    actually displays them to screen without having them stored.  So basically 
    there is more computation done and less storage before the value is returned
"""
import string
import random


class User:
    def __init__(self, name):
        self.name = name


class User2:
    strings = []

    def __init__(self, full_name):
        def get_or_add(s):
            if s in self.strings:
                return self.strings.index(s)
            else:
                self.strings.append(s)
                return len(self.strings) - 1

        self.names = [get_or_add(x) for x in full_name.split(" ")]

    def __str__(self):
        return " ".join([self.strings[x] for x in self.names])


def random_string():
    chars = string.ascii_lowercase

    return "".join([random.choice(chars) for x in range(8)])


if __name__ == "__main__":
    users = []

    first_names = [random_string() for x in range(100)]
    last_names = [random_string() for x in range(100)]

    for first in first_names:
        for last in last_names:
            users.append(User2(f"{first} {last}"))

    print(users[0])