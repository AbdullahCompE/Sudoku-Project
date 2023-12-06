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

# game variables
game_over = False
win = False
game_menu = True
enter_key = False

# intialize font
font_title = pygame.font.Font('freesansbold.ttf', 50)
font_subtitle = pygame.font.Font('freesansbold.ttf', 40)
text_color = (0, 0, 0)

difficulty = 0

WIDTH = 600
HEIGHT = 700
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
    reset_button = sudoku_generator.Button(25, 630, reset_img, 0.4)
    restart_button = sudoku_generator.Button(210, 630, restart_img, 0.4)
    exit_button = sudoku_generator.Button(450, 630, exit_img, 0.4)





    #title screen

    #clock = pygame.time.Clock()

    run = True
    while run:
        # Process player inputs.

        # Background Color
        screen.fill(BACKGROUND_COLOR)

        if game_menu:
            draw_text("Welcome to Sudoku!", font_title, text_color, 50, 150)
            draw_text("Select Difficulty:", font_subtitle, text_color, 150, 350)
            # gets difficulty from the buttons on start menu
            if easy_button.draw(screen):
                difficulty = 30
                game_menu = False
            if medium_button.draw(screen):
                difficulty = 40
                game_menu = False
            if hard_button.draw(screen):
                difficulty = 50
                game_menu = False

        if not game_menu:
            board_initialize = sudoku_generator.Board(WIDTH, HEIGHT, screen, difficulty)
            board_initialize.draw()

            board = board_initialize.board
            print(board)
            for k in range(50, WIDTH, int(WIDTH / 3)):
                for i in range(0, 2):
                    for j in range(0, 2):
                        draw_text(str(board[i][j]), font_title, text_color, k, k+20)

            # game-in-progress menu buttons
            if reset_button.draw(screen):
                pass
            if restart_button.draw(screen):
                sudoku_generator.Board.reset_to_original()

            if exit_button.draw(screen):
                run = False



        # Print Start menu

        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    enter_key = True

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
