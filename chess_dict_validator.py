import functools

board = {'1h': 'bking', '6c': 'wqueen', '2g': 'bbishop', '5h': 'bqueen', '3e': 'wking'}

def is_valid_chess_board(dict):
    w_pieces = list(filter(lambda p: p[0] == 'w', list(dict.values())))
    w_pieces_number = len(w_pieces)
    w_pieces_number_king = len(list(filter(lambda p: p[1] == 'k', w_pieces)))
    w_pieces_number_queen = len(list(filter(lambda p: p[1] == 'q', w_pieces)))
    w_pieces_number_bishop = len(list(filter(lambda p: p[1] == 'b', w_pieces)))
    w_pieces_number_knight = len(list(filter(lambda p: p[1] == 'n', w_pieces)))
    w_pieces_number_rook = len(list(filter(lambda p: p[1] == 'r', w_pieces)))
    w_pieces_number_pawn = len(list(filter(lambda p: p[1] == 'p', w_pieces)))


    b_pieces = list(filter(lambda p: p[0] == 'b', list(dict.values())))
    b_pieces_number = len(b_pieces)
    b_pieces_number_king = len(list(filter(lambda p: p[1] == 'k', b_pieces)))
    b_pieces_number_queen = len(list(filter(lambda p: p[1] == 'q', b_pieces)))
    b_pieces_number_bishop = len(list(filter(lambda p: p[1] == 'b', b_pieces)))
    b_pieces_number_knight = len(list(filter(lambda p: p[1] == 'n', b_pieces)))
    b_pieces_number_rook = len(list(filter(lambda p: p[1] == 'r', b_pieces)))
    b_pieces_number_pawn = len(list(filter(lambda p: p[1] == 'p', b_pieces)))

    pieces_valid_places_number = len(list(filter(lambda p: 0 <= int(p[0]) <= 8, list(dict.keys()))))
    pieces_valid_places_letter = len(list(filter(lambda p: 'a' <= p[1] <= 'h', list(dict.keys()))))

    
    return \
    w_pieces_number <= 16 and b_pieces_number <= 16 and \
    w_pieces_number_king <= 1 and b_pieces_number_king <= 1 and \
    w_pieces_number_queen <= 1 and b_pieces_number_queen <= 1 and \
    w_pieces_number_bishop <= 2 and b_pieces_number_bishop <= 2 and \
    w_pieces_number_knight <= 2 and b_pieces_number_knight <= 2 and \
    w_pieces_number_rook <= 2 and b_pieces_number_rook <= 2 and \
    w_pieces_number_pawn <= 8 and b_pieces_number_pawn <= 8 and \
    pieces_valid_places_number == w_pieces_number + b_pieces_number and \
    pieces_valid_places_letter == w_pieces_number + b_pieces_number

print(is_valid_chess_board(board))