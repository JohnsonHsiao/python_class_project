
# Project Overview

This project contains two main Python scripts, `final.py` and `midterm.py`, each serving different purposes.

## 1. `final.py` - Othello Game using Telegram Bot

The `final.py` script implements a simple version of the "Othello" (or Reversi) game, allowing players to interact with a Telegram bot to play the game. This script uses the Telegram Bot API and `python-telegram-bot` library to enable gameplay via chat interaction.

### Key Features:
- Initializes an 8x8 Othello game board with starting pieces in the center.
- Allows players to make moves by clicking buttons on the Telegram chat.
- The bot performs random valid moves as an opponent to the player.
- Checks for valid moves, counts pieces, and determines when the game ends.
- Displays the board and updates it dynamically as the game progresses.

### How to Run
1. Install the required libraries:
   ```bash
   pip install python-telegram-bot
   ```
2. Replace the `token` in the `main()` function with your own Telegram bot token.
3. Run the script:
   ```bash
   python final.py
   ```
4. Start a chat with your Telegram bot and use the command `/start` to begin the game.

### Commands
- `/start` - Starts interaction with the bot.
- `/game_start` - Begins a new Othello game.

---

## 2. `midterm.py` - Web Automation Using PyAutoGUI

The `midterm.py` script automates interactions with a web-based game using the `pyautogui` library. The script opens a Chrome browser, navigates to a specific game URL, and performs actions by locating images on the screen.

### Key Features:
- Opens Chrome browser and navigates to the target URL.
- Uses image recognition to find and click specific images on the screen to interact with the game.
- Automates gameplay by finding patterns, clicking elements, and reacting based on the game’s status.

### How to Run
1. Install the required library:
   ```bash
   pip install pyautogui
   ```
2. Ensure the `photo` directory contains all the required images for the game automation (excluding `.DS_Store` and `shuffle.png`).
3. Run the script:
   ```bash
   python midterm.py
   ```

### Important Note
- This script requires `pyautogui` to have appropriate permissions to control the mouse and keyboard. Make sure to grant necessary permissions on your system.

---

## Requirements
- Python 3.x
- `python-telegram-bot` library for `final.py`
- `pyautogui` library for `midterm.py`

## Disclaimer
The use of this project is intended for educational purposes only. Please ensure you comply with relevant usage policies when running automation scripts or interacting with external services.
