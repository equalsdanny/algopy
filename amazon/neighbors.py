def cellCompete(states, days):
    current = [0] + states + [0]

    for _ in range(days):
        new = [0] + [
            1 if (current[i - 1] + current[i + 1]) == 1 else 0
            for i in range(1, len(current) - 1)
        ] + [0]

        if current == new:
            break

        current = new

    return current[1:-1]

print(cellCompete([1, 0, 0, 0, 0, 1, 0, 0], 1))