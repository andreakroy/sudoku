class puzzle:
    """
    Puzzle class to store a single sudoku puzzle.
    """
    def __init__(self, puzzle):
        """
        Initializes a puzzle from a puzzle string.
        A puzzle string consists of 81 characters, where each set of 9 characters 
        is a single row. Blank cells are represented by a 0.
        """
        self.puzzle = [[0] * 9] * 9
        assert len(puzzle) == 81
        for i in range(9):
            for j in range(9):
                self.puzzle[i][j] = int(puzzle[9 * i + j])
    


    def __str__(self):
        """
        Returns a grid representation of a puzzle.
        """
        out = []
        for row in self.puzzle:
            r = []
            for val in row:
                r.append(str(val))
            out.append(' '.join(r))
        return '\n'.join(out)