# env.py
# -*- coding:utf-8 -*-

import numpy as np
import pyglet


class Env(object):
    viewer = None  # 首先没有 viewer
    dt = .1  # refresh rate # 转动的速度和 dt 有关
    action_bound = [-1, 1]  # 转动的角度范围
    goal = {'x': 100., 'y': 100., 'l': 40}  # 蓝色 goal 的 x,y 坐标和长度
    state_dim = 9  # 观测值 state 的维度变到 9
    action_dim = 2  # 两个动作

    def __init__(self):
        # 生成出(2, 2)的矩阵
        self.arm_info = np.zeros(2, dtype=[('l', np.float32), ('r', np.float32)])

        self.arm_info['l'] = 100  # 2 arms length # 两个手臂的长度
        self.arm_info['r'] = np.pi / 6  # 2 angles information  # 两段手臂的端点角度
        self.on_goal = 0

    def step(self, action):
        done = False
        # 计算单位时间 dt 内旋转的角度,将角度限制在360度以内
        action = np.clip(action, *self.action_bound)
        self.arm_info['r'] += action * self.dt
        self.arm_info['r'] %= np.pi * 2  # normalize

        # 如果手指接触到蓝色的 goal, 我们判定结束回合 (done)
        # 所以需要计算 finger 的坐标
        (a1l, a2l) = self.arm_info['l']  # radius, arm length
        (a1r, a2r) = self.arm_info['r']  # radian, angle
        a1xy = np.array([200., 200.])  # a1 start (x0, y0)
        a1xy_ = np.array([np.cos(a1r), np.sin(a1r)]) * a1l + a1xy  # a1 end and a2 start (x1, y1)
        finger = np.array([np.cos(a1r + a2r), np.sin(a1r + a2r)]) * a2l + a1xy_  # a2 end(x2, y2)

        # normalize features
        dist1 = [(self.goal['x'] - a1xy_[0]) / 400, (self.goal['y'] - a1xy_[1]) / 400]
        # dist2 是 finger 离 goal 的 x, y 方向的距离
        dist2 = [(self.goal['x'] - finger[0]) / 400, (self.goal['y'] - finger[1]) / 400]
        r = -np.sqrt(dist2[0]**2 + dist2[1]**2)

        # 根据 finger 和 goal 的坐标得出 done and reward
        # done and reward
        if self.goal['x'] - self.goal['l'] / 2 < finger[0] < self.goal['x'] + self.goal['l'] / 2:

            if self.goal['y'] - self.goal['l'] / 2 < finger[1] < self.goal['y'] + self.goal['l'] / 2:

                r += 1.  # finger 在 goal 以内
                if self.on_goal > 50:
                    done = True

        else:
            self.on_goal = 0

        # state
        s = np.concatenate(
            (a1xy_ / 200, finger / 200, dist1 + dist2, [1. if self.on_goal else 0.])
        )

        return s, r, done

    def reset(self):
        self.arm_info['r'] = 2 * np.pi * np.random.rand(2)
        self.on_goal = 0

        s = np.concatenate()
        return s

    def render(self):
        # 如果调用了 render, 而且没有 viewer, 就生产一个
        if self.viewer is None:  
            self.viewer = Viewer(self.arm_info, self.goal)
        self.viewer.render()  # 使用 Viewer 中的 render 功能

    def sample_action(self):
        return np.random.rand(2) - 0.5  # tow radians


