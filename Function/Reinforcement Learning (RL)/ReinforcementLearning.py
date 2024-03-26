import torch
import torch.nn as nn
import torch.optim as optim
import numpy as np

class ReinforcementLearning:
    def __init__(self, state_dim, action_dim, learning_rate=0.001):
        self.state_dim = state_dim
        self.action_dim = action_dim
        self.learning_rate = learning_rate
        
        self.policy_net = self.build_policy_net()
        self.optimizer = optim.Adam(self.policy_net.parameters(), lr=self.learning_rate)
        
    def build_policy_net(self):
        policy_net = nn.Sequential(
            nn.Linear(self.state_dim, 128),
            nn.ReLU(),
            nn.Linear(128, 64),
            nn.ReLU(),
            nn.Linear(64, self.action_dim),
            nn.Softmax(dim=-1)
        )
        return policy_net
    
    def select_action(self, state):
        state = torch.from_numpy(state).float().unsqueeze(0)
        probs = self.policy_net(state)
        action_probs = torch.distributions.Categorical(probs)
        action = action_probs.sample()
        return action.item()
    
    def train(self, states, actions, rewards):
        states = torch.from_numpy(states).float()
        actions = torch.from_numpy(actions).long()
        rewards = torch.from_numpy(rewards).float()
        
        log_probs = torch.log(self.policy_net(states).gather(1, actions.unsqueeze(-1)))
        loss = -torch.mean(log_probs * rewards)
        
        self.optimizer.zero_grad()
        loss.backward()
        self.optimizer.step()
