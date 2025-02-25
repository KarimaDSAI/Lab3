import time
from src.functions import sum_numbers
from src.threads import threaded_sum
from src.processing import multiprocess_sum
from src.threads_sync import threaded_sum_with_barrier
from src.threads_futures import threaded_sum_with_future
from src.processing_pool import multiprocess_sum_pool

if __name__ == '__main__':
    n = 10_000_000  # Large number for testing
    num_workers = 6  # Number of threads/processes

    # Sequential Execution
    start_time = time.time()
    seq_sum = sum_numbers(1, n+1)
    seq_time = time.time() - start_time
    print(f"Sequential Sum: {seq_sum}, Time: {seq_time:.4f} sec")

    # Multithreading Execution
    thread_sum, thread_time = threaded_sum(n, num_workers)
    print(f"Threaded Sum: {thread_sum}, Time: {thread_time:.4f} sec")
    
    # # Multiprocessing Execution
    process_sum, process_time = multiprocess_sum(n, num_workers)
    print(f"Multiprocessing Sum: {process_sum}, Time: {process_time:.4f} sec")

    # Multithreading with barrier Execution
    thread_sum, thread_time = threaded_sum_with_barrier(n, num_workers)
    print(f"Threaded Sum with Barrier: {thread_sum}, Time: {thread_time:.4f} sec")

    # Multithreading with barrier Execution
    thread_sum, thread_time = threaded_sum_with_future(n, num_workers)
    print(f"Threaded Sum with futures: {thread_sum}, Time: {thread_time:.4f} sec")

    # # Multiprocessing Execution
    process_sum, process_time = multiprocess_sum_pool(n, num_workers)
    print(f"Multiprocessing Pool Sum: {process_sum}, Time: {process_time:.4f} sec")

