# Pac-Man Uninformed Search Project

## Project Overview
This project implements uninformed search algorithms (Breadth-First Search and Depth-First Search) for a Multi-Agent Pac-Man environment. The goal is to navigate Pac-Man from the starting point to the goal, exploring the maze efficiently using the specified search strategies.

The project is based on the Multi-Agent Pac-Man framework provided by Stanford University.

## Implemented Algorithms
1. **Breadth-First Search (BFS):**
   - Explores all the neighbor nodes at the present depth before moving on to nodes at the next depth level.
   - Implemented using a queue to manage the frontier.

2. **Depth-First Search (DFS):**
   - Explores as far as possible along each branch before backtracking.
   - Implemented using a stack to manage the frontier.

Both algorithms ensure Pac-Man navigates through the maze while adhering to legal movements (North, South, East, West).

## File Structure
- `pacman.py`: Main script to run the Pac-Man simulation.
- `searchAgents.py`: Contains the implementation of BFS and DFS algorithms.
- `game.py`, `layout.py`, `graphicsDisplay.py`, and other support files: Framework files for the Pac-Man environment.
- `result.txt`: Outputs the sequence of `(x, y)` coordinates visited by Pac-Man in the search process.

## How to Run the Code
1. **Run Pac-Man with BFSAgent:**
   ```bash
   python pacman.py -p BFSAgent

2. **Run Pac-Man with DFSAgent:**
   ```bash
   python pacman.py -p DFSAgent

3. **Run in Non-Graphic Mode:**
   ```bash
   python pacman.py -p BFSAgent -q
   python pacman.py -p DFSAgent -q

### Note for macOS Users
If the above commands do not work, try using:
    ```bash
   python3 pacman.py -p BFSAgent
   python3 pacman.py -p DFSAgent

## Input and Output
### Input:
- Pac-Man starts at the default position (0, 0)
- The maze layout and legal moves are determined by the Pac-Man framework.

### Output:
- The sequence of (x, y) coordinates visited by Pac-Man is saved in the result.txt file.

## Legal Moves
- Pac-Man can move in the four cardinal directions: North, South, East, and West.
- Movements are restricted based on walls and the maze layout.
- The order of exploration for neighboring nodes is:
    1. East
    2. West
    3. South
    4. North

## Requirements
- Python 3.6 or higher.
- Ensure all framework files are in the same directory as `searchAgents.py`.

## References
This project is based on the Multi-Agent Pac-Man project from Stanford University: [Pac-Man Project](https://stanford.edu/~cpiech/cs221/homework/prog/pacman/pacman.html).

This project was completed as part of the **CSCI-3613 Artificial Intelligence** course at ADA University, which focuses on various machine learning techniques and their applications.