# 2Q48

This project explores an unorthodox approach to solving the popular tile-merging game 2048 by leveraging the power of quantum computing within a reinforcement learning (RL) environment.

The project examines three distinct methodologies- traditional heuristic-based techniques, classical reinforcement learning, and quantum reinforcement learning (QRL); to observe the effects and unique behaviors introduced by quantum-inspired strategies compared to classical methods. 
## Prerequisites

Before running the code, ensure that you have the following prerequisites installed:

- Python 3.10 (or later)
- pip (Python's package installer)

Ensure you have Python 3.10 installed. You can download it from the official website: [Python 3.10](https://www.python.org/downloads/release/python-3100/)

## Running the Project
1. Clone the repository
```
git clone https://github.com/DineshDhanji/2Q48.git
cd 2Q48
```
2. Create a virtual environment using Python 3.10, then activate it:
```
virtualenv -p python3.10 .venv
source .venv/bin/activate  # For Linux/MacOS
.\.venv\Scripts\activate   # For Windows
```
3. You can deactivate the environment by following command:
```
deactivate
```

## File Structure
- `checkpoints/`: Contains the latest model weights for the quantum-based Q-learning agent.
- `QDQN.py`: Implements the quantum-based neural network used to train the agent.
- `Heuristic.py:` A simple heuristic-based approach for solving the 2048 game.
- `initializer.py:` Responsible for loading the latest weights and continuing training from the last checkpoint. Update the `last_episode` variable to resume training.
- `Tester.py:` Test the agent by playing the game using the most recent weights. Modify last_episode to load the latest trained model. 
- `2048.py:` The base implementation of the 2048 game. Play the game manually using this file.


## Training the Model
To train the Q-learning agent with quantum neural networks, run the following script:
```
python initializer.py
```
But make sure that the `episode_num` is set to latest iteration. This will load the latest episode's model weights, continue training, and save new checkpoints as training progresses. 

## Testing the Model
To test the model with the most recent weights, update the `episode_num` in tester.py and run:
```
python Tester.py
```
This will load the latest model and use it to play the 2048 game, demonstrating how well the agent performs after training.