# RxPy Test

A few files demonstrating custom observables. Originally created to test parallel HTTP requests, but abandoned when `ThreadPoolScheduler` couldn't be figured out.

- `simple.py`: Standalone synchronous observable demo
- `mock-server.py`: Server that sleeps when `?delay=int` is detected. Run before `rx-test.py`
- `rx-test.py`: Request implementation of the POC in `simple.py`


A public gist was create for this: https://gist.github.com/emcniece/0a893f4c86df566a5c6464d0b06c9b32/edit
