from .GridArray import GridArray


class Grid:
    def __init__(self, width, height):
        self.shape = [width, height]

        self.columns = GridArray()
        self.rows = GridArray()
        self.diagonals = GridArray()

        for _ in range(width):
            self.columns.append(GridArray())

        for _ in range(height):
            self.rows.append(GridArray())

        self.diagonals = GridArray()

    def set_value(self, x, y, value):
        self.rows[y][x] = value
        self.columns[x][y] = value

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
            self.rows[i] = GridArray(r)
        self._update_columns()
        self._update_diagonals()

    def _update_diagonals(self):
        self.diagonals = GridArray()
        if self.shape[0] == self.shape[1]:
            self.diagonals.append(
                GridArray(
                    [self.rows[x][y] for x, y in zip(range(self.shape[0]), range(self.shape[1]))])
            )
            self.diagonals.append(
                GridArray([self.rows[x][y] for x, y in zip(
                    range(self.shape[0]), range(self.shape[1] - 1, -1, -1))]
                )
            )

    def _update_columns(self):
        for i in range(self.shape[0]):
            self.columns[i] = GridArray(
                [self.rows[x][i] for x in range(self.shape[1])])

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

    def is_empty(self):
        for r in self.rows:
            if not r.is_empty():
                return False
        return True
