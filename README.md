# Deep-Reinforcement-Learning
**Summary**: This repository is to demonstrate a custom environment for Deep Reinforcement Learning (DQN) using GPU acceleration in pytorch.

**Objective**: To showcase a custom environment written in pure Python that can be used for Deep Reinforcement Learning 

**Details**: This notebook has a simple jump game simulated and learned by the computer using machine learning through Deep Q Learning. The environment settings are:

![](https://github.com/SaratChandraV/Deep-Reinforcement-Learning/blob/main/game_sample.gif)

1. Reward = 1 if correct action else 0
2. Termination = if any incorrect action
3. Max length of Episode = 200 steps

**Note: Please change the code to CUDA wherever MPS (MacBook GPU - Metal) has been used.**

The library used: **Pytorch**.

**The Training and Testing Results are:**

**1. Training:**

![](https://github.com/SaratChandraV/Deep-Reinforcement-Learning/blob/main/training_output.png)

**2. Testing: (Here 1000 steps per episode are used)**

![](https://github.com/SaratChandraV/Deep-Reinforcement-Learning/blob/main/testing_ouput.png)
