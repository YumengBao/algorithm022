from queue import PriorityQueue

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # 记录频次，再对频次用优先级队列（大堆顶）
        freq,res = {},[]
        for n in nums:
            if n not in freq: freq[n] = 1
            else: freq[n]+=1
        maxpq = PriorityQueue()
        for key, val in freq.items():
            maxpq.put((val,key))
            if maxpq.qsize() > k:
                maxpq.get()
        while not maxpq.empty():
            res.append(maxpq.get()[-1])
        return res
