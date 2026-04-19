from game.agent import naive
from game import goboard
from game import gotypes
from game.utils import print_board, print_move, point_from_coords
from six.moves import input

def main():
    board_size = 9
    game = goboard.GameState.new_game(board_size)
    bot = naive.RandomBot()

    while not game.is_over():
        print(chr(27) + "[2J")
        print_board(game.board)

        if game.next_player == gotypes.Player.black:
            made_move = False

            while not made_move:
                print('Enter any cell or "pass" or "resign"')
                human_move = input('-- ')
                human_move = human_move.strip()

                try:
                    if human_move == 'pass':
                        move = goboard.Move.pass_turn()
                    elif human_move == 'resign':
                        move = goboard.Move.resign()
                    else:
                        point = point_from_coords(human_move)

                        if game.board.get(point) is not None:
                            raise ExceptionError

                        move = goboard.Move.play(point)
                except:
                    print('! Invalid move. Try again!')
                else:
                    made_move = True

        else:
            move = bot.select_move(game)

        print_move(game.next_player, move)
        game = game.apply_move(move)

if __name__ == '__main__':
    main()
