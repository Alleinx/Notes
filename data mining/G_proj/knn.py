import numpy as np


def knn(training_set, test_set, k=3):
    train_data = np.copy(training_set)
    test_data = np.copy(test_set)

    result = []

    for data in test_data:
        distance = []
        for i in train_data:
            distance.append(
                (_distance(i[: -1], data[: -1]),
                 i[-1])
            )

        distance.sort(key=lambda x: x[0])

        count_zero = len([i[-1] for i in distance[:k] if i[-1] == 0])
        label = 0 if count_zero >= (k - count_zero) else 1

        result.append(label)

    return result


def _distance(train_data, test_data):
    '''
    calculate distance between two points
    '''
    total = len(train_data)
    distance = 0.0

    for i in range(total):
        distance += (train_data[i] - test_data[i]) ** 2

    return np.sqrt(distance)
