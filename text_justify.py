import math
import random

target_width = 80
text = 'Machine learning (ML) is the scientific study of algorithms and statistical models that computer systems use to perform a specific task without using explicit instructions, relying on patterns and inference instead. It is seen as a subset of artificial intelligence. Machine learning algorithms build a mathematical model based on sample data, known as "training data", in order to make predictions or decisions without being explicitly programmed to perform the task.[1][2]:2 Machine learning algorithms are used in a wide variety of applications, such as email filtering and computer vision, where it is difficult or infeasible to develop a conventional algorithm for effectively performing the task. Machine learning is closely related to computational statistics, which focuses on making predictions using computers. The study of mathematical optimization delivers methods, theory and application domains to the field of machine learning. Data mining is a field of study within machine learning, and focuses on exploratory data analysis through unsupervised learning.[3][4] In its application across business problems, machine learning is also referred to as predictive analytics.'

# target_width = 4
# text = '0qwe abc zzy dbe'


def cost(target_width, line_width):
    if line_width > target_width:
        return float('inf')

    return (target_width - line_width)**3


def text_to_justified_lines(text, target_width):
    text = text.split(' ')
    best_cost, best_split = search_best_splits(text, target_width, 0, {})

    return [
        text[start:end]
        for start, end in zip([0] + best_split, best_split + [len(text)])
    ]


def search_best_splits(text, target_width, start, cache):
    if start in cache:
        return cache[start]

    min_cost = None
    min_split = []
    line_length = 0

    for i in range(start, len(text)):
        line_length += len(text[i]) + 1

        if line_length > target_width:
            break

        if i+1 < len(text):
            best_cost, best_split = search_best_splits(text, target_width, i + 1, cache)
            best_cost += cost(target_width, line_length)
            best_split = [i+1] + best_split
        else:
            best_cost = cost(target_width, line_length)
            best_split = []

        if min_cost is None or best_cost < min_cost:
            min_cost = best_cost
            min_split = best_split

    cache[start] = (min_cost, min_split)

    return min_cost, min_split


def monospaced_line(group, target_width):
    output = ''

    characters = sum(map(len, group))
    extra_spaces = target_width - characters

    breaks = len(group) - 1
    per_word = extra_spaces / breaks
    base_per_word = math.floor(per_word)

    random_spaces = extra_spaces - base_per_word*breaks
    random_per_word = per_word - base_per_word

    for i, word in enumerate(group):
        if i+1 == len(group):
            output += ' ' * random_spaces
            random_spaces = 0

        output += group[i]

        if i+1 == len(group):
            break

        output += ' ' * base_per_word

        if random_spaces > 0 and random.uniform(0, 1) < random_per_word:
            output += ' '
            random_spaces -= 1

    return output



for line in text_to_justified_lines(text, target_width):
    print(monospaced_line(line, target_width))

