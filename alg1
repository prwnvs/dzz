import timeit

edges = [(1, 2), (2, 3), (2, 4), (4, 5), (1, 6), (6, 7), (4, 5)]

def count_vertices(edges):
    """Подсчет количества вершин в графе."""
    vertices = set()
    for edge in edges:
        vertices.add(edge[0])
        vertices.add(edge[1])
    return len(vertices)

execution_time1 = timeit.timeit(lambda: count_vertices(edges), number = 1000)
print(f"time for end : {execution_time1:.6f} sec")
print (f"middle time: { execution_time1 / number :.9f} sec")

