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
# episodes = 10  # Just for checking whether the code runs without errors

# Ensure the directory exists
Path("./checkpoints").mkdir(parents=True, exist_ok=True)

# Initialize agent and environment
agent = QuantumDQNAgent(
    n_qubits=n_qubits, n_actions=n_actions, n_layers=n_layers, batch_size=32
)
env = Grid(size=4)

# Training loop
for episode in range(episodes):
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

    if (episode + 1) % 10 == 0:
        agent.save(f"./checkpoints/qdqn_model_{episode + 1}.keras")
