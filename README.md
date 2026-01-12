# Number Guessing Game with Flask

A simple Flask web app where users guess a random number between 0 and 9.

## Features
- Generates a random number (0–9) when the app starts
- Home page displays game instructions and an animated GIF
- User guesses by visiting `/number` (e.g., `/5`)
- Feedback: "Too Low", "Too High", or "Correct!" with colored text and GIFs

## How to Run
1. Save the code as `app.py`
2. Install Flask:  
   ```bash
   pip install flask
   ```
3. Run the app:  
   ```bash
   python app.py
   ```
4. Open [http://localhost:5000](http://localhost:5000)

## Requirements
- Python 3.x
- Flask

The game uses direct URL input for guesses (no form). The random number is reset each time the server starts.

