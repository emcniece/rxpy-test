# Example: Custom observable creation for switchmapping.
# Library: https://github.com/ReactiveX/RxPY
# Requires: `Rx==3.0.0b4` or greater. `pip3 install --pre rx`
#

import time
import rx
from rx import operators as op


# Accept a value (emission), return an observable that doubles its input.
# Sleeps to simulate synchronous behaviour.
def to_double(val):
    def subscribe(observer, dispose):
        try:
            time.sleep(val)
            observer.on_next(val*2)
        except TypeError:
            observer.on_error("Error doubling val:", val)

    return rx.create(subscribe)


# Initial stream of values (emissions)
source = rx.of(1, 2, 3)

# Pipe: perform actions on a stream of emissions
composed = source.pipe(
    # do_action: Operate on & forward value to next action.
    # Unpacks emission so `print` sees the actual emission value.
    op.do_action(print),

    # Replace the original emission with a new observable
    op.flat_map(to_double)
)

# Activate the stream (turn it "hot") by subscribing:
composed.subscribe(lambda output: print("Final value:", output))

'''
Sample output:
1
Final value: 2
2
Final value: 4
3
Final value: 6
'''
