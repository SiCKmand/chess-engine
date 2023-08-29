import chess
from engine import ChessAI

def user_move(color, board, list):
    print(board)
    legalMoves = board.legal_moves
    while True:
        move = chess.Move.from_uci(input("Enter move:"))
        if move in legalMoves:
            board.push(move)
            ChessAI(color).add_move(list, str(move))
            return str(move)
        else:
            print("Invalid move")

def ai_move(color, board):
    print(board)
    move = chess.Move.from_uci(ChessAI(color).make_move(board))
    board.push(move)
    return str(move)

def main(color, board, fname):
    user_moves=[]
    while True:
        file = open(f"data/{fname}", "a")
        if color == "b":
            umove=user_move(color, board, user_moves)
            file.write(umove+"\n")
            amove=ai_move(color, board)
            file.write(amove + "\n")
        elif color == "w":
            amove=ai_move(color, board)
            file.write(amove+"\n")
            umove=user_move(color, board, user_moves)
            file.write(umove + "\n")

        if board.is_checkmate():
            print(board.outcome())
        elif board.is_stalemate() or board.is_insufficient_material():
            print("Match draw")
        file.close()

board = chess.Board()
user_color = input("Enter color(w or b):")
filename = input("Enter filename to save the game:")
while True:
    if user_color == "w":
        ai_color = "b"
        break
    elif user_color == "b":
        ai_color = "w"
        break
    else:
        print("Invalid Move")
main(ai_color, board, filename)