def search_graph(start):

    qu = []
    done = set()

    search_info = {
        1: [2, 3],
        2: [4, 5, 1],
        3: [1],
        4: [2],
        5: [2]
    }

    qu.append((start, 0))
    done.add(start)

    while qu:
        vertex, depth = qu.pop(0)
        print(vertex, depth)

        for x in search_info[vertex]:
            if x in done:
                continue
            qu.append((x, depth + 1))
            done.add(x)


search_graph(6)
