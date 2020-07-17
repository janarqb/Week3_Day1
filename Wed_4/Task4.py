a = {'a': 5, 'b': 3, 'c': 8, 'd': 14}
newdict = {key: ('Foo' if value % 3 == 0 else 'Bar' if value % 5 == 0 else value) for (key, value) in a.items()}
print(newdict)