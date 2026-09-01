class Solution:
    def leastInterval(self, tasks, n):
        freq = Counter(tasks)
        max_freq = max(freq.values())
        max_count = list(freq.values()).count(max_freq)

        return max(len(tasks), (max_freq - 1) * (n + 1) + max_count)
