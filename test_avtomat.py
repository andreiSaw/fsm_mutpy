import unittest
import avtomat
from avtomat import Value

W = [
    [Value.B, Value.A0, Value.A0],
    [Value.B, Value.A3],
    [Value.A0, Value.B, Value.A0],
    [Value.A0, Value.A0, Value.A0, Value.A0],
    [Value.A0, Value.A0, Value.A3],
    [Value.A0, Value.A1, Value.A0, Value.A0],
    [Value.A0, Value.A1, Value.A3],
    [Value.A0, Value.A2, Value.A0, Value.A0],
    [Value.A0, Value.A2, Value.A3],
    [Value.A0, Value.A3, Value.A0, Value.A0],
    [Value.A0, Value.A3, Value.A3],
    [Value.A1, Value.A0],
    [Value.A2, Value.A0],
    [Value.A3, Value.B, Value.A0, Value.A0],
    [Value.A3, Value.B, Value.A3],
    [Value.A3, Value.A0, Value.B, Value.A0],
    [Value.A3, Value.A0, Value.A0, Value.A0],
    [Value.A3, Value.A0, Value.A0, Value.A3],
    [Value.A3, Value.A0, Value.A1, Value.A0],
    [Value.A3, Value.A0, Value.A2, Value.A0],
    [Value.A3, Value.A0, Value.A2, Value.A3],
    [Value.A3, Value.A0, Value.A3, Value.A0],
    [Value.A3, Value.A1, Value.A0],
    [Value.A3, Value.A1, Value.A3],
    [Value.A3, Value.A2, Value.A0],
    [Value.A3, Value.A2, Value.A3],
    [Value.A3, Value.A3, Value.A0, Value.A0],
    [Value.A3, Value.A3, Value.A3]
]
out_W = [
    [1, 0, 1],
    [1, 1],
    [0, 1, 1],
    [0, 1, 0, 1],
    [0, 1, 1],
    [0, 1, 0, 1],
    [0, 1, 1],
    [0, 1, 0, 1],
    [0, 1, 1],
    [0, 1, 0, 1],
    [0, 1, 1],
    [0, 1],
    [0, 1],
    [1, 1, 0, 1],
    [1, 1, 1],
    [1, 0, 1, 1],
    [1, 0, 0, 0],
    [1, 0, 0, 0],
    [1, 0, 0, 1],
    [1, 0, 0, 0],
    [1, 0, 0, 0],
    [1, 0, 0, 1],
    [1, 0, 0],
    [1, 0, 0],
    [1, 0, 0],
    [1, 0, 0],
    [1, 1, 0, 1],
    [1, 1, 1]
]


class TestStringMethods(unittest.TestCase):
    def test_hsi(self):
        ins = avtomat.System()
        for (_input, _output) in list(zip(W, out_W)):
            self.assertEqual(ins.process(_input), _output)


if __name__ == '__main__':
    unittest.main()
