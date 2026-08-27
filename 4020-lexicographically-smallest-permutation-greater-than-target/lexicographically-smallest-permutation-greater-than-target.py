from collections import Counter

class Solution:
    def lexGreaterPermutation(self, s, target):
        count = Counter(s)
        answer = ""

        for i in range(len(target)):
            # Try to make this position bigger
            for ch in sorted(count):
                if ch > target[i] and count[ch] > 0:
                    count[ch] -= 1

                    temp = target[:i] + ch

                    for c in sorted(count):
                        temp += c * count[c]

                    answer = temp
                    count[ch] += 1
                    break

            # Use target[i] if possible
            if count[target[i]] > 0:
                count[target[i]] -= 1
            else:
                break

        return answer