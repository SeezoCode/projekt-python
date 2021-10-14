import collections


def char_frequency(filename: str):
    arr = []
    with open(filename, 'r') as file:
        for line in file:
            line = line.lower()
            arr.append(collections.Counter(line).most_common())
            # arr.append(most_common(line))
    return arr


def most_common(string: str):
    zipped = [list(a) for a in zip(set(string), [0] * len(string))]
    
    for letter in string:
        for t in zipped:
            if t[0] == letter:
                t[1] += 1

    zipped.sort(key=lambda el: el[1], reverse=True)
    return zipped
