# xo
Tic-Tac-Toe: Desktop GUI ApplicationA fully functional, interactive board game built with Python and the Tkinter framework.

Tech StackLanguage: 
-Python
-Library: Tkinter (Python’s standard GUI toolkit)
-Logic: Matrix-based win detection and state management

Key Features
- Interactive Graphical User Interface (GUI)
- -Developed a clean, responsive game board using a grid-based layout.
- Visual Feedback: Implemented color-coded state changes—winning combinations highlight in green, while a draw highlights the board in yellow.
- Intelligent Game LogicBuilt a custom engine to handle the rules of Tic-Tac-Toe:Turn
- Management: Features a random starting player ("X" or "O") and toggles turns automatically after each valid move.
- Win/Tie Detection: A comprehensive algorithm scans rows, columns, and diagonals to identify a winner instantly.Draw Validation: The script checks for "Tie" states by verifying if the board is full without a winning pattern.
- State Reset CapabilityIncluded a "Restart" functionality that resets the game state, clears the board, and picks a new starting player without needing to relaunch the application.

 
Engineering Highlights
- Closures and Scope Management
Used the nonlocal keyword to manage the player state within nested functions.
- Event-Driven ProgrammingImplemented lambda functions to bind grid coordinates $(r, c)$ to button click events. This allows a single function (next_turn) to handle interactions for all nine buttons dynamically.
//Python
buttons[r][c] = tk.Button(
    frame,
    command=lambda r=r, c=c: next_turn(r, c)
)



Future Improvements:
- AI Opponent
- Score Tracker: Add a persistent scoreboard to track wins between multiple rounds.
- Custom Themes: Allow users to choose different colors or symbols (e.g., Emoji) instead of X and O.
