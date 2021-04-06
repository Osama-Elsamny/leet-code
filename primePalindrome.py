class Solution:
    def primePalindrome(self, N):
        i = N
        while True:
            if self.is_palindrome(i):
                if self.is_prime(i):
                    return i
            i += 1

    def is_prime(self, n):
        if n == 2 or n == 3:
            return True
        # Add a check for even number and numbers less than zero
        if n % 2 == 0 or n < 2:
            return False
        for i in range(3, int(n ** 0.5) + 1, 2):
            if n % i == 0:
                return False
        return True

    def is_palindrome(self, n):
        dev = 1
        while n / dev >= 10:
            dev *= 10
        while n != 0:
            first = n // dev
            last = n % 10

            if first != last:
                return False
            n = (n % dev) // 10
            dev = dev // 100

        return True


if __name__ == '__main__':
    print(Solution().primePalindrome(6))
    print(Solution().is_palindrome(12321))
    print(Solution().is_prime(12321))
