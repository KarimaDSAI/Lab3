# src/processing.py
import multiprocessing
import time
from src.functions import sum_numbers

def sum_in_process(start: int, end: int, result_queue: multiprocessing.Queue) -> None:
    """
    sum_in_process function for multiprocessing that calculates a partial sum 
    and puts the result in a queue.

    Args:
        start (int): The start of the range.
        end (int): The end of the range.
        result_queue (multiprocessing.Queue): Queue to store results.
    """
    result_queue.put(sum_numbers(start, end))

def multiprocess_sum(n: int, num_processes: int = 4) -> tuple[int, float]:
    """
    Calculate the sum of numbers from 1 to n using multiple processes.

    Args:
        n (int): The upper limit of the range (starting from 1).
        num_processes (int, optional): The number of processes to use. Defaults to 4.

    Returns:
        tuple[int, float]: The total sum and the execution time in seconds.
    """
    processes = []
    result_queue = multiprocessing.Queue()
    step = n // num_processes

    start_time = time.time()

    for i in range(num_processes):
        start = i * step
        end = (i + 1) * step if i != num_processes - 1 else n + 1
        process = multiprocessing.Process(target=sum_in_process, args=(start, end, result_queue))
        processes.append(process)
        process.start()

    for process in processes:
        process.join()

    total_sum = sum(result_queue.get() for _ in range(num_processes))
    exec_time = time.time() - start_time
    return total_sum, exec_time

