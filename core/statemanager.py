class State:

    def start(self):
        pass

    def update(self):
        return True

    def pause(self):
        pass

    def unpause(self):
        pass

    def stop(self):
        pass


class StateManager:
    def __init__(self):
        self.states = []

    def loop(self):
        while self.states != []:
            self.update()

    def update(self):
        last_state_quit = False
        for s in self.states:
            last_state_quit = not s.update()
        return last_state_quit

    def pop_state(self):
        if self.states:
            self.states.pop().stop()
        if self.states:
            self.states[-1].unpause()

    def push_state(self, s):
        if self.states:
            self.states[-1].pause()
            self.states.append(s)
