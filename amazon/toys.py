def popularNToys(numToys, topToys, toys,
                 numQuotes, quotes):
    # using hashmap for quick lookup
    toys = {t.lower(): t for t in toys}

    # converting quotes into lists of words
    quotes = [
        [
            word for word in q.split(' ')
            if len(word) > 0
        ]
        for q in quotes
    ]

    # initalizing table where
    # key = toy, value = count of mentioning quotes
    toys_stat = {
        t: 0
        for t in toys
    }

    for quote in quotes:
        # tracking found toy names for each quote
        # using set since the count of mentions within quote is irrelevant
        found = set()
        for word in quote:
            if word in toys:
                found.add(word)

        # copying findings to the final table
        for toy in found:
            toys_stat[toy] += 1

    # sorting by alphabet first
    toys_top = sorted(toys_stat.items(), key=lambda x: x[0])

    # sorting by popularity second, guarantees stable sorting
    toys_top = sorted(toys_top, key=lambda x: x[1], reverse=True)

    # extracting original toy names
    toys_top = [
        toys[t[0]] for t in toys_top
    ]

    # returning top-N only
    return toys_top[:topToys]


print(popularNToys(2, 2, ['b', 'a'], 2, [
    'a is  s!! and b is good!!!!',
    'b,,, is nice but a   is better',
    'b nice and a too'
]))

print(popularNToys(2, 2, ['b', 'a'], 2, [
    "b's a b",
    "b's"
]))

print(popularNToys(2, 2, ['B', 'a'], 2, [
    "b a b",
    "B"
]))