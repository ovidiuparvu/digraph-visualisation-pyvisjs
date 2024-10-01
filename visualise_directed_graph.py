from pyvisjs.network import Network

# Create a directed graph
net = Network(options={"edges": {"arrows": {"to": True}}})

# Add nodes
net.add_node("1", label='Node 1', color="red")
net.add_node("2", label='Node 2')
net.add_node("3", label='Node 3')

# Add edges
net.add_edge("1", "2")
net.add_edge("2", "3")
net.add_edge("3", "1")

# Visualize the graph
net.show('directed_graph.html')
