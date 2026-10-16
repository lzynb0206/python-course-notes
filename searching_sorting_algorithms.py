"""Searching and sorting algorithms for Experiment 3.

Python lists use indexes starting at 0, so the last valid index is
len(data) - 1.
"""

import random
import time


# Name: Lu Zhengyang；UoR ID: 33803834；NUIST ID: 202483710010
# Linear Search
def linear_search(datum, data):
    index = -1
    found = False

    for i in range(len(data)):
        d = data[i]
        if d == datum:
            index = i
            found = True
            return index, found

    return index, found


# Name: Lu Zhengyang；NUIST ID: 202483710010；UoR ID: 33803834
# Binary Search - Iterative version
def binary_search(target, array):
    first = 0
    last = len(array) - 1

    while first <= last:
        middle = (first + last) // 2

        if array[middle] == target:
            return middle, True
        elif array[middle] > target:
            last = middle - 1
        else:
            first = middle + 1

    return -1, False


# Binary Search - Recursive version
def binary_search_recursive(target, array, first, last):
    if first <= last:
        middle = (first + last) // 2

        if array[middle] == target:
            return middle, True
        if array[middle] > target:
            return binary_search_recursive(
                target, array, first, middle - 1
            )
        if array[middle] < target:
            return binary_search_recursive(
                target, array, middle + 1, last
            )

    return -1, False


# Name: Lu Zhengyang；UoR ID: 33803834；NUIST ID: 202483710010
# Random Data and Average Timing
def generate_task1_data(size, rng):
    """Create random data and 100 targets, half present and half absent."""
    data = rng.sample(range(size * 20), size)
    sorted_data = sorted(data)

    present = [rng.choice(data) for _ in range(50)]
    absent = [size * 20 + i for i in range(50)]
    targets = present + absent
    rng.shuffle(targets)
    return data, sorted_data, targets


def average_search_time(search_function, targets):
    """Return average search time in microseconds."""
    start = time.perf_counter_ns()
    for target in targets:
        search_function(target)
    elapsed = time.perf_counter_ns() - start
    return elapsed / len(targets) / 1000


# Name: Lu Zhengyang；UoR ID: 33803834；NUIST ID: 202483710010
# Experiment Driver and Required Output Format
def run_task1_experiment():
    """Compare linear and binary search for the four required sizes."""
    rng = random.Random()
    sizes = [10, 100, 1000, 10000]

    for size in sizes:
        data, sorted_data, targets = generate_task1_data(size, rng)

        linear_us = average_search_time(
            lambda target: linear_search(target, data), targets
        )
        iterative_us = average_search_time(
            lambda target: binary_search(target, sorted_data), targets
        )
        recursive_us = average_search_time(
            lambda target: binary_search_recursive(
                target, sorted_data, 0, len(sorted_data) - 1
            ),
            targets,
        )

        print(
            f"Algorithm: {'Linear Search,':<26} n: {size:>5}, "
            f"Time: {linear_us:>12.6f}"
        )
        print(
            f"Algorithm: {'Binary Search (iterative),':<26} n: {size:>5}, "
            f"Time: {iterative_us:>12.6f}"
        )
        print(
            f"Algorithm: {'Binary Search (recursive),':<26} n: {size:>5}, "
            f"Time: {recursive_us:>12.6f}"
        )
        print()


# Name: Lu Zhengyang；UoR ID: 33803834；NUIST ID: 202483710010
# Insertion Sort
def insertion_sort(data):
    for i in range(1, len(data)):
        m = data[i]
        j = i - 1

        while j >= 0 and data[j] > m:
            data[j + 1] = data[j]
            j = j - 1

        data[j + 1] = m

    return data

# Name: Lu Zhengyang；UoR ID: 33803834；NUIST ID: 202483710010
# Bubble Sort
def bubble_sort(data):
    for i in range(len(data) - 1):
        for j in range(len(data) - 1, i, -1):
            if data[j - 1] > data[j]:
                swap(data, j - 1, j)

    return data

# Name: Lu Zhengyang；UoR ID: 33803834；NUIST ID: 202483710010
# Merge Sort
def merge_sort(data):
    if len(data) > 1:
        middle = len(data) // 2
        left = data[:middle]
        right = data[middle:]

        merge_sort(left)
        merge_sort(right)

        i = 0
        j = 0
        k = 0

        while i < len(left) and j < len(right):
            if left[i] <= right[j]:
                data[k] = left[i]
                i = i + 1
            else:
                data[k] = right[j]
                j = j + 1
            k = k + 1

        while i < len(left):
            data[k] = left[i]
            i = i + 1
            k = k + 1

        while j < len(right):
            data[k] = right[j]
            j = j + 1
            k = k + 1

    return data

# Name: Lu Zhengyang；UoR ID: 33803834；NUIST ID: 202483710010
# Quick Sort
def quick_sort(data):
    quick_sort_recursive(data, 0, len(data) - 1)
    return data

def quick_sort_recursive(data, low, high):
    if low < high:
        pivot_index = partition(data, low, high)
        quick_sort_recursive(data, low, pivot_index - 1)
        quick_sort_recursive(data, pivot_index, high)

def partition(data, left, right):
    pivot = data[(left + right) // 2]
    i = left
    j = right

    while i <= j:
        while data[i] < pivot:
            i = i + 1

        while data[j] > pivot:
            j = j - 1

        if i <= j:
            swap(data, i, j)
            i = i + 1
            j = j - 1

    return i


# swap two elements.
def swap(data, first, second):
    temp = data[first]
    data[first] = data[second]
    data[second] = temp


# Name: Lu Zhengyang; UoR ID: 33803834; NUIST ID: 202483710010
# Task 2 Random Data and Average Timing
def average_sort_time(sort_function, test_arrays):
    """Return the average sorting time in milliseconds."""
    elapsed_times = []

    for original in test_arrays:
        data = original.copy()
        start = time.perf_counter_ns()
        sort_function(data)
        elapsed = time.perf_counter_ns() - start

        if data != sorted(original):
            raise ValueError(f"{sort_function.__name__} produced an incorrect result")

        elapsed_times.append(elapsed / 1_000_000)

    return sum(elapsed_times) / len(elapsed_times)


# Name: Lu Zhengyang; UoR ID: 33803834; NUIST ID: 202483710010
# Task 2 Experiment Driver and Required Output Format
def run_task2_experiment():
    """Measure four sorting algorithms for the required array sizes."""
    rng = random.Random()
    sizes = [10, 100, 1000, 10000]
    trials = 5
    algorithms = [
        ("Insertion Sort", insertion_sort),
        ("Bubble Sort", bubble_sort),
        ("Merge Sort", merge_sort),
        ("Quick Sort", quick_sort),
    ]

    for size in sizes:
        test_arrays = [
            [rng.randrange(size * 20) for _ in range(size)]
            for _ in range(trials)
        ]

        for name, sort_function in algorithms:
            average_ms = average_sort_time(sort_function, test_arrays)
            print(
                f"Algorithm: {(name + ','):<26} n: {size:>5}, "
                f"Time: {average_ms:>12.6f}"
            )

        sorted_arrays = [list(range(size)) for _ in range(trials)]
        sorted_ms = average_sort_time(quick_sort, sorted_arrays)
        print(
            f"Algorithm: {'Quick Sort (sorted input),':<26} n: {size:>5}, "
            f"Time: {sorted_ms:>12.6f}"
        )
        print()


if __name__ == "__main__":
    print("Task 1: Searching Algorithms")
    run_task1_experiment()
    print("Task 2: Sorting Algorithms")
    run_task2_experiment()
