import unittest
from statemanager import State, StateManager


class StateManagerTest(unittest.TestCase):

    def test_push(self):
        mgr = StateManager()
        for _ in range(10):
            mgr.push_state(State())
        for _ in range(10):
            mgr.pop_state()
        self.assertTrue(mgr.states == [])


if __name__ == '__main__':
    unittest.main()
