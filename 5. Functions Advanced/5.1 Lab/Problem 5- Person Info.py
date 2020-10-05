

def get_info(name: str, age: int, town: str):
    return f"This is {name} from {town} and he is {age} years old"


# print(get_info(**{"name": "George", "town": "Sofia", "age": 20}))
print(get_info(**{"town": "Unknown", "age": "###", "name": "Code#4739"}))
