from enum import Enum


class Value(Enum):
    A0 = 0
    A1 = 1
    A2 = 2
    A3 = 3
    B1 = 4


class States(Enum):
    P = 0
    Q = 1


class System:
    __VALUE_INITIAL = 0
    __STATES_INITIAL = States.P

    def _input(self, var):
        if self.state == States.P:
            return self._p(var)
        if self.state == States.Q:
            return self._q(var)

    def _p(self, inp):
        if inp == Value.B1:
            self.z = 0
            return 1
        if inp == Value.A3:
            self.z += 1
            return 1
        if inp == Value.A0 or inp == Value.A1 or inp == Value.A2:
            self.z += 1
            self.state = States.Q
            return 0

    def _q(self, inp):
        if inp == Value.B1:
            self.z = 1
            return 1
        if self.z % 2 == 0:
            if inp == Value.A1 or inp == Value.A3:
                self.z += 1
            return 0
        if self.z % 2 == 1:
            self.z = 0
            self.state = States.P
            return 1

    def _reset(self):
        assert isinstance(self, System)
        self.z = System.__VALUE_INITIAL
        self.state = System.__STATES_INITIAL

    def process(self, seq):
        self._reset()
        assert self.z == System.__VALUE_INITIAL
        assert self.state == System.__STATES_INITIAL
        output = []
        for i in seq:
            o = self._input(i)
            output.append(o)
        return output
