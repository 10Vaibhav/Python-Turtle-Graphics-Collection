# U.S. 50 States Quiz

An interactive educational game to test and improve your knowledge of U.S. state locations.

![U.S. Map](blank_states_img.gif)

## Description

This Python-based quiz game challenges players to name all 50 U.S. states by clicking on their locations on a map. It's an engaging way to learn U.S. geography and test your knowledge of state locations.

## Features

- Interactive U.S. map using the Turtle graphics library
- Input-based state guessing
- Progress tracking (number of correctly guessed states)
- Ability to exit the game and save progress
- Generation of a CSV file with missed states for further learning

## Files

- `main.py`: The main game script
- `writer.py`: Contains the Writer class for placing text on the map
- `50_states.csv`: Data file with state names and coordinates
- `blank_states_img.gif`: The blank U.S. map image
- `states_to_learn.csv`: Generated file with missed states (created upon exit)

## Requirements

- Python 3.x
- Pandas library
- Turtle graphics library

## Game Rules

1. Enter the name of a U.S. state when prompted
2. Correct guesses will be placed on the map
3. The game continues until all 50 states are guessed or the player exits
4. Exiting the game will generate a CSV file with missed states

## Learning Tool

After exiting the game, check the `states_to_learn.csv` file to see which states you missed. Use this as a study guide to improve your U.S. geography knowledge!

## Contributing

Contributions, issues, and feature requests are welcome

## Acknowledgements
- Inspired by educational geography quizzes