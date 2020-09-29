def make_custom_set(range_data: str):
    start, end = list(map(int, range_data.split(',')))
    custom_set = set(range(start, end+1))

    return custom_set


n_intersections = int(input())
longest_intersection = set()

for _ in range(n_intersections):
    first_range, second_range = input().split('-')

    first_set = make_custom_set(first_range)
    second_set = make_custom_set(second_range)

    local_intersection = first_set & second_set
    if len(local_intersection) > len(longest_intersection):
        longest_intersection = local_intersection

print(f"Longest intersection is {list(longest_intersection)} with length {len(longest_intersection)}")
