import requests

# Your Lichess API token
api_token = "lip_Y0c8hdqpMPl6OmqmF0yI"  # Replace with your actual token

def get_lichess_fen(game_id):
    url = f"https://lichess.org/api/game/{game_id}"
    headers = {
        "Authorization": f"Bearer {api_token}"
    }
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        game_data = response.json()
        return game_data.get('fen', 'No FEN found.')
    else:
        return f"Error: {response.status_code}"

# Example usage
game_id = "oK8jdwTE4JXMa"  # Replace with the game ID of the game you want to check
fen = get_lichess_fen(game_id)
print(f"FEN for game {game_id}: {fen}")