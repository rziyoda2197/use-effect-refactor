import asyncio
import time

async def get_data():
    # Simulate API call
    await asyncio.sleep(1)
    return "Data received"

async def main():
    start_time = time.time()
    data = await get_data()
    end_time = time.time()
    print(f"Data received in {end_time - start_time} seconds")

async def refactored_use_effect():
    start_time = time.time()
    await get_data()
    end_time = time.time()
    print(f"Data received in {end_time - start_time} seconds")

async def main_refactored():
    await refactored_use_effect()

asyncio.run(main_refactored())
