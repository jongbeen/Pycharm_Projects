from collections import deque
from copy import deepcopy

def solution(tickets):
    queue = deque([])
    result = []
    for t in tickets:
        if t[0] == "ICN":
            queue.append((t,[t],1,t))

    while queue:
        route, visited, cnt, travel = queue.popleft()
        print(route[0], visited)
        if cnt == len(tickets):
            result.append(travel)
        start, dest = route[0], route[1]

        for t in tickets:
            visit = deepcopy(visited)
            if t not in visit:
                if t[0] == dest:
                    visit.append(t)
                    travel.append(t[1])
                    queue.append((t,visit,cnt+1,travel))
    return result

# print(solution([["ICN", "JFK"], ["HND", "IAD"], ["JFK", "HND"]]))
t = [["ICN", "SFO"], ["ICN", "ATL"], ["SFO", "ATL"], ["ATL", "ICN"], ["ATL","SFO"]]
print(solution(t))