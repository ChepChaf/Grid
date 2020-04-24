from copy import copy

class GridArray:
    def __init__(self, n=0, elements=[]):
        self.elements = []
        if len(elements) > 0:
            self.elements = copy(elements)
        elif n > 0:
            self.elements = [None for _ in range(n)]

    # We want this class to be subscriptable
    def __getitem__(self, i):
        return self.elements[i]

    def __hash__(self):
        return hash(str(self))

    def __sizeof__(self):
        return len(self.elements)

    def __iter__(self):
        for el in self.elements:
            yield el

    def set_value(self, index, value):
        self.elements[index] = value

    def __repr__(self):
        return "[" + " ".join(str(self.elements)) + "]"

    def __eq__(self, other):
        if type(other) == type(self):
            return other.elements == self.elements
        return self.elements == other

    def is_empty(self):
        return len(self.elements) == 0 or set(self.elements) == {None}

    def append(self, element):
        self.elements.append(element)

    def has_repeated(self):
        return len(self.elements) > len(set(self.elements))

    def repeated(self, value):
        return self.repeated_count(value) > 1

    def repeated_count(self, value):
        frequency = 0
        for el in self.elements:
            if el == value:
                frequency += 1

        return frequency
