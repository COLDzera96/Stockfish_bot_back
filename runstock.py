import chess
import chess.engine
import lichess_call

def get_best_move_and_scores():
    # Initialize the board with the given FEN position
    position = lichess_call.get_current_fen()
    board = chess.Board(position)

    # Determine the side to move (White or Black)
    parts = position.split()
    active_color = parts[1]  # 'w' means White to move, 'b' means Black

    # Path to the Stockfish engine (adjust the path based on your system)
    stockfish_path = r"C:\Users\space\Desktop\stockfish\stockfish.exe"  # Replace with your Stockfish binary path
    engine = chess.engine.SimpleEngine.popen_uci(stockfish_path)

    # Find the best move for the active color
    result = engine.play(board, chess.engine.Limit(time=1.0))

    # Analyze the position
    info = engine.analyse(board, chess.engine.Limit(depth=10))
    score = info["score"].relative.score(mate_score=10000)  # Use a large number for mate score

    # Calculate winning percentage for the active color
    if score is not None:
        winning_percentage_active = 50 + (score / 100.0)
    else:
        winning_percentage_active = 50  # Neutral position

    # Calculate winning percentage for the other side
    winning_percentage_other = 100 - winning_percentage_active

    # Close the engine after use
    engine.quit()

    return (f"Best move for {'black' if active_color == 'b' else 'white'}: {result.move}, "
            f"Win for {'black' if active_color == 'b' else 'white'}: {winning_percentage_active}%, "
            f"Win for {'white' if active_color == 'b' else 'black'}: {winning_percentage_other}%")

if __name__ == "__main__":
    best_move_text = get_best_move_and_scores()
    print(best_move_text)
