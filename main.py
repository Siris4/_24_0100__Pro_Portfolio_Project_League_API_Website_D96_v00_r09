from flask import Flask, render_template, jsonify
from riot_api import get_live_game_by_puuid  # Import the function from riot_api.py

app = Flask(__name__)


# Define the route for the home page
@app.route('/')
def index():
    return render_template('index.html')


# Define the route to get live game data
@app.route('/get-live-game', methods=['GET'])
def get_live_game():
    # Call the function to get live game data
    live_game_data = get_live_game_by_puuid(region='na1')

    # If live_game_data exists, return it as JSON, else return an error message
    if live_game_data:
        return jsonify(live_game_data)
    else:
        return jsonify({"error": "This summoner is not currently in a live game."})


# Run the Flask app
if __name__ == '__main__':
    app.run(debug=True)
