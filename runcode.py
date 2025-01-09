import chess
import chess.engine

engine_path = r"C:\Users\space\Desktop\stockfish\stockfish.exe"
board = chess.Board()

with chess.engine.SimpleEngine.popen_uci(engine_path) as engine:
    info = engine.analyse(board, chess.engine.Limit(depth=10))
    
    print("Depth:", info["depth"])
    print("Score:", info["score"])
    if "string" in info:
        print("Engine String:", info["string"])
    
    print("Principal Variation (line of moves):")
    temp_board = board.copy()
    for move in info["pv"]:
        print(" ", temp_board.san(move))
        temp_board.push(move)
