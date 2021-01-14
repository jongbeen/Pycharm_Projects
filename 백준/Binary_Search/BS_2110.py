import sys
sys.stdin = open('input_2110.txt','r')
def find(array):
    # 최소간격과 최대간격을 찾음
    MAX, MIN = array[-1] - array[0], array[-1]
    for i in range(1, len(array)):
        MIN = min(array[i]- array[i-1], MIN)
    return MIN, MAX
N, C = map(int, input().split())
location = []
for _ in range(N):
    location.append(int(input()))
location.sort()
start, end = find(location)
result = 0
while start <= end:
    mid = (start + end) // 2
    spot, count = location[0], 1
    for i in range(1, len(location)):
        if location[i] >= spot + mid:
            spot = location[i]
            count += 1
    if count >= C:
        start = mid + 1
        result = mid
    else:
        end = mid -1
print(result)