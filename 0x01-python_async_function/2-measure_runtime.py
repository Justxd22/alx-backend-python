#!/usr/bin/env python3
"""Wait for a random delay between 0 and max_delay."""


from asyncio import run
from time import time

wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> float:
    """Wait for a random delay between 0 and max_delay mesure time."""
    start = time()

    run(wait_n(n, max_delay))

    end = time()

    return (end - start) / n
