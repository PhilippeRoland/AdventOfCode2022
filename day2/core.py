import os
from utils import read_file, print_lines


def get_moves(lines):
    print_lines(lines)
    print('-----------------------------')
    moves_tuples = [tuple(line.split(' ')) for line in lines if line]
    print(moves_tuples)
    return moves_tuples


def calc_score(moves_tuples):
    scores_tuples = list(map(score_round, moves_tuples))
    print(scores_tuples)
    print('-----------------------------')
    total_score = sum([score_tuple[0] + score_tuple[1] for score_tuple in scores_tuples])
    print(total_score)
    return total_score


def score_round(move_tuple):
    opp_move = move_tuple[0]
    # shift X-Z to A-C for easier comparison
    my_move = chr(ord(move_tuple[1]) - 23)
    # value of the move in pos 0, round result in pos 1
    return move_score(my_move), score_win_loss(opp_move, my_move)


def score_win_loss(opp_move, my_move):
    if my_move == opp_move:
        return 3
    elif (ord(my_move) - ord(opp_move)) % 3 == 1:
        return 6
    else:
        return 0


def move_score(my_move):
    return ord(my_move) - 64


# --------------------------------------------------------------------------------------- #

def calc_score_bis(moves_tuples):
    scores_tuples = list(map(score_round_bis, moves_tuples))
    print(scores_tuples)
    print('-----------------------------')
    total_score = sum([score_tuple[0] + score_tuple[1] for score_tuple in scores_tuples])
    print(total_score)
    return total_score


def score_round_bis(move_tuple):
    opp_move = move_tuple[0]
    # shift X-Z to A-C for easier comparison
    round_result = move_tuple[1]
    my_move_score = calc_my_move_score(opp_move, round_result)
    # value of the move in pos 0, round result in pos 1
    return my_move_score, score_win_loss_bis(round_result)


def calc_my_move_score(opp_move, round_result):
    modifier = 0
    if round_result == 'X':
        modifier = -1
    elif round_result == 'Z':
        modifier = 1
    raw_my_move = ((ord(opp_move) - 64) + modifier) % 3
    return raw_my_move if raw_my_move > 0 else 3


def score_win_loss_bis(round_result):
    if round_result == 'X':
        return 0
    elif round_result == 'Y':
        return 3
    else:
        return 6


if __name__ == '__main__':
    script_dir = os.path.dirname(__file__)
    lines = read_file(os.path.join(script_dir, 'input'))
    moves_tuples = get_moves(lines)
    calc_score(moves_tuples)
    print('----------------------------------------------------------\n'
          '----------------------------------------------------------')
    calc_score_bis(moves_tuples)
