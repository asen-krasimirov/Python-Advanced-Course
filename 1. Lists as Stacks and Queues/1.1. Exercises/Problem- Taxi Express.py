from collections import deque


customers = deque(list(map(int, input().split(", "))))
drive = input().split(", ")
drivers = deque(list(map(int, drive[::-1])))

total_time = 0

while customers and drivers:
    customer = customers.popleft()
    driver = drivers.popleft()

    if driver >= customer:
        total_time += customer
    else:
        customers.appendleft(customer)

if not customers:
    print("All customers were driven to their destinations")
    print(f"Total time: {total_time} minutes")
elif not drivers:
    customers = list(map(str, customers))
    print("Not all customers were driven to their destinations")
    print(f"Customers left: {', '.join(customers)}")
