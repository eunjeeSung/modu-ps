# Sol1: python sort
# Time: O(NlogN) / Space: O(N)
class Solution:
    def kClosest(self, points: List[List[int]], K: int) -> List[List[int]]:
        points.sort(key=lambda x: sqrt(x[0]**2 + x[1]**2))
        return points[:K]
    
    
# Sol2: divide and conquer
# Solution from leetcode.com
# class Solution:
#     def kClosest(self, points: List[List[int]], K: int) -> List[List[int]]:
#         dist = lambda i: points[i][0]**2 + points[i][1]**2
        
#         def sort(i, j, K):
#             if i >= j: return
            
#             k = random.randint(i, j) # pick random element
#             points[i], points[k] = points[k], points[i] # swap
            
#             mid = partition(i, j)
#             if K < (mid - i + 1):
#                 sort(i, mid - 1, K)
#             elif K > (mid - i + 1):
#                 sort(mid + 1, j, K - (mid - i + 1))
                
#         def partition(i, j):
#             oi = i
#             pivot = dist(i)
#             i += 1
            
#             while True:
#                 while i < j and dist(i) < pivot:
#                     i += 1
#                 while i <= j and dist(j) >= pivot:
#                     j -= 1
#                 if i >= j: break
#                 points[i], points[j] = points[j], points[i]
            
#             points[oi], points[j] = points[j], points[oi]
#             return j
            
#         sort(0, len(points) - 1, K)
#         return points[:K]
            
    
# Sol3: priority heap
# from https://leetcode.com/problems/k-closest-points-to-origin/discuss/294389/Easy-to-read-Python-min-heap-solution-(-beat-99-python-solutions-)
# class Solution:
#     def kClosest(self, points: List[List[int]], K: int) -> List[List[int]]:
#         heap = []
#         for point in points:
#             dist = -(point[0]**2 + point[1]**2)
#             if len(heap) == K:
#                 heapq.heappushpop(heap, (dist, point))
#             else:
#                 heapq.heappush(heap, (dist, point))
                
#         return [point for (dist, point) in heap]
            