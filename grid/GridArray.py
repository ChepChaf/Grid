from copy import copy

class GridArray:
    def __init__(self, elements=[]):
        self.elements = copy(elements)

    # We want this class to be subscriptable
    def __getitem__(self, i):
        return self.elements[i]

    def __sizeof__(self):
        return len(self.elements)

    def __iter__(self):
        for el in self.elements:
            yield el

    def __setitem__(self, index, value):
        self.elements[index] = value

    def __repr__(self):
        return "[" + " ".join(str(self.elements)) + "]"

    def __eq__(self, other):
        if type(other) == type(self):
            return other.elements == self.elements
        return self.elements == other

    def is_empty(self):
        return len(self.elements) == 0

    def append(self, element):
        self.elements.append(element)

    def has_repeated(self):
        return len(self.elements) > len(set(self.elements))

    def repeated(self, value):
        frequency = 0
        for el in self.elements:
            if el == value:
                frequency += 1

        return frequency > 1
