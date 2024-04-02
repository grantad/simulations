import numpy as np

def equal_proportions_method(population, seats):
    """
    Simulates the assignment of electors using the Method of Equal Proportions
    """
    quotas = np.zeros(len(population))
    electors = np.zeros(len(population))
    total_seats = sum(seats)

    for i in range(total_seats):
        quotas = population / (np.sqrt(electors * (electors + 1)))
        max_quota_index = np.argmax(quotas)
        electors[max_quota_index] += 1

    return electors
