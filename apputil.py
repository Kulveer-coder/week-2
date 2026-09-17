import numpy as np


# update/add code below ...

def ways(n):
    # Start counting the number of possible ways.
    count = 0

    # Try every possible number of nickels.
    for nickels in range(n // 5 + 1):
        # Each possible number of nickels gives one combination.
        count += 1

    # Return the total number of combinations.
    return count


def lowest_score(names, scores):
    # Find the position of the lowest score.
    lowest_index = np.argmin(scores)

    # Return the name at that position.
    return names[lowest_index]


def sort_names(names, scores):
    # Get the positions of scores from highest to lowest.
    sorted_indices = np.argsort(scores)[::-1]

    # Return the names in descending order of their scores.
    return [names[i] for i in sorted_indices]