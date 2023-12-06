import pygame, sudoku_generator
from sudoku_generator import Board

WIDTH = 600
HEIGHT = 600
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
    screen.fill(BACKGROUND_COLOR)
    game_over = False
    win = False


    #title screen
    pygame.init()
    clock = pygame.time.Clock()
    pygame.display.set_caption("Sudoku")

    while True:
        # Process player inputs.

        # gets mouse input
        #Board.click(pygame.mouse.get_pos())


        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                raise SystemExit

        # Do logical updates here.
        # option = draw_game_start(screen)
        option = 'easy'
        if option == 'easy':
            difficulty = 30
        elif option == 'medium':
            difficulty = 40
        elif option == 'hard':
            difficulty = 50

        board = Board(WIDTH, HEIGHT, screen, difficulty)
        board.draw()

        # Render the graphics here.
        # ...

        pygame.display.flip()  # Refresh on-screen display
        clock.tick(60)  # wait until next frame (at 60 FPS)


    chip_font = pygame.font.Font(None, 35)
    chip_surfs_1 = [chip_font.render(str(i), 1, Gray) for i in range(1, 10)]
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
    if option == 'easy':
        difficulty = 30
    elif option == 'medium':
        difficulty = 40
    elif option == 'hard':
        difficulty = 50

    board = Board(WIDTH, HEIGHT, screen, difficulty)
    board.draw()
