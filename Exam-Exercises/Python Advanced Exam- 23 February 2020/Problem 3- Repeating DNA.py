

def get_repeating_DNA(sequence):
    repeated_sequences = []

    for i in range(len(sequence)-10):
        current_subsequence = sequence[i:i+10]
        the_rest = sequence[i+1:]

        if current_subsequence in the_rest and current_subsequence not in repeated_sequences:
            repeated_sequences.append(current_subsequence)

    return repeated_sequences


test = "AAAAAACCCCAAAAAACCCCTTCAAAATCTTTCAAAATCT"
result = get_repeating_DNA(test)
print(result)

test = "TTCCTTAAGGCCGACTTCCAAGGTTCGATC"
result = get_repeating_DNA(test)
print(result)

test = "AAAAAAAAAAA"
result = get_repeating_DNA(test)
print(result)
