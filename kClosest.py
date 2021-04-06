class Solution:
    def kClosest(self, points, K):
        my_dict = {}
        dis_set = set()
        my_result = []
        for list in points:
            dis = list[0] ** 2 + list[1] ** 2
            dis_set.add(dis)
            if dis not in my_dict:
                my_dict[dis] = []
            my_dict[dis].append(list)

        sort_dis_set = sorted(dis_set)

        for i in sort_dis_set:
            if K > 0:
                temp_list = my_dict[i]
                my_result.extend(temp_list)
                K -= len(temp_list)

        return my_result


if __name__ == '__main__':
    points = [[1, 3], [-2, 2], [-2, 2], [-2, 2]]
    K = 4
    print(Solution().kClosest(points, K))
