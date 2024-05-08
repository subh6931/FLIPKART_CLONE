def count_return_to_start(N, moves):
    count = 0
    position = 0
    for move in moves:
        position += move
        if position % N == 0:
            count += 1
    return count

# Example usage:
N = 5
moves = [1, -1, -1, 1, 1]
print(count_return_to_start(N, moves))  # Output: 1