from game import goboard
from game import gotypes
#from game.gotypes import COLS
from game.agent import naive
from game.utils import print_board, print_move, COLS
import time
import pygame

width = 1280
height = 720

margin_width  = 280
margin_height = 70

board_size = 9

def main():
    pygame.init()
    print(COLS)
    font = pygame.font.SysFont('arial', 22)
    screen = pygame.display.set_mode((1280, 720))
    clock = pygame.time.Clock()
    running = True

    game = goboard.GameState.new_game(board_size)

    bots = {
        gotypes.Player.black: naive.RandomBot(),
        gotypes.Player.white: naive.RandomBot(),
    }

    delta_x = (width - 2 * margin_width) / (board_size - 1)
    delta_y = (height - 2 * margin_height) / (board_size - 1)
    circle_radius = min(delta_x, delta_y) // 2.4

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        if not game.is_over():
            bot_move = bots[game.next_player].select_move(game)
            print_move(game.next_player, bot_move)
            game = game.apply_move(bot_move)

        screen.fill(pygame.Color("#966F33"))

        for hor_line in range(0, board_size):
            text_surf = font.render(str(board_size - hor_line), True, pygame.Color("#FFFFFF"))
            text_rect = text_surf.get_rect(center=(margin_width - 40, margin_height + delta_y * hor_line))
            screen.blit(text_surf, text_rect)
            pygame.draw.line(screen, "black", (margin_width, int(margin_height + delta_y * hor_line)), (width - margin_width, int(margin_height + delta_y * hor_line)))

        for ver_line in range(0, board_size):
            text_surf = font.render(COLS[ver_line], True, pygame.Color("#FFFFFF"))
            text_rect = text_surf.get_rect(center=(margin_width + delta_x * ver_line, height - 20))
            screen.blit(text_surf, text_rect)
            pygame.draw.line(screen, "black", (int(margin_width + delta_x * ver_line), margin_height), (int(margin_width + delta_x * ver_line), height - margin_height))

        for row in range(0, board_size):
            for col in range(0, board_size):
                point = game.board.get(gotypes.Point(row+1, col+1))
                if point is not None:
                    color_circle = "black" if point == gotypes.Player.black else "white"
                    pygame.draw.circle(screen, color_circle, (margin_width + col * delta_x, margin_height + (board_size - row - 1) * delta_y), circle_radius)

        pygame.display.flip()

        clock.tick(60)

    pygame.quit()


if __name__ == '__main__':
    main()
