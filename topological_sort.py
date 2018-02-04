import os
import operator
from collections import defaultdict
from itertools import chain


class DirectedAcyclicGraph:
    def __init__(self, size, skiMap):
        self.graph_out = defaultdict(list)
        self.graph_in = defaultdict(list)
        self.shape = size
        self.ski_map = skiMap

    def addEdgeOut(self, u, v):
        self.graph_out[u].append(v)

    def addEdgeIn(self, u, v):
        self.graph_in[u].append(v)

    def showEdge(self):
        print(self.graph_out)

    def topologicalSort(self):
        in_degree = []
        for i in range(self.shape[0]):
            in_degree.append([0]*(self.shape[1]))

        for i in self.graph_out:
            for j in self.graph_out[i]:
                in_degree[j[0]][j[1]] += 1

        queue = []
        for i in range(self.shape[0]):
            for j in range(self.shape[1]):
                if in_degree[i][j] == 0:
                    queue.append((i, j))

        cnt = 0
        top_order = []

        while queue:
            u = queue.pop(0)
            top_order.append(u)

            for i in self.graph_out[u]:
                in_degree[i[0]][i[1]] -= 1
                if in_degree[i[0]][i[1]] == 0:
                    queue.append(i)
            cnt += 1

        if cnt != self.shape[0]*self.shape[1]:
            print("There exists a cycle in the graph!")
            return None
        else:
            self.order = top_order
            return self.order

    def findLongestPath(self):
        path_map = []
        for i in range(self.shape[0]):
            path_map.append([-1]*(self.shape[1]))
        for i in self.order:
            if i not in self.graph_in:
                path_map[i[0]][i[1]] = 0
            else:
                path_map[i[0]][i[1]] = max([path_map[j[0]][j[1]] for j in self.graph_in[i]]) + 1

        start_nodes = []
        max_length = max(chain.from_iterable(path_map))
        for i in range(self.shape[0]):
            for j in range(self.shape[1]):
                if path_map[i][j] == max_length:
                    start_nodes.append((i,j))
        max_drop = 0
        longest_path = []
        for i in start_nodes:
            drop, longest_path = self.dfs([i], path_map)
            if drop > max_drop:
                max_drop = drop
        return max_length+1, max_drop, longest_path, [self.ski_map[x[0]][x[1]] for x in longest_path]

    def dfs(self, opening, pathMap):
        search_path = defaultdict(list)
        start_node_value = self.ski_map[opening[0][0]][opening[0][1]]
        max_drop = 0
        while opening:
            n = opening.pop(0)
            if pathMap[n[0]][n[1]] == 0:
                if max_drop < self.ski_map[n[0]][n[1]] - start_node_value:
                    max_drop = self.ski_map[n[0]][n[1]] - start_node_value
                    max_node = (n[0], n[1])
            else:
                temp_max = max([pathMap[x[0]][x[1]] for x in self.graph_in[n]])
                for x in self.graph_in[n]:
                    if pathMap[x[0]][x[1]] == temp_max:
                        opening.insert(0, x)
                        search_path[x] = n
        longest_path = []
        longest_path.append(max_node)
        while max_node in search_path:
            max_node = search_path[max_node]
            longest_path.append(max_node)
        return max_drop, longest_path


cwd = os.getcwd()
file_path = os.path.join(cwd, 'ski_map_sample2.txt')
ski_map = []
with open(file_path) as f:
    size = [int(x) for x in f.readline().split(' ')]
    for line in f:
        ski_map.append([int(x) for x in line.split(' ')])


def build_dag(skimap):
    dag = DirectedAcyclicGraph(size, ski_map)
    # find difference between rows
    row_diff = []
    for m in range(size[0]-1):
        row_diff.append(list(map(operator.sub, ski_map[m], ski_map[m+1])))
    # find difference between columns
    column_diff = []
    for m in range(size[1]-1):
        column_diff.append(list(map(operator.sub, [row[m] for row in ski_map], [row[m+1] for row in ski_map])))
    # add row edges
    for i in range(size[0]-1):
        for j in range(size[0]):
            if row_diff[i][j] > 0:
                dag.addEdgeOut((i, j), (i+1, j))
                dag.addEdgeIn((i+1, j), (i, j))
            elif row_diff[i][j] < 0:
                dag.addEdgeOut((i+1, j), (i, j))
                dag.addEdgeIn((i, j), (i+1, j))
            else:
                pass
    # add column edges
    for i in range(size[0]-1):
        for j in range(size[0]):
            if column_diff[i][j] > 0:
                dag.addEdgeOut((j, i), (j, i+1))
                dag.addEdgeIn((j, i+1), (j, i))
            elif column_diff[i][j] < 0:
                dag.addEdgeOut((j, i+1), (j, i))
                dag.addEdgeIn((j, i), (j, i+1))
            else:
                pass
    return dag


dag = build_dag(ski_map)
# dag.showEdge()
top_order = dag.topologicalSort()
length, drop, path, value = dag.findLongestPath()
print(length, drop)
print(path)
print(value)

