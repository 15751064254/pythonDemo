# -*- coding:utf-8 -*-

from env import Env
from rl import DDPG

ON_TRAIN = True

MAX_EPISODES = 500
MAX_EP_STEPS = 200

# set env
env = Env()
s_dim = env.state_dim
a_dim = env.action_dim
a_bound = env.action_bound

# set rl
rl = DDPG()

def train():
    for i in range(MAX_EPISODES):
        ep_r = 0.
        for j in range(MAX_EP_STEPS):


    rl.save()

def eval():
    rl.restore()




if ON_TRAIN:
    train()
else:
    eval()
