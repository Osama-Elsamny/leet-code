class Solution:
    def search(self, nums, target):
        if not nums:
            return False
        return self.binarySerachRotatedArrayWithDuplicates(nums, 0, len(nums) - 1, target)

    def binarySerachRotatedArray(self, arr, left, right, elem):
        while left <= right:
            mid = left + (right - left) // 2
            if arr[mid] == elem:
                return mid
            elif arr[mid] >= arr[left]:
                # not rotated left side
                if arr[left] <= elem < arr[mid]:
                    right = mid - 1
                else:
                    left = mid + 1
            else:
                # not rotated right side
                if arr[mid] < elem <= arr[right]:
                    left = mid + 1
                else:
                    right = mid - 1
        return -1

    def binarySerachRotatedArrayWithDuplicates(self, arr, left, right, elem):
        while left <= right:
            mid = left + (right - left) // 2
            if arr[mid] == elem:
                return True
            elif arr[mid] > arr[left]:
                # not rotated left side
                if arr[left] <= elem < arr[mid]:
                    right = mid - 1
                else:
                    left = mid + 1
            elif arr[mid] < arr[left]:
                # not rotated right side
                if arr[mid] < elem <= arr[right]:
                    left = mid + 1
                else:
                    right = mid - 1
            else:
                left += 1
        return False


if __name__ == '__main__':
    # nums = [4, 5, 6, 7, 0, 1, 2]
    # nums = [4, 5, 6, 7, 8, 1, 2, 3]
    nums = [1, 3, 1, 1, 1]
    target = 3
    # nums = [3, 1]
    # target = 1
    print(Solution().search(nums, target))
