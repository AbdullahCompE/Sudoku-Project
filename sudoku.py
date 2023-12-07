import pygame, sudoku_generator
from pygame.locals import *
import sys

def wait():
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN and event.key == K_f:
                return

pygame.init()

#function to draw text
def draw_text(text, font, text_col, x, y):
    img = font.render(text, True, text_col)
    screen.blit(img, (x, y))

# screen variables
game_over_screen = False
win_screen = False
game_menu_screen = True
game_running_screen = False


# game variables
enter_key = False
initialized_board = True
x, y = 1, 1

# intialize font
font_title = pygame.font.Font('freesansbold.ttf', 50)
font_subtitle = pygame.font.Font('freesansbold.ttf', 40)
text_color = (0, 0, 0)

difficulty = 0

WIDTH = 630
HEIGHT = 730
# LINE_WIDTH =
# BOARD_ROWS =
# BOARD_COLS =
# SQUARE_SIZE =
BACKGROUND_COLOR = (250, 250, 230)
RED = (255, 0, 0)
LINE_COLOR = (27, 27, 27)
TEMP_CHIP_COLOR = (171, 176, 172)
CHIP_COLOR = (27, 27, 27)
GRAY = (170, 170, 170)

if __name__ == "__main__":
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Sudoku")



    # load button images
    easy_img = pygame.image.load('easy_btn.png').convert_alpha()
    medium_img = pygame.image.load('medium_btn.png').convert_alpha()
    hard_img = pygame.image.load('hard_btn.png').convert_alpha()
    reset_img = pygame.image.load('reset_btn.png').convert_alpha()
    restart_img = pygame.image.load('restart_btn.png').convert_alpha()
    exit_img = pygame.image.load('exit_btn.png').convert_alpha()



    # button instances
    easy_button = sudoku_generator.Button(50, 450, easy_img, 0.4)
    medium_button = sudoku_generator.Button(200, 450, medium_img, 0.4)
    hard_button = sudoku_generator.Button(425, 450, hard_img, 0.4)
    reset_button = sudoku_generator.Button(25, 660, reset_img, 0.4)
    restart_button = sudoku_generator.Button(225, 660, restart_img, 0.4)
    exit_button = sudoku_generator.Button(475, 660, exit_img, 0.4)






    #title screen

    #clock = pygame.time.Clock()

    run = True
    while run:
        # Process player inputs.

        # Background Color
        screen.fill(BACKGROUND_COLOR)

        # Print Start menu
        if game_menu_screen:
            draw_text("Welcome to Sudoku!", font_title, text_color, 50, 150)
            draw_text("Select Difficulty:", font_subtitle, text_color, 150, 350)
            # gets difficulty from the buttons on start menu
            if easy_button.draw(screen):
                difficulty = 30

                game_menu_screen = False
                game_running_screen = True
            if medium_button.draw(screen):
                difficulty = 40
                game_menu_screen = False
                game_running_screen = True
            if hard_button.draw(screen):
                difficulty = 50
                game_menu_screen = False
                game_running_screen = True

        if game_running_screen:
            if initialized_board:
                board_initialize = sudoku_generator.Board(9, 9, screen, difficulty)
                initialized_board = False
            board_initialize.draw()
            initial_board = board_initialize.board
            board = initial_board.copy()

            #print(board)

            for i in range(0, 9):
                for j in range(0, 9):
                    if initial_board[i][j] == 0:
                        active_cell = sudoku_generator.Cell(' ', i, j, screen)

                        if active_cell.draw():
                            y, x = active_cell.draw()

                        continue
                    else:

                        active_cell = sudoku_generator.Cell(board[i][j], i, j, screen)

                        if active_cell.draw():
                            y, x = active_cell.draw()


            for i in range(0, 9):
                for j in range(0, 9):
                    if board[i][j] == 0:
                        active_cell = sudoku_generator.Cell(' ', i, j, screen)

                        if active_cell.draw():
                            y, x = active_cell.draw()

                        continue
                    else:

                        active_cell = sudoku_generator.Cell(board[i][j], i, j, screen)

                        if active_cell.draw():
                            y, x = active_cell.draw()


            board_initialize.draw()
            board_initialize.highlight_cell(x, y)



            # game-in-progress menu buttons
            if reset_button.draw(screen):
                sudoku_generator.Board.reset_to_original()
                pass
            if restart_button.draw(screen):
                game_running_screen = False
                game_menu_screen = True
                initialized_board = True

            if exit_button.draw(screen):
                run = False

        if game_over_screen:
            pass

        if win_screen:
            pass




        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    enter_key = True
                if event.key == pygame.K_1:
                    board[x][y]= 1
                if event.key == pygame.K_2:
                    board[x][y]= 2
                if event.key == pygame.K_3:
                    board[x][y]= 3
                if event.key == pygame.K_4:
                    board[x][y]= 4
                if event.key == pygame.K_5:
                    board[x][y]= 5
                if event.key == pygame.K_6:
                    board[x][y]= 6
                if event.key == pygame.K_7:
                    board[x][y]= 7
                if event.key == pygame.K_8:
                    board[x][y]= 8
                if event.key == pygame.K_9:
                    board[x][y]= 9

            if event.type == pygame.QUIT:
                pygame.quit()
                raise SystemExit

        # Do logical updates here.




        # Render the graphics here.
        # ...
        pygame.display.update()



    chip_font = pygame.font.Font(None, 35)
    chip_surfs_1 = [chip_font.render(str(i), 1, GRAY) for i in range(1, 10)]
    chip_1_surf_1 = chip_surfs_1[0]
    chip_2_surf_1 = chip_surfs_1[1]
    chip_3_surf_1 = chip_surfs_1[2]
    chip_4_surf_1 = chip_surfs_1[3]
    chip_5_surf_1 = chip_surfs_1[4]
    chip_6_surf_1 = chip_surfs_1[5]
    chip_7_surf_1 = chip_surfs_1[6]
    chip_8_surf_1 = chip_surfs_1[7]
    chip_9_surf_1 = chip_surfs_1[8]



    # option = draw_game_start(screen)
    # if option == 'easy':
    #     difficulty = 30
    # elif option == 'medium':
    #     difficulty = 40
    # elif option == 'hard':
    #     difficulty = 50
    #
    # board = Board(WIDTH, HEIGHT, screen, difficulty)
    # board.draw()
