import os
from collections import defaultdict
import operator


class DirectedAcyclicGraph:
    def __init__(self, skimap, shape):
        self.graph = defaultdict(list)
        self.skimap = skimap
        self.shape = shape
        self.length_map = []
        for i in range(shape[0]):
            # (initial max length, (initial start node coordinate))
            self.length_map.append([(0, (-1, -1))]*self.shape[1])

    def addedge(self,k,v):
        self.graph[k].append(v)


def builddag(ski_map, shape):
    dag = DirectedAcyclicGraph(ski_map, shape)
    # find difference between rows
    row_diff = []
    for m in range(shape[0]-1):
        row_diff.append(list(map(operator.sub, ski_map[m], ski_map[m+1])))
    # find difference between columns
    column_diff = []
    for m in range(shape[1]-1):
        column_diff.append(list(map(operator.sub, [row[m] for row in ski_map], [row[m+1] for row in ski_map])))
    # add row edges
    for i in range(shape[0]-1):
        for j in range(shape[0]):
            if row_diff[i][j] > 0:
                dag.addedge((i, j), (i+1, j))
            elif row_diff[i][j] < 0:
                dag.addedge((i+1, j), (i, j))
            else:
                pass
    # add column edges
    for i in range(shape[0]-1):
        for j in range(shape[0]):
            if column_diff[i][j] > 0:
                dag.addedge((j, i), (j, i+1))
            elif column_diff[i][j] < 0:
                dag.addedge((j, i+1), (j, i))
            else:
                pass
    return dag


def findlocalmax(n, dag):
    if dag.length_map[n[0]][n[1]][0] != 0:
        return dag.length_map[n[0]][n[1]]
    else:
        if n not in dag.graph:
            dag.length_map[n[0]][n[1]] = (1, n)
            return dag.length_map[n[0]][n[1]]
        else:
            possiblelocalmax = [findlocalmax(x, dag) for x in dag.graph[n]]
            maxtuple = [x for x in possiblelocalmax if x[0] == max([x[0] for x in possiblelocalmax])]
            localmax = min([x for x in maxtuple], key=lambda y: dag.skimap[y[1][0]][y[1][1]])
            dag.length_map[n[0]][n[1]] = (localmax[0]+1, localmax[1])
            return dag.length_map[n[0]][n[1]]


def generatepath(start, dag, path):
    path.append(start)
    if start in dag.graph:
        for x in dag.graph[start]:
            if (dag.length_map[x[0]][x[1]][0] == dag.length_map[start[0]][start[1]][0]-1 and
                    dag.length_map[x[0]][x[1]][1] == dag.length_map[start[0]][start[1]][1]):
                generatepath(x, dag, path)
    return path


def main():
    cwd = os.getcwd()
    file_path = os.path.join(cwd, 'ski_map_sample2.txt')
    ski_map = []
    with open(file_path) as f:
        shape = [int(x) for x in f.readline().split(' ')]
        for line in f:
            ski_map.append([int(x) for x in line.split(' ')])
    dag = builddag(ski_map, shape)
    max_length = max_drop = -1
    start_node = end_node = (-1, -1)
    for n in dag.graph:
        localmax = findlocalmax(n, dag)
        if (max_length < localmax[0] or
        (max_length == localmax[0] and max_drop < ski_map[n[0]][n[1]] - ski_map[localmax[1][0]][localmax[1][1]])):
            max_length = localmax[0]
            start_node = n
            end_node = localmax[1]
            max_drop = ski_map[start_node[0]][start_node[1]] - ski_map[end_node[0]][end_node[1]]

    path = generatepath(start_node, dag, [])
    value = []
    for n in path:
        value.append(ski_map[n[0]][n[1]])
    print(max_length, max_drop)
    print(path)
    print(value)


if __name__ == '__main__':
    main()
