class Solution:
    def findOrder(self, numCourses, prerequisites):
        matrix = [[False for _ in range(numCourses)] for _ in range(numCourses)]
        sort = []
        node_weight = {course: 0 for course in range(numCourses)}
        # build dependency matrix
        for course in prerequisites:
            matrix[course[1]][course[0]] = True
            node_weight[course[0]] += 1

        while node_weight:
            node = self.findNextZero(node_weight)
            if node is None:
                return []
            sort.append(node)
            del node_weight[node]
            self.deleteAllEdges(node, node_weight, matrix)
        return sort

    def deleteAllEdges(self, node, node_wight, matrix):
        edges = matrix[node]
        for i, edge in enumerate(edges):
            if edge:
                node_wight[i] -= 1

    def findNextZero(self, my_map):
        for k in my_map:
            if my_map[k] == 0:
                return k


if __name__ == '__main__':
    numCourses = 2
    arr = [[1, 0]]
    print(Solution().findOrder(numCourses, arr))
