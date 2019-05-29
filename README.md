Building Finite State Machine and Mutation Testing for ISP RAS
--
1. Get automat
2. Build FSM
3. Write textual description `test.fsm`
4. Generate test sequences [lib here](http://github.com/kitidis/fsm)
5. Use test sequences to Testing with [mutPy](https://github.com/mutpy/mutpy)
6. run with `mut.py --target avtomat --unit-test test_avtomat -m` 
