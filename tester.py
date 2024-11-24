import numpy as np
import tensorflow as tf
from grid import Grid
from QDQN import QuantumDQNAgent

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

# Play the game by interacting with the environment
while not done:
    state_flat = np.array(state).flatten()
    q_values = agent.model.predict(np.expand_dims(state_flat, axis=0))[0]

    # # Introduce randomness for exploration
    # epsilon = 0.1  # Set a small exploration rate for testing
    # if np.random.rand() <= epsilon:
    #     action = np.random.choice(n_actions)  # Exploration
    # else:
    #     action = np.argmax(q_values)  # Exploitation
    action = np.argmax(q_values)  # Exploitation

    print("q_values: ", q_values)
    print("action: ", action)
    next_state, reward, done = env.step(
        agent.action_map[action]
    )  # Take the action in the environment
    state = next_state  # Update state with the next state
    total_reward += reward  # Update total reward

    env.render()  # Optionally render the environment to see the prog

print(f"Game Over! Total Reward: {total_reward}")
