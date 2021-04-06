from collections import defaultdict, deque


class Solution:
    def canFinish(self, numCourses, prerequisites):
        adjacent_nodes = defaultdict(list)
        node_weight = {course: 0 for course in range(numCourses)}
        result = []
        my_queue = deque()
        # build dependency nodes
        for course in prerequisites:
            adjacent_nodes[course[1]].append(course[0])
            node_weight[course[0]] += 1
        # Adding the Zero nodes to the queue
        for i in range(numCourses):
            if node_weight[i] == 0:
                my_queue.append(i)

        # Loop until we remove all the nodes from the graph
        while node_weight:
            try:
                node = my_queue.pop()
            except Exception:
                # if the there is no more zero nodes and we still have nodes that mean that
                # we have a cycle
                return []
            result.append(node)
            del node_weight[node]
            self.delete_all_edges(node, node_weight, adjacent_nodes, my_queue)
        return result

    def delete_all_edges(self, node, node_wight, adjacent_nodes, my_queue):
        edges = adjacent_nodes[node]

        for edge in edges:
            node_wight[edge] -= 1
            if node_wight[edge] == 0:
                my_queue.append(edge)
