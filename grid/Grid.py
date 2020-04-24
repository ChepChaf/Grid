from .GridArray import GridArray


class Grid:
    def __init__(self, width, height):
        self.shape = [width, height]

        self.columns = GridArray()
        self.rows = GridArray()
        self.diagonals = GridArray()

        for _ in range(width):
            self.columns.append(GridArray(n=height))

        for _ in range(height):
            self.rows.append(GridArray(n=width))

        self.diagonals = GridArray()

    def __getitem__(self, index):
        return self.columns[index]

    def __setitem__(self, x, value):
        self.rows.set_value(x, value)

        self._update_columns()
        self._update_diagonals()

    def __repr__(self):
        return "\n".join([str(r) for r in self.rows])

    def set_value(self, x, y, value):
        self.rows[y].set_value(x, value)
        self.columns[x].set_value(y, value)

        self._update_diagonals()

    def set_values(self, grid_values):
        if len(grid_values) != self.shape[0]:
            print("Error X shape should be: {}".format(self.shape[0]))
            return

        for r in grid_values:
            if len(r) != self.shape[1]:
                print("Error Y shape should be: {}".format(self.shape[1]))
                return

        for i, r in enumerate(grid_values):
            self.rows.set_value(i, GridArray(elements=r))
        self._update_columns()
        self._update_diagonals()

    def _update_diagonals(self):
        self.diagonals = GridArray()
        if self.shape[0] == self.shape[1]:
            self.diagonals.append(
                GridArray(
                    elements=[self.rows[x][y] for x, y in zip(range(self.shape[0]), range(self.shape[1]))])
            )
            self.diagonals.append(
                GridArray(elements=[self.rows[x][y] for x, y in zip(
                    range(self.shape[0]), range(self.shape[1] - 1, -1, -1))]
                )
            )

    def _update_columns(self):
        for i in range(self.shape[0]):
            self.columns.set_value(i, GridArray(
                elements=[self.rows[x][i] for x in range(self.shape[1])]))

    def repeated(self, value):
        for r in self.rows:
            if r.repeated(value):
                return True
        for c in self.columns:
            if c.repeated(value):
                return True
        for d in self.diagonals:
            if d.repeated(value):
                return True
        return False

    def has_repeated(self):
        for r in self.rows:
            if r.has_repeated():
                return True
        for c in self.columns:
            if c.has_repeated():
                return True
        for d in self.diagonals:
            if d.has_repeated():
                return True
        return False

    def repeated_count(self, value):
        appearances = 0
        for r in self.rows:
            appearances += r.repeated_count(value)

        return appearances

    def is_empty(self):
        for r in self.rows:
            if not r.is_empty():
                return False
        return True

    def empty_positions(self):
        if self.is_empty():
            return self.shape[0] * self.shape[1]

        empty_pos = 0

        for r in self.rows:
            for el in r:
                if el == None:
                    empty_pos += 1

        return empty_pos
