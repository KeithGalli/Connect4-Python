# connect4-python

A simple Connect Four game implemented in Python, following Test-Driven Development (TDD) principles.

## Description

This project provides a basic Connect Four game with core functionalities, including board representation and win detection. The focus is on demonstrating TDD workflow and clean code implementation.

## Key Features

- **Game Board:** A 2D representation of the Connect Four board.
- **Winning Move Detection:** Functionality to check for horizontal, vertical, and diagonal wins.

## Technologies Used

- Python
- NumPy (for efficient array manipulation)
- Pygame (for potential future graphical interface enhancements)

## Installation

1.  **Clone the Repository:**
    ```bash
    git clone [your_repository_url]
    cd connect4-python
    ```
2.  **Ensure Python is Installed:** Python 3.x is required.
3.  **Install Dependencies (if any):**
    ```bash
    # Install them with pip
    pip install numpy pygame
    ```

## Basic Usage

1.  **Run the Tests:**
    ```bash
    python -m unittest connect_test.py
    ```
    This will execute the test suite to verify the core functionality.
2.  **Run the Game **
    ```bash
    python connect4.py
    ```

## Features Overview

-   **Test-Driven Development:** The project emphasizes TDD, ensuring robust and reliable code.
-   **Horizontal Win Detection:** Implemented and tested.
-   **Extensible:** Designed to accommodate future features like vertical and diagonal win detection, and AI integration.

## Configuration Options

-   Currently, the game parameters (board size, etc.) are hardcoded. Future iterations can introduce configuration files or command-line arguments.

## Troubleshooting

-   **Test Failures:** If tests fail, review the `connect_test.py` file and the corresponding implementation in `connect4.py`.
-   **Import Errors:** Ensure that all required libraries (NumPy, Pygame) are correctly installed.

## Contributing Guidelines

1.  **Fork the Repository:** Create your own copy of the project.
2.  **Create a Branch:** `git checkout -b feature/your-feature`
3.  **Make Changes:** Implement your feature or fix.
4.  **Commit Changes:** `git commit -m "Add your feature"`
5.  **Push Changes:** `git push origin feature/your-feature`
6.  **Create a Pull Request:** Submit your changes for review.

## License Information

-    MIT License

## Code Structure Overview

-   `connect4.py`: Contains the core game logic.
-   `connect4_with_ai.py`: Includes AI implementation for Connect Four.
-   `connect_test.py`: Contains unit tests for the game functionality.

Video walkthrough on programming this game: https://youtu.be/UYgyRArKDEs

Video walkthrough on programming the AI: https://youtu.be/MMLtza3CZFM
