from unittest import TestCase
from grid import Grid


class EmptyGrid(TestCase):
    def setUp(self):
        self.grid = Grid(3, 3)

    def test_gridIsEmpty(self):
        self.assertTrue(self.grid.is_empty())

    def test_allRowsAreEmpty(self):
        for row in self.grid.rows:
            self.assertTrue(row.is_empty())

    def test_allColumnsAreEmpty(self):
        for col in self.grid.columns:
            self.assertTrue(col.is_empty())

    def test_emptyPositionCount(self):
        self.assertEqual(self.grid.empty_positions(), 9)

        self.grid.set_value(1, 1, 1)

        self.assertEqual(self.grid.empty_positions(), 8)

    def test_setValueByIndex(self):
        self.grid.set_value(1, 1, 1)

        self.assertEqual(self.grid.rows[1][1], 1)
        self.assertEqual(self.grid.columns[1][1], 1)
        self.assertEqual(self.grid.diagonals[0][1], 1)
        self.assertEqual(self.grid.diagonals[1][1], 1)

        self.grid.set_value(0, 1, 'X')

        self.assertEqual(self.grid.rows[1][0], 'X')
        self.assertEqual(self.grid.columns[0][1], 'X')

class GridWithNonRepeatedValues(TestCase):
    def setUp(self):
        self.grid = Grid(3, 3)
        self.grid.set_values([[1, 2, 3], [4, 5, 6], [7, 8, 9]])

    def test_getElementWithIndexes(self):
        self.assertEqual(self.grid[0][0], 1)
        self.assertEqual(self.grid[0][1], 4)
        self.assertEqual(self.grid[0][2], 7)
        self.assertEqual(self.grid[1][0], 2)
        self.assertEqual(self.grid[1][1], 5)
        self.assertEqual(self.grid[1][2], 8)
        self.assertEqual(self.grid[2][0], 3)
        self.assertEqual(self.grid[2][1], 6)
        self.assertEqual(self.grid[2][2], 9)

    def test_rowsCountsAreCorrect(self):
        self.assertEqual(len(self.grid.rows.elements), 3)

    def test_columnsCountsAreCorrect(self):
        self.assertEqual(len(self.grid.columns.elements), 3)

    def test_rowValuesAreCorrect(self):
        self.assertEqual(self.grid.rows[0], [1, 2, 3])
        self.assertEqual(self.grid.rows[1], [4, 5, 6])
        self.assertEqual(self.grid.rows[2], [7, 8, 9])

    def test_columnValuesAreCorrect(self):
        self.assertEqual(self.grid.columns[0], [1, 4, 7])
        self.assertEqual(self.grid.columns[1], [2, 5, 8])
        self.assertEqual(self.grid.columns[2], [3, 6, 9])

    def test_diagonalValuesAreCorrect(self):
        self.assertEqual(self.grid.diagonals[0], [1, 5, 9])
        self.assertEqual(self.grid.diagonals[1], [3, 5, 7])

    def test_gridIsNotEmpty(self):
        self.assertFalse(self.grid.is_empty())

    def test_rowsColumnsAndDiagonalsAreNotEmpty(self):
        self.assertFalse(self.grid.rows.is_empty())
        self.assertFalse(self.grid.columns.is_empty())
        self.assertFalse(self.grid.diagonals.is_empty())

    def test_setValue(self):
        self.grid.set_value(1, 1, 10)

        self.assertEqual(self.grid.rows[1], [4, 10, 6])

        self.assertEqual(self.grid.columns[1], [2, 10, 8])

        self.assertEqual(self.grid.diagonals[0], [1, 10, 9])
        self.assertEqual(self.grid.diagonals[1], [3, 10, 7])

    def test_setValues(self):
        self.grid.set_values([[2, 3, 4], [5, 6, 7], [8, 9, 10]])

        self.assertEqual(self.grid.rows[0], [2, 3, 4])
        self.assertEqual(self.grid.rows[1], [5, 6, 7])
        self.assertEqual(self.grid.rows[2], [8, 9, 10])


class GridWithRepeatedValues(TestCase):
    def setUp(self):
        self.grid = Grid(3, 3)
        self.grid.set_values([[1, 2, 4], [3, 3, 4], [4, 4, 4]])

    def test_hasRepeated(self):
        self.assertTrue(self.grid.has_repeated())

        self.assertFalse(self.grid.columns[0].has_repeated())

        self.assertFalse(self.grid.columns[1].has_repeated())
        self.assertTrue(self.grid.columns[2].has_repeated())

        self.assertFalse(self.grid.rows[0].has_repeated())
        self.assertTrue(self.grid.rows[1].has_repeated())
        self.assertTrue(self.grid.rows[2].has_repeated())

    def test_valueRepeated(self):
        self.assertFalse(self.grid.repeated(1))
        self.assertFalse(self.grid.repeated(2))
        self.assertTrue(self.grid.repeated(3))
        self.assertTrue(self.grid.repeated(4))

        self.assertFalse(self.grid.rows[0].repeated(1))
        self.assertFalse(self.grid.rows[0].repeated(2))
        self.assertFalse(self.grid.rows[0].repeated(4))

        self.assertTrue(self.grid.rows[1].repeated(3))
        self.assertFalse(self.grid.rows[1].repeated(4))

        self.assertTrue(self.grid.rows[2].repeated(4))

    def test_repeatedCount(self):
        self.assertEqual(self.grid.repeated_count(3), 2)
        self.assertEqual(self.grid.repeated_count(1), 1)

        self.assertEqual(self.grid.columns[2].repeated_count(4), 3)
        self.assertEqual(self.grid.rows[1].repeated_count(3), 2)
