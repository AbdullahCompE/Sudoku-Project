import math, random, pygame, sys

"""
This was adapted from a GeeksforGeeks article "Program for Sudoku Generator" by Aarti_Rathi and Ankur Trisal
https://www.geeksforgeeks.org/program-sudoku-generator/

"""

# WIDTH =
# HEIGHT =
# LINE_WIDTH =
# BOARD_ROWS =
# BOARD_COLS =
# SQUARE_SIZE =
BACKGROUND_COLOR = (255, 255, 255)
RED = (255, 0, 0)
LINE_COLOR = (27, 27, 27)
TEMP_CHIP_COLOR = (171, 176, 172)
CHIP_COLOR = (27, 27, 27)
GRAY = (170, 170, 170)


class SudokuGenerator:
    '''
	create a sudoku board - initialize class variables and set up the 2D board
	This should initialize:
	self.row_length		- the length of each row
	self.removed_cells	- the total number of cells to be removed
	self.board			- a 2D list of ints to represent the board
	self.box_length		- the square root of row_length

	Parameters:
    row_length is the number of rows/columns of the board (always 9 for this project)
    removed_cells is an integer value - the number of cells to be removed

	Return:
	None
    '''

    def __init__(self, row_length, removed_cells):
        self.row_length = row_length
        self.removed_cells = removed_cells
        self.board = [[0 for i in range(self.row_length)] for i in range(self.row_length)]
        self.box_length = int(math.sqrt(row_length))
        pass

    '''
	Returns a 2D python list of numbers which represents the board

	Parameters: None
	Return: list[list]
    '''

    def get_board(self):
        return self.board
        pass

    '''
	Displays the board to the console
    This is not strictly required, but it may be useful for debugging purposes

	Parameters: None
	Return: None
    '''

    def print_board(self):
        for row in self.board:
            print(row)
        pass

    '''
	Determines if num is contained in the specified row (horizontal) of the board
    If num is already in the specified row, return False. Otherwise, return True

	Parameters:
	row is the index of the row we are checking
	num is the value we are looking for in the row

	Return: boolean
    '''

    def valid_in_row(self, row, num):
        if num not in self.board[row]:
            return True
        return False

    '''
	Determines if num is contained in the specified column (vertical) of the board
    If num is already in the specified col, return False. Otherwise, return True

	Parameters:
	col is the index of the column we are checking
	num is the value we are looking for in the column

	Return: boolean
    '''

    def valid_in_col(self, col, num):
        for row in range(self.row_length):
            if num == self.board[row][col]:
                return False
        return True

    '''
	Determines if num is contained in the 3x3 box specified on the board
    If num is in the specified box starting at (row_start, col_start), return False.
    Otherwise, return True

	Parameters:
	row_start and col_start are the starting indices of the box to check
	i.e. the box is from (row_start, col_start) to (row_start+2, col_start+2)
	num is the value we are looking for in the box

	Return: boolean
    '''

    def valid_in_box(self, row_start, col_start, num):
        row_def = row_start - row_start % self.box_length
        col_def = col_start - col_start % self.box_length
        for i in range(row_def, row_def + self.box_length):
            for j in range(col_def, col_def + self.box_length):
                if self.board[i][j] == num:
                    return False
        return True

    '''
    Determines if it is valid to enter num at (row, col) in the board
    This is done by checking that num is unused in the appropriate, row, column, and box

	Parameters:
	row and col are the row index and col index of the cell to check in the board
	num is the value to test if it is safe to enter in this cell

	Return: boolean
    '''

    def is_valid(self, row, col, num):
        if self.valid_in_row(row, num) and self.valid_in_box(row, col, num) and self.valid_in_col(col, num):
            return True
        return False

        pass

    '''
    Fills the specified 3x3 box with values
    For each position, generates a random digit which has not yet been used in the box

	Parameters:
	row_start and col_start are the starting indices of the box to check
	i.e. the box is from (row_start, col_start) to (row_start+2, col_start+2)

	Return: None
    '''

    def fill_box(self, row_start, col_start):
        nums = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        random.shuffle(nums)
        for i in range(row_start, row_start + self.box_length):
            for j in range(col_start, col_start + self.box_length):
                self.board[i][j] = nums.pop()
        pass

    '''
    Fills the three boxes along the main diagonal of the board
    These are the boxes which start at (0,0), (3,3), and (6,6)

	Parameters: None
	Return: None
    '''

    def fill_diagonal(self):
        for i in range(0, self.row_length, self.box_length):
            self.fill_box(i, i)
        pass

    '''
    DO NOT CHANGE
    Provided for students
    Fills the remaining cells of the board
    Should be called after the diagonal boxes have been filled

	Parameters:
	row, col specify the coordinates of the first empty (0) cell

	Return:
	boolean (whether or not we could solve the board)
    '''

    def fill_remaining(self, row, col):
        if (col >= self.row_length and row < self.row_length - 1):
            row += 1
            col = 0
        if row >= self.row_length and col >= self.row_length:
            return True
        if row < self.box_length:
            if col < self.box_length:
                col = self.box_length
        elif row < self.row_length - self.box_length:
            if col == int(row // self.box_length * self.box_length):
                col += self.box_length
        else:
            if col == self.row_length - self.box_length:
                row += 1
                col = 0
                if row >= self.row_length:
                    return True

        for num in range(1, self.row_length + 1):
            if self.is_valid(row, col, num):
                self.board[row][col] = num
                if self.fill_remaining(row, col + 1):
                    return True
                self.board[row][col] = 0
        return False

    '''
    DO NOT CHANGE
    Provided for students
    Constructs a solution by calling fill_diagonal and fill_remaining

	Parameters: None
	Return: None
    '''

    def fill_values(self):
        self.fill_diagonal()
        self.fill_remaining(0, self.box_length)

    '''
    Removes the appropriate number of cells from the board
    This is done by setting some values to 0
    Should be called after the entire solution has been constructed
    i.e. after fill_values has been called

    NOTE: Be careful not to 'remove' the same cell multiple times
    i.e. if a cell is already 0, it cannot be removed again

	Parameters: None
	Return: None
    '''

    def remove_cells(self):
        cells_removed = 0
        while cells_removed < self.removed_cells:
            row = random.randint(0, self.row_length - 1)
            col = random.randint(0, self.row_length - 1)
            if self.board[row][col] != 0:
                self.board[row][col] = 0
                cells_removed += 1
        pass


'''
DO NOT CHANGE
Provided for students
Given a number of rows and number of cells to remove, this function:
1. creates a SudokuGenerator
2. fills its values and saves this as the solved state
3. removes the appropriate number of cells
4. returns the representative 2D Python Lists of the board and solution

Parameters:
size is the number of rows/columns of the board (9 for this project)
removed is the number of cells to clear (set to 0)

Return: list[list] (a 2D Python list to represent the board)
'''


def generate_sudoku(size, removed):
    sudoku = SudokuGenerator(size, removed)
    sudoku.fill_values()
    board = sudoku.get_board()
    sudoku.remove_cells()
    board = sudoku.get_board()
    return board


class Click_cell:
    def __init__(self, x, y, image, scale):
        width = image.get_width()
        height = image.get_height()
        self.image = pygame.transform.scale(image, (int(width * scale), int(height * scale)))
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)
        self.clicked = False

    def draw(self, surface):
        action = False
        # get mouse position
        pos = pygame.mouse.get_pos()

        if self.rect.collidepoint(pos):
            if pygame.mouse.get_pressed()[0] == 1 and self.clicked == False:
                self.clicked = True
                action = True

            if pygame.mouse.get_pressed()[0] == 0:
                self.clicked = False

        surface.blit(self.image, (self.rect.x, self.rect.y))
        return action

    pass


