### 1. **What is Deep Q-Learning?**
Deep Q-Learning is a reinforcement learning algorithm where an agent learns to maximize rewards by interacting with an environment. It uses a **neural network (Q-network)** to approximate the Q-values for each state-action pair.

#### Key Components:
1. **State (`S`)**: Representation of the environment at a specific time (e.g., the 2048 grid).
2. **Action (`A`)**: Possible moves the agent can take (e.g., `UP`, `DOWN`, `LEFT`, `RIGHT`).
3. **Reward (`R`)**: Feedback from the environment after taking an action.
4. **Q-value (`Q(S, A)`)**: Expected future reward for taking action `A` in state `S`.
5. **Target Q-value (`Q_target`)**: Helps stabilize training:
   \[
   Q_{\text{target}} = R + \gamma \max Q(S', A')
   \]
   Here, `S'` is the next state, and `\gamma` is the discount factor.

---

### 2. **Quantum Deep Q-Learning**
Instead of a classical neural network, we use a **quantum neural network (QNN)**. A QNN is a parameterized quantum circuit (PQC) that can represent and learn complex patterns.

#### Benefits of Quantum:
- **Parallelism**: Quantum superposition allows simultaneous exploration of multiple states.
- **Expressivity**: QNNs can potentially encode certain problems more efficiently than classical networks.

---

### 3. **How It Works**

#### Step 1: **The Environment**
The environment simulates the game (2048 in our case):
1. Receives the agent's action.
2. Updates the game state.
3. Provides a reward and tells if the game is over.

#### Step 2: **The Quantum Neural Network (QNN)**
The QNN:
- Accepts the current state of the environment (flattened grid).
- Outputs Q-values for all possible actions.

#### Step 3: **Agent's Decision**
The agent:
- Uses an **epsilon-greedy strategy**:
  - **Exploration**: Chooses a random action with probability `epsilon`.
  - **Exploitation**: Chooses the action with the highest Q-value otherwise.

#### Step 4: **Experience Replay**
The agent:
1. Stores experiences `(state, action, reward, next_state, done)` in a **replay memory**.
2. Trains the QNN by sampling random batches from this memory.

#### Step 5: **Training**
The agent:
1. Calculates the **target Q-value** for each experience:
   \[
   Q_{\text{target}} = R + \gamma \max Q(S', A')
   \]
2. Computes the **loss**:
   \[
   \text{Loss} = \left(Q_{\text{target}} - Q_{\text{predicted}}\right)^2
   \]
3. Updates the QNN weights using gradients of the loss.

---

### 4. **Architecture Overview**

#### Quantum Circuit:
- **Input Layer**: Encodes the game state (e.g., Angle Embedding).
- **Hidden Layers**: Parameterized gates (e.g., RX, RY, RZ) and entangling layers.
- **Output Layer**: Returns Q-values (via expectation values).

#### Training Loop:
1. Observe the initial state.
2. Choose an action (epsilon-greedy).
3. Perform the action and observe the reward and next state.
4. Store the experience in replay memory.
5. Train the QNN by minimizing the loss for a batch of experiences.
6. Update the target network periodically.