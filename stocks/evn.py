import numpy as np
import pyglet

class Env(object):
    biewer = None

    def __init__(self):

    def step(self, action):
        done = False

    def reset(self):

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



if __name__ == '__main__':
    env = Env()
    while True:
        env.render()
        env.step(env.sample_action())
