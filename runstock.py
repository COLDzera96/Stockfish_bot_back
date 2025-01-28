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
    stockfish_path = r"stockfish\stockfish-ubuntu-x86-64-avx2"  # Replace with your Stockfish binary path
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

    result_map = {
        "best_move": result.move,
        "active_color": "black" if active_color == 'b' else "white",
        "winning_percentage_active": winning_percentage_active,
        "winning_percentage_other": winning_percentage_other
    }
    return result_map

if __name__ == "__main__":
    best_move_data = get_best_move_and_scores()
    formatted_output = f"""Best move for {best_move_data['active_color']}: {best_move_data['best_move']},
Win for {best_move_data['active_color']}: {best_move_data['winning_percentage_active']}%,
Win for {'white' if best_move_data['active_color'] == 'black' else 'black'}: {best_move_data['winning_percentage_other']}%"""
    print(formatted_output)
