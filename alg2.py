import timeit

edges = [(1, 2), (2, 3), (2, 4), (4, 5), (1, 6), (6, 7), (4, 5)]

def get_vertices(edges):
    """Получение списка вершин из списка ребер."""
    vertices = set()
    for edge in edges:
        vertices.add(edge[0])
        vertices.add(edge[1])
    return list(vertices)

number = 1000
execution_time1 = timeit.timeit(lambda: get_vertices(edges), number = 1000)
print(f"time for end : { execution_time1:.6f} sec")
print (f"middle time: { execution_time1 / number :.9f} sec")

