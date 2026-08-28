class Solution:
    def lexPalindromicPermutation(self, s, target):

        n = len(s)
        half = n // 2

        # Count characters in s
        count = [0] * 26

        for ch in s:
            count[ord(ch) - ord('a')] += 1

        # Check if palindrome is possible
        odd = 0
        middle = ""

        for i in range(26):
            if count[i] % 2 == 1:
                odd += 1
                middle = chr(97 + i)

        if odd > 1:
            return ""

        # Number of each character available in the LEFT half
        pairs = [x // 2 for x in count]

        # Try to make target's left half
        for i in range(half):
            x = ord(target[i]) - 97
            pairs[x] -= 1

        # Case 1:
        # The left half can be exactly target's left half
        if min(pairs) >= 0:

            left = target[:half]

            answer = left + middle + left[::-1]

            # Must be STRICTLY greater
            if answer > target:
                return answer

        # Case 2:
        # Go backwards and make one character bigger
        for i in range(half - 1, -1, -1):

            x = ord(target[i]) - 97

            # Give target[i] back
            pairs[x] += 1

            # If target[:i] cannot be formed, skip
            if min(pairs) < 0:
                continue

            # Try the smallest character bigger than target[i]
            for c in range(x + 1, 26):

                if pairs[c] > 0:

                    pairs[c] -= 1

                    # Prefix remains same as target
                    left = target[:i] + chr(97 + c)

                    # Put remaining characters in smallest order
                    for j in range(26):
                        left += chr(97 + j) * pairs[j]

                    # Make palindrome
                    answer = left + middle + left[::-1]

                    return answer

        return ""