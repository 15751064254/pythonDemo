#!/usr/bin/python
# vim: set fileencoding=utf-8:

# 导入环境和学习方法
from env import ArmEnv
from rl import DDPG

# 设置全局变量
MAX_EPISODES = 500
MAX_EP_STEPS = 200
# ON_TRAIN = True
ON_TRAIN = False

# 设置环境
# set env
env = ArmEnv()
s_dim = env.state_dim
a_dim = env.action_dim
a_bound = env.action_bound

# 设置学习方法(这里使用 DDPG)
# set RL method (continuous)
rl = DDPG(a_dim, s_dim, a_bound)

steps = []

# 开始训练
def train():
    # start training
    for i in range(MAX_EPISODES):
        s = env.reset() # 初始化回合设置
        ep_r = 0.
        for j in range(MAX_EP_STEPS):
            # env.render()    # 环境的渲染
            a = rl.choose_action(s) # RL 选择动作
            s_, r, done = env.step(a)   # 在环境中施加动作
            rl.store_transition(s, a, r, s_)    # DDPG 这种强化学习需要存放记忆库
            ep_r += r
            if rl.memory_full:
                # start to learn once has fulfilled the memory
                rl.learn()  # 记忆库满了，开始学习

            s = s_  # 变为下一回合
            if done or j == MAX_EP_STEPS-1:
                print('Ep: %i | %s | ep_r: %.1f | step: %i' % (i, '---' if not done else 'done', ep_r, j))
                break

    rl.save()

# 开始测试
def eval():
    rl.restore()    # 提取网络
    env.render()
    env.viewer.set_vsync(True)
    while True:
        s = env.reset()
        for _ in range(200):
            env.render()
            a = rl.choose_action(s)
            s, r, done = env.step(a)
            if done:
                break


if ON_TRAIN:
    train()
else:
    eval()
