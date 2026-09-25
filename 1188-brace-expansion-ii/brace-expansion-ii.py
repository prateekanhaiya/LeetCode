class Solution:
    def braceExpansionII(self, expression):

        def multiply(a, b):
            result = set()

            for x in a:
                for y in b:
                    result.add(x + y)

            return result

        def parse(i):
            result = set()
            current = {""}

            while i < len(expression) and expression[i] != '}':
                if expression[i] == ',':
                    result |= current
                    current = {""}
                    i += 1

                elif expression[i] == '{':
                    inside, i = parse(i + 1)
                    current = multiply(current, inside)

                else:
                    current = multiply(current, {expression[i]})
                    i += 1

            result |= current

            if i < len(expression) and expression[i] == '}':
                i += 1

            return result, i

        words, _ = parse(0)

        return sorted(words)