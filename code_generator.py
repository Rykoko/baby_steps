message = input('What would you like to encode? ')


def encode(word):
    replacements = [('a', '£'), ('e', '$'), ('i', '€'), ('o', '§'), ('u', '@'),
                    ('b', '1'), ('c', '2'), ('d', '3'), ('f', '4'), ('g', '5'),
                    ('h', '6'), ('j', '#'), ('k', '7'), ('l', '8'), ('m', '9'),
                    ('n', '!'), ('p', ';'), ('r', '^'), ('s', '/'), ('t', '"'),
                    ('v', '*'), ('w', 'ç'), ('x', '&'), ('y', '£'), ('z', '?')]
    for (x, y) in replacements:
        word = word.replace(x, y)
    return word


print(encode(message))
