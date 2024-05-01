import heapq


def make_graph():
    
    # tuple = (cost, n1, n2)
    return {
        'A': [(3, 'D', 'A'), (4, 'B', 'A'), (5, 'E', 'A')],
        'B': [(4, 'A', 'B'), (2, 'C', 'B')],
        'C': [(2, 'B', 'C'),(1, 'D', 'C')],
        'D': [(3, 'A', 'D'), (1, 'C', 'D')],
        'E': [(5, 'A', 'E')],
    }


def prims(G, start='A'):
    unvisited = list(G.keys())
    visited = []
    total_cost = 0
    MST = []

    unvisited.remove(start)
    visited.append(start)

    heap = G[start]
    heapq.heapify(heap)

    while unvisited:
        (cost, n2, n1) = heapq.heappop(heap)
        new_node = None

        if n1 in unvisited and n2 in visited:
            new_node = n1
            MST.append((n2, n1, cost))

        elif n1 in visited and n2 in unvisited:
            new_node = n2
            MST.append((n1, n2, cost))

        if new_node != None:
            unvisited.remove(new_node)
            visited.append(new_node)
            total_cost += cost

            for node in G[new_node]:
                heapq.heappush(heap, node)

    return MST, total_cost


def main():
    G = make_graph()
    MST, total_cost = prims(G, 'A')

    print(f'Minimum spanning tree: {MST}')
    print(f'Total cost: {total_cost}')


main()


# Output :
# Minimum spanning tree: [('A', 'D', 3), ('D', 'C', 1), ('C', 'B', 2), ('A', 'E', 5)]
# Total cost: 11