class Button:
    def __init__(self, x, y, image, scale):
        width = image.get_width()
        height = image.get_height()
        self.image = pygame.transform.scale(image, (int(width * scale), int(height * scale)))
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)
        self.clicked = False

    def draw(self, surface):
        action = False
        # get mouse position
        pos = pygame.mouse.get_pos()

        if self.rect.collidepoint(pos):
            if pygame.mouse.get_pressed()[0] == 1 and self.clicked == False:
                self.clicked = True
                action = True

            if pygame.mouse.get_pressed()[0] == 0:
                self.clicked = False

        surface.blit(self.image, (self.rect.x, self.rect.y))
        return action


class Cell:
    def __init__(self, value, row, col, screen, text_col):
        self.value = value
        self.row = row
        self.col = col
        self.screen = screen

        self.sketched_value = value
        self.selected = False
        self.line_color_grey = (132, 132, 132)
        self.text_col = text_col

    def set_cell_value(self, value):
        self.value = value

    def set_sketched_value(self, value):
        self.sketched_value = value

    def draw(self):
        cell_size = 70  # Define the size of each cell
        cell_x = self.col * cell_size
        cell_y = self.row * cell_size
        self.clicked = False

        pygame.draw.rect(self.screen, self.line_color_grey, (cell_x, cell_y, cell_size, cell_size),
                         1)  # Example rectangle for cell
        font = pygame.font.Font('freesansbold.ttf', 50,)
        text = font.render(str(self.value), True, self.text_col)  # Example cell value text
        self.text_rect = text.get_rect(
            center=(cell_x + cell_size // 2, cell_y + cell_size // 2))  # Example text position

        action = False
        # get mouse position
        pos = pygame.mouse.get_pos()

        if self.text_rect.collidepoint(pos):
            if pygame.mouse.get_pressed()[0] == 1 and self.clicked == False:
                self.clicked = True
                action = True
                x, y = pos
                return x // 70, y // 70

            if pygame.mouse.get_pressed()[0] == 0:
                self.clicked = False

        # surface.blit(self.image, (self.rect.x, self.rect.y))
        self.screen.blit(text, self.text_rect)  # Drawing the text on the cell

    # def draw(self):
    #     # Draws this cell and its nonzero value, otherwise no value displayed
    #     chip_font = pygame.font.Font(None, 60)
    #     chip_surfs = [chip_font.render(str(i), 1, LINE_COLOR) for i in range(1, 10)]
    #     chip_rects = [None] * 9
    #     for i in range(9):
    #         chip_rects[i] = chip_surfs[i].get_rect(
    #             center=(self.col * SQUARE_SIZE + SQUARE_SIZE // 2,
    #                     self.row * SQUARE_SIZE + SQUARE_SIZE // 2 + 3))
    #         self.screen.blit(chip_surfs[i], chip_rects[i])
    #     if self.selected:
    #         pygame.draw.rect(screen, RED,
    #                          pygame.Rect(
    #                              self.col * SQUARE_SIZE, self.row * SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE), 3)
    #         self.selected = False
    #     if self.value != 0:
    #         chip_rect = chip_rects[self.value - 1]
    #         self.screen.blit(chip_surfs[self.value - 1], chip_rect)
    #     pygame.display.update()


class Board:
    def __init__(self, width, height, screen, difficulty):
        self.width = width * 70
        self.height = height * 70 + 100
        self.screen = screen
        self.difficulty = difficulty
        self.board = generate_sudoku(9, self.difficulty)

        self.line_thickness_cell = 2
        self.line_thickness_box = 5
        self.line_color_black = (0, 0, 0)
        self.line_color_grey = (132, 132, 132)
        self.menu_space = 100

    def draw(self):
        # Horizontal thin lines
        # for i in range(1, 9):
        #     pygame.draw.line(self.screen, self.line_color_grey, ((self.width / 9) * i, 0), ((self.width / 9) * i, self.height - self.menu_space), self.line_thickness_cell)
        # # vertical thin lines
        #     pygame.draw.line(self.screen, self.line_color_grey, (0, ((self.height-self.menu_space) / 9) * i), (self.width, ((self.height - self.menu_space)/ 9) * i), self.line_thickness_cell)

        # Thick lines
        for i in range(1, 4):
            # Horizontal
            pygame.draw.line(self.screen, self.line_color_black, (0, ((self.height - self.menu_space) / 3) * i),
                             (self.width, ((self.height - self.menu_space) / 3) * i), self.line_thickness_box)
        # vertical
        for i in range(1, 3):
            pygame.draw.line(self.screen, self.line_color_black, ((self.width / 3) * i, 0),
                             ((self.width / 3) * i, self.height - self.menu_space), self.line_thickness_box)


    def check_for_win(self, board):
        for row in range(9):
            for col in range(9):
                num = board[row][col]
                if num == 0:
                    return False  # found an empty cell
                else:
                    # check if number is valid in row
                    if board[row].count(num) > 1:
                        return False

                    # check if number is valid in column
                    for r in range(9):
                        if num == board[r][col]:
                            return False

                    # check if number is valid in box
                    row_def = row - row % 3
                    col_def = col - col % 3
                    for i in range(row_def, row_def + 3):
                        for j in range(col_def, col_def + 3):
                            if board[i][j] == num:
                                return False
        return True  # no empty or repeated numbers found


    def select(self, row, col):
        # deselect previous cell
        self.cells[self.selected_row][self.selected_col].selected = True

        # select a new cell
        if row in range(9) and col in range(9):
            self.row = row
            self.col = col
        self.cells[self.selected_row][self.selected_col].selected = True

    def click(self, x, y):
        width_cell = self.width // 9
        height_cell = self.height // 9
        click_row = x // width_cell
        click_col = y // height_cell
        cell = (click_row, click_col)
        return cell

    def clear(self):


        pass

    def sketch(self, value):
        self.sketch = value
        pass

    def place_number(self, value):
        self.number = value
        pass

    def reset_to_original(self):
        for i in range(9):
            for j in range(9):
                self.cells[row][col].reset_to_original()
        pass

    def is_full(self):
        for i in range(9):
            for j in range(9):
                if self.cells[row][col].get_value() == 0:
                    return False
        pass

    def update_board(self):
        for i in range(9):
            for j in range(9):
                self.cells[row][col].update()
        pass

    def find_empty(self):
        for i in range(9):
            for j in range(9):
                if self.cells[row][col].get_value() == 0:
                    return (row, col)

    def check_board(self):
        for i in range(9):
            values = set()
            for j in range(9):
                value = self.cells[row][col].get_value()
                if value != 0:
                    if value in values:
                        return False
                    values.add(value)
        pass

    def highlight_cell(self, x, y):
        pygame.draw.rect(self.screen, (255, 0, 0), (y * 70, x * 70, 70, 70), 3)


