#!/usr/bin/env python3
"""Async Mesure."""


import asyncio
import time

async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """Async Mesure."""
    s = time.time()
    await asyncio.gather(*[async_comprehension() for i in range(4)])
    e = time.time()
    return e - s
