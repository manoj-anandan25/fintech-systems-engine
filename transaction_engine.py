import asyncio
import time
import random

# Simulating a high-performance Cache (Dictionary)
account_cache = {
    "ACC_001": {"balance": 1000.0, "status": "ACTIVE"},
    "ACC_002": {"balance": 500.0, "status": "ACTIVE"}
}

async def process_transaction(txn_id):
    """
    Simulates a non-blocking transaction.
    Instead of waiting for a DB, it uses 'await' to let other 
    tasks run in the background.
    """
    # 1. Fast Cache Lookup
    acc_id = "ACC_001"
    account = account_cache.get(acc_id)

    # 2. In-memory Validation (Very Fast)
    if account["balance"] < 10.0:
        return f"Txn {txn_id}: Failed"

    # 3. Simulated Asynchronous DB/Network Write
    # In a real app, this would be a call to DynamoDB or a Kafka Queue
    await asyncio.sleep(0.01) # Simulate 10ms network latency
    
    return f"Txn {txn_id}: Success"

async def main():
    print(f"Starting High-Scale Engine Simulation...")
    start_time = time.perf_counter()

    # Simulate 10,000 requests sent almost simultaneously
    tasks = [process_transaction(i) for i in range(10000)]
    
    # Run all tasks concurrently
    results = await asyncio.gather(*tasks)

    end_time = time.perf_counter()
    duration = end_time - start_time

    print("-----------------------------------")
    print(f"Total Transactions Processed: {len(results)}")
    print(f"Time Taken: {duration:.2f} seconds")
    print(f"Simulated TPS: {int(len(results) / duration)}")

if __name__ == "__main__":
    asyncio.run(main())