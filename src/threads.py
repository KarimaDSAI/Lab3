# src/threads.py

import threading
import time
from src.functions import sum_numbers


def sum_in_thread(index: int,
                  start: int,
                  end: int,
                  results: list[int]) -> None:
    """
    sum_in_thread function for calculating partial sums in a thread.

    Args:
        index (int): The index in the results list.
        start (int): The start of the range.
        end (int): The end of the range.
        results (list[int]): Shared list to store partial sums.
    """
    results[index] = sum_numbers(start, end)


def threaded_sum(n: int,
                 num_threads: int = 4) -> tuple[int, float]:
    """
    Calculate the sum of numbers from 1 to n using multiple threads.

    Args:
        n (int): The upper limit of the range (starting from 1).
        num_threads (int, optional): The number of threads to use. Defaults to 4.

    Returns:
        tuple[int, float]: The total sum and the execution time in seconds.
    """
    threads = []
    results = [0] * num_threads
    step = n // num_threads

    start_time = time.time()

    for i in range(num_threads):

        start = i * step
        end = (i + 1) * step if i != num_threads - 1 else n + 1        
        
        thread = threading.Thread(target=sum_in_thread, args=(i, start, end, results))
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()

    total_sum = sum(results)
    exec_time = time.time() - start_time
    return total_sum, exec_time
