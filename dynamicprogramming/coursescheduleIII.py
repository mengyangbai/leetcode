import heapq

class Solution:
    def scheduleCourse(self, courses: 'List[List[int]]') -> 'int':
        max_heap = []
        courses.sort(key=lambda course: course[1])
        
        cur = 0
        for t,d in courses:
            if cur + t <= d:
                heapq.heappush(max_heap, -t)
                cur += t
            elif max_heap and t < -max_heap[0]:
                cur -= -heapq.heappop(max_heap)
                heapq.heappush(max_heap, -t)
                cur += t
        return len(max_heap)