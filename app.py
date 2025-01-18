from flask import Flask, jsonify
import runstock  # Import your runstock script
import lichess_call  # Import the script that fetches FEN from Lichess

app = Flask(__name__)

@app.route('/get-best-move', methods=['GET'])
def get_best_move():
    try:
        # Call the function from your runstock code
        best_move_data = runstock.get_best_move_and_scores()

        # Format the response to be JSON-friendly
        response = {
            "best_move": str(best_move_data["best_move"]),
            "active_color": best_move_data["active_color"],
            "winning_percentage_active": best_move_data["winning_percentage_active"],
            "winning_percentage_other": best_move_data["winning_percentage_other"]
        }
        return jsonify(response), 200
    except Exception as e:
        # Handle errors gracefully
        return jsonify({"error": str(e)}), 500

@app.route('/get-fen', methods=['GET'])
def get_fen():
    try:
        # Call the function from your lichess_call script
        fen = lichess_call.get_current_fen()

        if fen:
            return jsonify({"fen": fen}), 200
        else:
            return jsonify({"message": "No ongoing games found or unable to fetch FEN"}), 404
    except Exception as e:
        # Handle errors gracefully
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
