import heapq

class Solution:
    def assignTasks(self, servers: list[int], tasks: list[int]) -> list[int]:

        available = [(weight, i) for i, weight in enumerate(servers)]
        heapq.heapify(available)

        busy = []
        ans = []
        current_time = 0

        for i, task in enumerate(tasks):

            current_time = max(current_time, i)

            # Release all servers that have finished
            while busy and busy[0][0] <= current_time:
                finish, weight, index = heapq.heappop(busy)
                heapq.heappush(available, (weight, index))

            # If no server is free, move time forward
            if not available:
                current_time = busy[0][0]

                while busy and busy[0][0] <= current_time:
                    finish, weight, index = heapq.heappop(busy)
                    heapq.heappush(available, (weight, index))

            # Select the best available server
            weight, index = heapq.heappop(available)

            ans.append(index)

            # Mark server as busy
            heapq.heappush(
                busy,
                (current_time + task, weight, index)
            )

        return ans