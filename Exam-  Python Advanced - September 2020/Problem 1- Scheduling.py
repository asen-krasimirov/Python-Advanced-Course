

def find_shortest_index(array):
    cur_shortest = 1000
    cur_shortest_index = 0
    for i in range(len(array)):
        if array[i] is not None:
            if array[i] < cur_shortest:
                cur_shortest = array[i]
                cur_shortest_index = i
    return cur_shortest_index


jobs = [int(n) for n in input().split(", ")]
needed_index = int(input())

passed_cycles = 0

while True:
    shortest_index = find_shortest_index(jobs)
    passed_cycles += jobs[shortest_index]
    jobs[shortest_index] = None
    if shortest_index == needed_index:
        break


print(passed_cycles)
