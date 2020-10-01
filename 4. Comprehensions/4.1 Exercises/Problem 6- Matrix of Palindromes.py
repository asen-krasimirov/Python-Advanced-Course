row_c, column_c = map(int, input().split())

alphabet = [chr(x) for x in range(97, 123)]

palindrome_matrix = [
    [
        alphabet[row] + alphabet[column+row] + alphabet[row]
        for column in range(column_c)
    ]
    for row in range(row_c)
]

for row in palindrome_matrix:
    print(' '.join(row))

# Alternative Solution

# row_c, column_c = map(int, input().split())
#
# alphabet = [chr(x) for x in range(97, 123)]
#
# palindrome_matrix = [
#     print(
#         ' '.join([
#             alphabet[row] + alphabet[column+row] + alphabet[row]
#             for column in range(column_c)
#         ])
#     )
#     for row in range(row_c)
# ]
