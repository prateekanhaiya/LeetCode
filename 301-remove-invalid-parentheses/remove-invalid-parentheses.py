class Solution:
    def removeInvalidParentheses(self, s):
        def is_valid(string):
            balance = 0

            for ch in string:
                if ch == '(':
                    balance += 1
                elif ch == ')':
                    balance -= 1
                    if balance < 0:
                        return False

            return balance == 0

        queue = [s]
        visited = set([s])
        answer = []

        while queue:
            found = False
            next_level = []

            for current in queue:
                if is_valid(current):
                    answer.append(current)
                    found = True

            if found:
                return answer

            for current in queue:
                for i in range(len(current)):
                    if current[i] != '(' and current[i] != ')':
                        continue

                    new_string = current[:i] + current[i + 1:]

                    if new_string not in visited:
                        visited.add(new_string)
                        next_level.append(new_string)

            queue = next_level

        return answer
        