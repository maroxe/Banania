class State(object):

    is_paused = False
    is_stopped = False

    def start(self):
        pass

    def update(self, **kwargs):
        return not self.is_stopped

    def pause(self):
        self.is_paused = True
        print 'state %s paused' % self.__class__

    def unpause(self):
        self.is_paused = False
        print 'state %s unpaused' % self.__class__

    def stop(self):
        self.is_stopped = True

    def on_stop(self):
        print 'state %s stopped' % self.__class__


class StateManager(object):
    def __init__(self):
        self.states = []

    def loop(self):
        while self.states != []:
            self.update()

    def update(self, **kwargs):
        last_state_quit = False
        for s in self.states:
            last_state_quit = not s.update(**kwargs)
        if last_state_quit:
            self.pop_state()
        return len(self.states)

    def pop_state(self):
        if self.states:
            self.states.pop().on_stop()
        if self.states:
            self.states[-1].unpause()

    def push_state(self, s):
        if self.states:
            self.states[-1].pause()
        self.states.append(s)
