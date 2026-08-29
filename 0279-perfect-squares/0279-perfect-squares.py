class Solution:
    def numSquares(self, n: int) -> int:
        squares = [i*i for i in range(1, int(math.sqrt(n)) + 1)]
        queue = deque([(n, 0)]) 
        visited = set([n])
        
        while queue:
            remainder, steps = queue.popleft()
            if remainder == 0:
                return steps
            for sq in squares:
                nxt = remainder - sq
                if nxt < 0:
                    break
                if nxt not in visited:
                    visited.add(nxt)
                    queue.append((nxt, steps + 1))
