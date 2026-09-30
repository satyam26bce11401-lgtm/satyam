# Number Guessing Game

A menu-driven, command-line number guessing game written in Python 3. Pick a difficulty, guess the secret number within a limited number of attempts, and get direction and distance hints after every wrong guess. The game keeps a score and session statistics.

**Author:** Satyam Debnath | **Reg. No.:** 26BCE11401 | **University:** VIT Bhopal University
**Project:** VITyarthi - Build Your Own Project

---

## Overview

The computer picks a random secret number. You guess it before your attempts run out. After each wrong guess you are told whether the guess was **too low** or **too high**, plus a **hint** showing how close you are. Winning earlier gives a higher score, and statistics are shown after every game.

The project is built as a set of small, single-purpose functions organised into seven logical modules (display, input, game logic, scoring, help, statistics, controller). It uses only the Python standard library and includes an automated test suite.

## Features

- **Main menu:** Start Game, How to Play, Exit
- **Three difficulty levels:**

  | Level  | Range   | Attempts |
  |--------|---------|----------|
  | Easy   | 1 - 50  | 10       |
  | Medium | 1 - 100 | 7        |
  | Hard   | 1 - 200 | 5        |

- **Direction feedback:** "Too Low" / "Too High"
- **Distance hints:**

  | Difference from secret number | Hint             |
  |-------------------------------|------------------|
  | 1 - 5                         | VERY close       |
  | 6 - 15                        | Close            |
  | 16 - 30                       | Getting warmer   |
  | 31 or more                    | Quite far away   |

- **Scoring:** `score = 100 + (remaining attempts x 20)`
- **Session statistics:** games played, won, lost, total score, win rate
- **Input validation:** letters, decimals, blanks and out-of-range numbers are rejected without crashing, and an invalid entry does **not** use up an attempt
- **Play again** option after every game

## Technologies Used

- Python 3 (developed and tested on 3.12; 3.6+ required for f-strings)
- Standard library only: `random`, `time`
- Testing: `unittest`, `unittest.mock`
- Version control: Git / GitHub

## Project Structure

```
number-guessing-game/
|-- number_guess.py          # the game
|-- test_number_guess.py     # 37 automated tests
|-- README.md
|-- statement.md             # problem statement, scope, target users, features
+-- docs/
    +-- Number_Guessing_Game_Project_Report.pdf
```

## Installation and Running

1. Make sure Python 3 is installed:

   ```bash
   python --version
   ```

2. Get the project:

   ```bash
   git clone https://github.com/<your-username>/number-guessing-game.git
   cd number-guessing-game
   ```

3. Run the game:

   ```bash
   python number_guess.py
   ```

   On Linux/macOS you may need `python3` instead of `python`.

No extra packages need to be installed.

## How to Play

1. Type `1` and press Enter to start, then choose a difficulty (`1`, `2` or `3`).
2. Type a whole number in the range shown and press Enter.
3. Use the "Too Low / Too High" message and the hint to narrow down the number.
4. Guess it before you run out of attempts. The fewer attempts you use, the higher your score.
5. After the game, type `y` to play again or `n` to quit.

Tip: guessing the middle of the remaining range each time (binary search) is the best strategy.

## Testing

Run the automated test suite from the project folder:

```bash
python -m unittest -v test_number_guess
```

Expected result:

```
Ran 37 tests in 0.005s

OK
```

The tests cover guess comparison, hint boundaries, scoring, input validation (menu, difficulty, guess, replay), full game rounds (win, last-attempt win, loss), statistics, and the main program flow. Input and randomness are mocked, so the tests are fast and repeatable.

## Screenshots

Sample session (Medium difficulty, secret number was 42):

```
MAIN MENU
-------------------------------------------------------
1. Start Game
2. How to Play
3. Exit
-------------------------------------------------------
Enter your choice: 1

Choose a difficulty level:
1. Easy   - Numbers 1 to 50, 10 attempts
2. Medium - Numbers 1 to 100, 7 attempts
3. Hard   - Numbers 1 to 200, 5 attempts

Select difficulty: 2

I have selected a number.
The number is between 1 and 100.
You have 7 attempts.

Attempt 1/7 - Enter your guess (1-100): hello
Please enter a valid whole number.
Attempt 1/7 - Enter your guess (1-100): 101
Please enter a number between 1 and 100.
Attempt 1/7 - Enter your guess (1-100): 82
Too High! Try a lower number.
Hint: You are quite far away.
You have 6 attempt(s) remaining.

Attempt 2/7 - Enter your guess (1-100): 50
Too High! Try a lower number.
Hint: You are close.
You have 5 attempt(s) remaining.

Attempt 3/7 - Enter your guess (1-100): 42

Congratulations!
You guessed the correct number!
You guessed it in 3 attempt(s).
-------------------------------------------------------
Your score: 180
-------------------------------------------------------
-------------------------------------------------------
GAME STATISTICS
-------------------------------------------------------
Games played: 1
Games won: 1
Games lost: 0
Total score: 180
Win rate: 100.0%
-------------------------------------------------------
```

## Documentation

The full project report (requirements, architecture, UML and workflow diagrams, implementation details, testing and results) is in `docs/Number_Guessing_Game_Project_Report.pdf`.

## Known Limitations and Future Work

- Statistics are kept only for the current run (no high-score file).
- Pressing Ctrl+C shows a Python traceback instead of a graceful exit.
- The Hard level is very difficult: even a perfect binary-search player can win at most about 15.5% of games.
- Planned: split into a multi-file package, persistent high scores, custom ranges, and a GUI.

## License

Created for academic purposes as part of the VITyarthi Build Your Own Project evaluation.
