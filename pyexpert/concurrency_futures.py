"""
Based on examples from the book "Advanced Python Programming", Chapter 7, by Nguyen
"""

from threading import Timer
from concurrent.futures import Future
import asyncio
import nest_asyncio
import time

nest_asyncio.apply()


def on_done(result):
    print(result)


def network_request_timer(number, callback):
    def inner_callback():
        callback(f"{number} to the power of 2 is: {number**2}")

    timer = Timer(1.0, inner_callback)
    timer.start()


def run_timer():
    network_request_timer(2, on_done)
    network_request_timer(3, on_done)
    network_request_timer(4, on_done)
    print("Running timer example")


def network_request_future(number):
    def on_done(future):
        response = future.result()
        if response["success"]:
            print(f"SUCCESS: result is {number}")

    fut = Future()
    fut.add_done_callback(on_done)
    result = {"success": True, "result": number**2}
    timer = Timer(1.0, lambda: fut.set_result(result))
    timer.start()


def run_future():
    network_request_future(2)
    network_request_future(3)
    network_request_future(4)


def wrapper(func):
    def inner_func(number):
        def print_message(number):
            print(f"Generated number {number}")

        return func(number, print_message)

    return inner_func


@wrapper
def simple_generator(n, before_yield):
    i = 0
    while i < n:
        before_yield(i)
        yield i
        i += 1


async def hello_world():
    print("Async hello world!")


def run_asyncio_test_1():
    # hello_world is not executed yet
    coro = hello_world()
    print("After creation of coroutine")
    time.sleep(5)
    loop = asyncio.get_event_loop()
    # here we execute hello_world
    loop.run_until_complete(coro)
