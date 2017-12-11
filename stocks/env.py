import numpy as np
import pyglet

class Env(object):
    viewer = None
    dt = .1
    action_bound = [-1, 1]
    goal = {'x': 100., 'y': 100., 'l': 40}
    state_dim = 9
    action_dim = 2
    target = 1000

    def __init__(self):
        self.arm_info = np.zeros(2, dtype=[('l', np.float32), ('r', np.float32)])
        self.arm_info['l'] = 100
        self.arm_info['r'] = 200
        self.on_goal = 0

    def step(self, action):
        done = False
        r = 2
        s = 1
        return s, r, done

    def reset(self):
        s = np.concatenate()
        return s


    def render(self):
        if self.viewer is None:
            self.viewer = Viewer(self.arm_info, self.goal)
        self.viewer.render()

    def sample_action(self):
        return np.random.rand(2) - 0.5  # tow radians



class Viewer(pyglet.window.Window):
    bar_thc = 5

    def __init__(self, arm_info, goal):
        # vsync = False to not use the monitor FPS, we can speed up training
        super(Viewer, self).__init__(width=400, height=400, resizable=False, caption='Env', vsync=False)
        pyglet.gl.glClearColor(1, 1, 1, 1)
        self.batch = pyglet.graphics.Batch()

        self.arm_info = arm_info


    def render(self):
        self._update_arm()
        self.switch_to()
        self.dispatch_events()
        self.dispatch_event('on_draw')
        self.flip()


    def on_draw(self):
        self.clear()
        self.batch.draw()

    def _update_arm(self):
        return 0




if __name__ == '__main__':
    env = Env()
    while True:
        env.render()
        #env.step(env.sample_action())
