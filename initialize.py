from QDQN import QuantumDQNAgent
from grid import Grid
import numpy as np
from pathlib import Path

# Hyperparameters
n_qubits = 16  # Number of qubits (state space size)
n_actions = 4  # 'w', 'a', 's', 'd'
n_layers = 3
batch_size = 32
episodes = 100
episode_num = 4  # Last episode number from checkpoints/

# Ensure the directory exists
Path("./checkpoints").mkdir(parents=True, exist_ok=True)

# Initialize agent and environment
agent = QuantumDQNAgent(
    n_qubits=n_qubits, n_actions=n_actions, n_layers=n_layers, batch_size=batch_size
)
env = Grid(size=4)

# Load latest weights
print("Random weights", agent.model.get_weights())
agent.load(model_path=f"./checkpoints/qdqn_model_{episode_num}.keras")
print("Loaded weights", agent.model.get_weights())

# Training loop
for episode in range(episode_num + 1, episodes):
    # state = np.random.random(n_qubits)  # Flatten and normalize state
    state = env.reset()
    total_reward = 0
    done = False

    while not done:
        action = agent.choose_action(state)
        next_state, reward, done = env.step(action)
        agent.remember(state, action, reward, next_state, done)

        state = next_state
        total_reward += reward
        env.render()

        agent.replay()

    print(f"Episode {episode + 1}, Total Reward: {total_reward}")

    # Save every episode result
    agent.save(f"./checkpoints/qdqn_model_{episode + 1}.keras")
