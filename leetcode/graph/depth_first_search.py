import pprint


def adj_to_neighbors(adj):
    neighbors = dict()

    for src, dst in adj:
        if src not in neighbors:
            neighbors[src] = set()
        neighbors[src].add(dst)

    return neighbors


def depth_first_search(adj):
    neighbors = adj_to_neighbors(adj)

    visited = set()
    path = set()

    history = {'time': 0}
    edge_class = dict()
    topology = []

    def visit(node, neighbors, tree):
        assert node not in visited

        visited.add(node)
        path.add(node)
        tree.add(node)

        history[node] = history['time']
        history['time'] += 1

        if node in neighbors:

            for neighbor in neighbors[node]:
                edge = (node, neighbor)
                if neighbor in tree and history[neighbor] > history[node]:
                    edge_class[edge] = 'forward'
                elif neighbor in path:
                    edge_class[edge] = 'backward'
                elif neighbor in visited:
                    edge_class[edge] = 'cross'
                else:
                    edge_class[edge] = 'tree'
                    visit(neighbor, neighbors, tree)

        topology.insert(0, node)
        path.remove(node)

    for src, dst in adj:
        if src not in visited:
            visit(src, neighbors, set())

    return edge_class, history, topology


adj = [
    (1, 2),
    (1, 5),
    (1, 7),
    (2, 3),
    (2, 4),
    (3, 1),
    (3, 5),
    (4, 3),
    (6, 7),
    (7, 8),
    (8, 5)
]

expected_classes = {
    (1, 2): 'tree',
    (2, 3): 'tree',
    (3, 1): 'backward',
    (3, 5): 'tree',
    (2, 4): 'tree',
    (4, 3): 'cross',
    (1, 5): 'forward',
    (1, 7): 'tree',
    (7, 8): 'tree',
    (8, 5): 'cross',
    (6, 7): 'cross'
}

actual_classes, actual_history, topology = depth_first_search(adj)

pprint.PrettyPrinter(indent=4).pprint(actual_classes)
assert expected_classes == actual_classes
