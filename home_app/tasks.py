# tasks.py
from celery import shared_task
import os, time

@shared_task
def mock_heavy_task(size_in_gb=3):
    chunk_size = 1024 * 1024 * 100  # 100 MB
    iterations = (size_in_gb * 1024) // 100
    data_holder = []

    for _ in range(iterations):
        data_holder.append(os.urandom(chunk_size))  # allocate and hold random bytes
        time.sleep(0.05)            # simulate processing delay

    # sleep to simulate holding memory for a while after allocation
    time.sleep(10)
    
    return f"Simulated {size_in_gb}GB load"