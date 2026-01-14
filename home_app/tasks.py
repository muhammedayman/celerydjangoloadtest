# tasks.py
from celery import shared_task
import os, time

@shared_task
def mock_heavy_task(size_in_gb=3):
    chunk_size = 1024 * 1024 * 100  # 100 MB
    iterations = (size_in_gb * 1024) // 100
    data_holder = []

    for _ in range(iterations):
        # Create a 100MB byte chunk (fast allocation, low CPU)
        data_holder.append(b'0' * chunk_size)
        time.sleep(0.1)            # small delay to prevent freezing

    # sleep to simulate holding memory for a longer duration
    time.sleep(60)
    
    return f"Simulated {size_in_gb}GB load"