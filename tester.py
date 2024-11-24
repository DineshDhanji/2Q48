import numpy as np
import tensorflow as tf
from grid import Grid
from QDQN import QuantumDQNAgent
import time

# Hyperparameters
n_qubits = 16  # Number of qubits (state space size)
n_actions = 4  # 'w', 'a', 's', 'd'
n_layers = 3
batch_size = 32

# Initialize the environment and agent
env = Grid(size=4)
agent = QuantumDQNAgent(
    n_qubits=n_qubits, n_actions=n_actions, n_layers=n_layers, batch_size=batch_size
)

# Load the trained model
model_path = "./checkpoints/qdqn_model_4.keras"  # Provide the path to your saved model
agent.load(model_path)

# Test the agent by playing the game
state = env.reset()  # Reset the environment to get the initial state
done = False
total_reward = 0

# Exploration parameters
stuck = False  # Flag to check if the agent is stuck in a loop
move = -1  # No previous move initially
count = 0  # Counter for the number of times the same action is repeated

# Play the game by interacting with the environment
while not done:
    state_flat = np.array(state).flatten()
    q_values = agent.model.predict(np.expand_dims(state_flat, axis=0))[0]

    # Action selection (exploitation by default)
    if stuck:
        # If stuck, take a random action for exploration
        action = np.random.choice(n_actions)
        print("Agent is stuck! Taking random action.")
        stuck = False  # Reset stuck flag
    else:
        # Otherwise, take the action with the highest Q-value (exploitation)
        action = np.argmax(q_values)

    # Log Q-values and action taken
    print(f"Q-values: {q_values}")
    print(f"Action taken: {action}")

    # Take the action in the environment
    next_state, reward, done = env.step(agent.action_map[action])
    state = next_state  # Update state with the next state
    total_reward += reward  # Update total reward

    # Optionally render the environment to see the progress
    env.render()

    # Detect if the agent is stuck in a loop (i.e., repeating the same action multiple times)
    if action == move:
        count += 1
    else:
        move = action
        count = 0
    if count >= 5:  # If the agent repeats the same action 5 times, it's stuck
        stuck = True
        count = 0  # Reset counter for stuck detection

    # Pause for better visual inspection (optional)
    time.sleep(0.1)  # Optional: adds a small delay for rendering to be visible

# Print the final result
print(f"Game Over! Total Reward: {total_reward}")