class Viewer(pyglet.window.Window):
    bar_thc = 5  # 手臂的厚度

    # 画出手臂等
    def __init__(self, arm_info, goal):
        # 创建窗口的继承
        # vsync 如果是 True, 按屏幕频率刷新, 反之不按程序频率
        # vsync = False to not use the monitor FPS, we can speed up training
        super(Viewer, self).__init__(
            width=400, height=400, resizable=False, caption='Env', vsync=False)

        # 窗口背景颜色
        pyglet.gl.glClearColor(1, 1, 1, 1)
        
        # 添加 arm 信息
        self.arm_info = arm_info

        # 添加窗口中心点, 手臂的根
        self.center_coord = np.array([200, 200])

        self.batch = pyglet.graphics.Batch()  # display whole batch at noce

        # 蓝色 goal 的信息包括他的 x,y 坐标, goal 的长度
        self.goal = self.batch.add(
            4, pyglet.gl.GL_QUADS, None,  # 4 corners
            ('v2f', [goal['x'] - goal['l'] / 2, goal['y'] - goal['l'] / 2,
                    goal['x'] - goal['l'] / 2, goal['y'] + goal['l'] / 2,
                    goal['x'] + goal['l'] / 2, goal['y'] + goal['l'] / 2,
                    goal['x'] + goal['l'] / 2, goal['y'] - goal['l'] / 2, 
                    ]),
            ('c3B', (86, 109, 249) * 4)  # color
        )

        self.arm1 = self.batch.add(
            4, pyglet.gl.GL_QUADS, None,
            ('v2f', [250, 250,  # location
                    250, 300,
                    260, 300,
                    260, 250,
                    ]),
            ('c3B', (249, 86, 86) * 4)  # color
        )

        self.arm2 = self.batch.add(
            4, pyglet.gl.GL_QUADS, None,
            ('v2fl', [100, 150,
                     100, 160,
                     200, 160,
                     200, 150,
                     ]),
            ('c3B', (249, 86, 86) * 4)
        )

    # 刷新并呈现在屏幕上
    def render(self):
        self._update_arm()  # 更新手臂内容(暂时没有变化)
        self.switch_to()
        self.dispatch_events()
        self.dispatch_event('on_draw')
        self.flip()

    # 刷新手臂等位置
    def on_draw(self):
        self.clear()  # 清屏
        self.batch.draw()  # 画上 batch 里面的内容

    # 更新手臂的位置信息
    def _update_arm(self):
        (a1l, a2l) = self.arm_info['l']  # radius, arm length
        (a1r, a2r) = self.arm_info['r']  # radian, angle
        a1xy = self.center_coord  # a1 start(x0, y0)
        a1xy_ = np.array([np.cos(a1r), np.sin(a1r)]) * a1l + a1xy  # a1 end and a2 start(x1, y1)
        a2xy_ = np.array([np.cos(a1r + a2r), np.sin(a1r + a2r)]) * a2l + a1xy_  # a2 end(x2, y2)

        # 第一段手臂的4个点信息
        a1tr, a2tr = np.pi / 2 - self.arm_info['r'][0], np.pi / 2 - self.arm_info['r'].sum()
        xy01 = a1xy + np.array([-np.cos(a1tr), np.sin(a1tr)]) * self.bar_thc
        xy02 = a1xy + np.array([np.cos(a1tr), -np.sin(a1tr)]) * self.bar_thc
        xyl1 = a1xy_ + np.array([np.cos(a1tr), -np.sin(a1tr)]) * self.bar_thc
        xyl2 = a1xy_ + np.array([-np.cos(a1tr), np.sin(a1tr)]) * self.bar_thc

        # 第二段手臂的4个点信息
        xy11_ = a1xy_ + np.array([np.cos(a2tr), -np.sin(a2tr)]) * self.bar_thc
        xy12_ = a1xy_ + np.array([-np.cos(a2tr), np.sin(a2tr)]) * self.bar_thc
        xy21 = a2xy_ + np.array([-np.cos(a2tr), np.sin(a2tr)]) * self.bar_thc
        xy22 = a2xy_ + np.array([np.cos(a2tr), -np.sin(a2tr)]) * self.bar_thc

        # 将点信息都放入手臂显示中
        self.arm1.vertices = np.concatenate((xy01, xy02, xyl1, xyl2))
        self.arm2.vertices = np.concatenate((xy11_, xy12_, xy21, xy22))


if __name__ == '__main__':
    env = Env()
    while True:
        env.render()
        env.step(env.sample_action())
