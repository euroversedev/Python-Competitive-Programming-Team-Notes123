import heapq

''' [ Heap DataStructure ]
- `=. Priority Queue(우선순위 큐)는 힙 자료구조를 가지고 구현한다.

- 힙은 최대, 최소 값을 빠르게 찾아내기 위해 고안되었으며 완전 이진 트리 형태를 띈다.
- 파이썬에서는 heapq 모듈을 이용해 최소힙을 구현할 수 있다.
- 시간 복잡도는 O(logN)이며, 다익스트라 최단 경로 알고리즘 등에서 탐색 속도 개선을 위해 사용된다.
'''
# 힙 생성
h = []

# 데이터 삽입
heapq.heappush(h, 13)    # [13]
heapq.heappush(h, 10)    # [10, 13]

# 데이터 삭제
data = heapq.heappop(h)
print(data)              # 10

# 기존 리스트를 힙으로 변환 (내부 로직으로 인해 순차적으로 출력X)
array = [14, 10, 5, 7, 12, 4]
heapq.heapify(array)
print(array)             # [4, 7, 5, 10, 12, 14]


# 최대, 최소 메소드 (이중 우선순위 큐에 이용됨)
# heapq.nlargest(n, iterable[, key=None])
big_2 = heapq.nlargest(2, array)    # [14, 12]
small_3 = heapq.nsmallest(3, array)    # [4, 5, 7]
print(big_2, small_3)

''' [ Heap Sort ]
- heapq는 최소힙을 지원하며, 최대힙은 데이터의 부호를 바꿔 구현함.
'''
def heap_sort(iterable):
    h = []
    result = []
    
    # 모든 원소를 힙에 삽입
    for value in iterable:
        heapq.heappush(h, value)
    
    # 힙에서 리스트로 이동
    for i in range(len(h)):
        result.append(heapq.heappop(h))
    
    return result

result = heap_sort([1, 3, 5, 7, 9, 2, 4, 6, 8, 0])
print(result)

''' [ 최대, 절댓값 힙 ]
원소 삽입 시에 (-x, x) 혹은 (abs(x), x)를 삽입한다.
정렬 기준이 첫째 원소, 둘째 원소 순서로 적용 된다.
'''

