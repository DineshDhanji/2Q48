import logging
from QDQN import QuantumDQNAgent
from grid import Grid
import numpy as np
from pathlib import Path
import tensorflow as tf

# Hyperparameters
n_qubits = 16  # Number of qubits (state space size)
n_actions = 4  # 'w', 'a', 's', 'd'
n_layers = 3
batch_size = 64
episodes = 100
episode_num = 6  # Last episode number from checkpoints/
max_steps_per_episode = 200

# Enable GPUs
gpus = tf.config.list_physical_devices("GPU")
tf.config.set_visible_devices(gpus[0], "GPU")
tf.config.experimental.set_memory_growth(gpus[0], True)
# tf.debugging.set_log_device_placement(True)

# Ensure the directory exists
Path("./checkpoints").mkdir(parents=True, exist_ok=True)

# Set up logging
log_dir = Path("./logs")
log_dir.mkdir(parents=True, exist_ok=True)
log_file = log_dir / "training.log"

logging.basicConfig(
    filename=log_file,
    level=logging.INFO,  
    format="%(asctime)s - %(levelname)s - %(message)s",
)

# Initialize agent and environment
agent = QuantumDQNAgent(
    n_qubits=n_qubits, n_actions=n_actions, n_layers=n_layers, batch_size=batch_size
)
env = Grid(size=4)

# Load latest weights
print("Random weights", agent.model.get_weights())
agent.load(model_path=f"./checkpoints/qdqn_weights_{episode_num}.keras")
print("Loaded weights", agent.model.get_weights())

# Training loop
for episode in range(episode_num + 1, episodes):
    # state = np.random.random(n_qubits)  # Flatten and normalize state
    state = env.reset()
    total_reward = 0
    done = False
    steps = 0

    while not done and steps < max_steps_per_episode:
        action = agent.choose_action(state)
        next_state, reward, done = env.step(action)
        agent.remember(state, action, reward, next_state, done)

        state = next_state
        total_reward += reward
        steps += 1

        if steps % 5 == 0:  # Replay less frequently
            agent.replay()
        env.render()

    print(f"Episode {episode + 1}, Total Reward: {total_reward}")
    
    # Log episode results using logging module
    logging.info(f"Episode {episode + 1}, Total Reward: {total_reward}")

    # Save every episode result
    agent.save(f"./checkpoints/qdqn_weights_{episode + 1}.keras")
