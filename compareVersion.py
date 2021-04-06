class Solution:
    def compareVersion(self, version1, version2):
        version1_list = version1.split('.')
        version2_list = version2.split('.')
        version2_len = len(version2_list)
        version1_len = len(version1_list)

        longer_len = version2_len if version2_len > version1_len else version1_len
        for i in range(longer_len):
            version1_int = int(version1_list[i]) if i < version1_len else 0
            version2_int = int(version2_list[i]) if i < version2_len else 0
            if version1_int > version2_int:
                return 1
            elif version1_int < version2_int:
                return -1
        return 0


if __name__ == '__main__':
    # test 1
    version1 = "0.1"
    version2 = "1.1"

    # test 2
    # version1 = "1.0.1"
    # version2 = "1"

    # test 3
    # version1 = "7.5.2.4"
    # version2 = "7.5.3"

    # test 4
    # version1 = "1.01"
    # version2 = "1.001"

    # test 5
    # version1 = "1.0"
    # version2 = "1.0.0"

    print(Solution().compareVersion(version1, version2))
