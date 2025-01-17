This example shows a simple way to create a loop with Flojoy.
First, you'll need to place these three nodes:

The [`LOOP`](https://github.com/flojoy-io/nodes/blob/main/LOGIC_GATES/LOOPS/LOOP/LOOP.py) node which will define the number of loops.

The [`GOTO`](https://github.com/flojoy-io/nodes/blob/main/LOGIC_GATES/LOOPS/GOTO/GOTO.py) node will define where the loop ends. This node takes a parameter called 'referred_node' in which you can choose where the loop starts again (Generally, it's the [`LOOP`](https://github.com/flojoy-io/nodes/blob/main/LOGIC_GATES/LOOPS/LOOP/LOOP.py) node).

Lastly, we have an [`END`](https://github.com/flojoy-io/nodes/blob/main/LOGIC_GATES/TERMINATORS/END.py) node which is connected to the “end” output of the [`LOOP`](https://github.com/flojoy-io/nodes/blob/main/LOGIC_GATES/LOOPS/LOOP/LOOP.py) node, which serve, to terminate the program.

After that, we can place nodes to generate and visualize data within the loop.

In this example app, a random number is generated by the node ['RAND'](https://github.com/flojoy-io/nodes/blob/main/GENERATORS/SIMULATIONS/CONSTANT/CONSTANT.py) and multiplied with a constant defined by the user with the node [`CONSTANT`](https://github.com/flojoy-io/nodes/blob/main/GENERATORS/SIMULATIONS/CONSTANT/CONSTANT.py). Finally the result is displayed with the visualization node [`BIG_NUMBER`](https://github.com/flojoy-io/nodes/blob/main/VISUALIZERS/PLOTLY/BIG_NUMBER/BIG_NUMBER.py) and updated during each iteration of the loop.


After each iteration, the [`LOOP`](https://github.com/flojoy-io/nodes/blob/main/LOGIC_GATES/LOOPS/LOOP/LOOP.py) node checks if the remaining number of iterations is greater than zero. If so, it enqueues its body nodes again until the number of remaining iterations becomes zero. Finally, it enqueues the nodes connected to its "end" output.

