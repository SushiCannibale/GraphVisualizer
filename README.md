# GraphVisualizer
GraphVisualizer is a simple python project that uses PyGame library to help visualizing a graph.

# How to use
Import the library and instanciate the `GraphRenderer` class using a dictionnary-based representation of your graph (see example below).
Then simply call the `draw()` method and you're good to go :D

```python
from graph_visualizer import GraphRenderer

dict_graph = {'A':['B', 'C'], 'B':['A', 'C'], 'C':['A', 'B']}

graph = GraphRenderer(dict_graph)
graph.draw()
```

## `GraphRenderer` class

The `GraphRenderer` can take at least 3 keywords arguments:
- `int` `node_radius`: Changes the radius of each node of the graph
- `int` `base_length`: Changes the minimal distance of a node to the center of the screen
- `int` `length_offset`: Whenever the base circle on which are drawn the nodes is too small, this value will increase the `base_length` to match a fairly good value.
- `int` `base_offset`: Modifies the offset distance between each nodes
