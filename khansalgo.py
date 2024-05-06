sorted_list = []
process = []

# add all vertices without incoming edges to process (queue)

while len (process) > 0:
    vertex_u = process.pop()
    sorted_list.append(vertex_u)
    for edge in vertex_u.edges:
        edge.remove_from_graph()
        if len(edge.vertex_v.incoming_edges) == 0:
            process.append(vertex_v)

if graph.has_edges():
    print("Error, Not a cycle")
else:
    print(sorted_list)