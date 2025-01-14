import requests

# Your Lichess API token
api_token = "lip_CrLmOJARpkc2D94durcz"

# API URL for the user's ongoing games
url = "https://lichess.org/api/account/playing"

# Headers with authorization
headers = {
    "Authorization": f"Bearer {api_token}"
}

# Fetch the user's ongoing games
response = requests.get(url, headers=headers)

if response.status_code == 200:
    data = response.json()
    if "nowPlaying" in data and data["nowPlaying"]:
        # Get the FEN of the first ongoing game
        fen = data["nowPlaying"][0]["fen"]
        print("Current FEN:", fen)
    else:
        print("No ongoing games found.")
else:
    print("Error:", response.status_code, response.text)


# function returning fen of current game
def get_current_fen():
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        data = response.json()
        if "nowPlaying" in data and data["nowPlaying"]:
            return data["nowPlaying"][0]["fen"]
    return None

# fen of any game in the world on lichess
