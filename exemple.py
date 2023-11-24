#!/usr/bin/env python

from multiprocessing import Pool
from time import perf_counter

from task import task


def async_callback(resultat: int):
    print(f"callback: {resultat}")


def multi(count: int, size: int):
    start = perf_counter()
    with Pool() as pool:
        results = []
        for _ in range(count):
            result = pool.apply_async(task, [size], callback=async_callback)
            results.append(result)
        for result in results:
            print(result.get())
    end = perf_counter()

    return end - start


if __name__ == "__main__":
    print("total:", multi(6, 5_000))