import collections
import sys


class Solution:
    def shortestDistance(self, maze, start, destination):
        if not maze:
            return -1
        row = len(maze)
        col = len(maze[0])
        my_queue = collections.deque([start])
        distance = collections.defaultdict(lambda: sys.maxsize)
        distance[(start[0], start[1])] = 0
        dirs = [[0, 1], [0, -1], [-1, 0], [1, 0]]

        while my_queue:
            curr = my_queue.popleft()

            #  We're not suppose to have this here because we want the shortest distance
            #  not any distance, the distance recorded there might not be the smallest
            # if curr == destination:
            #     return distance[(curr[0], curr[1])]

            for dir in dirs:
                x = curr[0]
                y = curr[1]
                count = 0
                while self.is_vaild(x + dir[0], y + dir[1], maze, row, col):
                    x += dir[0]
                    y += dir[1]
                    count += 1

                if distance[(curr[0], curr[1])] + count < distance[(x, y)]:
                    distance[(x, y)] = distance[(curr[0], curr[1])] + count
                    my_queue.append([x, y])

        return distance[(destination[0], destination[1])] if distance[(
            destination[0], destination[1])] != sys.maxsize else -1

    def is_vaild(self, x, y, maze, row, col):
        return 0 <= x < row and 0 <= y < col and maze[x][y] == 0


if __name__ == '__main__':
    maze = [[0, 0, 1, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 1, 0], [1, 1, 0, 1, 1], [0, 0, 0, 0, 0]]
    start = [0, 4]
    des = [4, 4]
    print(Solution().shortestDistance(maze, start, des))
