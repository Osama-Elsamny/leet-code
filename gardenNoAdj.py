import collections


class Solution:
    def gardenNoAdj(self, N, paths):
        adjacent_nodes = collections.defaultdict(list)
        garden_to_flower_color = {garden: 0 for garden in range(1, N + 1)}
        result = []
        self.build_graph(adjacent_nodes, paths)
        for node in adjacent_nodes:
            flower_color = set(range(1, 5))
            for garden in adjacent_nodes[node]:
                if garden_to_flower_color[garden] != 0 and garden_to_flower_color[garden] in flower_color:
                    flower_color.remove(garden_to_flower_color[garden])
            garden_to_flower_color[node] = flower_color.pop()

        for x in range(1, N + 1):
            if garden_to_flower_color[x] != 0:
                result.append(garden_to_flower_color[x])
            else:
                result.append(1)
        return result

    # Build dependency graph
    def build_graph(self, adjacent_nodes, paths):
        for path in paths:
            adjacent_nodes[path[1]].append(path[0])
            adjacent_nodes[path[0]].append(path[1])


if __name__ == '__main__':
    N = 3
    paths = [[1, 2], [2, 3], [3, 1]]
    print(Solution().gardenNoAdj(N, paths))
