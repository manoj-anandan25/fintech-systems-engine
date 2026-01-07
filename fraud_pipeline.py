import asyncio
import random
import time
import pandas as pd

# =================================================================
# REAL-TIME FRAUD DETECTION PIPELINE (AWS Kinesis + SageMaker Sim)
# =================================================================

class FraudDetectionPipeline:
    def __init__(self):
        # Simulated "SageMaker" Model Weights
        self.threshold = 0.8
        self.processed_count = 0

    async def mock_sagemaker_predict(self, payload):
        """Simulates a SageMaker Endpoint invocation (<50ms latency)"""
        await asyncio.sleep(0.04)  # Simulate network hop to model
        
        # Logic: High amount + specific 'suspicious' flags = High Fraud Score
        score = random.uniform(0, 0.5)
        if payload['amount'] > 900 or payload['ip_region'] == 'Unknown':
            score += 0.45
            
        return score

    async def process_stream_record(self, record):
        """Simulates a Kinesis Consumer processing a single log record"""
        start_time = time.perf_counter()
        
        # 1. Ingest & Feature Extraction
        txn_id = record['txn_id']
        
        # 2. Call ML Model for Prediction
        fraud_score = await self.mock_sagemaker_predict(record)
        
        # 3. Decision Logic
        is_fraud = fraud_score > self.threshold
        
        latency_ms = (time.perf_counter() - start_time) * 1000
        
        if is_fraud:
            print(f"⚠️ [ALERT] Fraud Detected! ID: {txn_id} | Score: {fraud_score:.2f} | Latency: {latency_ms:.2f}ms")
        
        return is_fraud

async def run_pipeline_demo():
    pipeline = FraudDetectionPipeline()
    
    # Simulated Stream of User Logs (Kinesis Shard)
    user_logs = [
        {"txn_id": "TXN_A1", "amount": 100, "ip_region": "US"},
        {"txn_id": "TXN_B2", "amount": 950, "ip_region": "Unknown"}, # Suspicious
        {"txn_id": "TXN_C3", "amount": 50,  "ip_region": "UK"},
        {"txn_id": "TXN_D4", "amount": 1200, "ip_region": "US"}, # Suspicious
    ]

    print(f"--- Starting Real-Time Fraud Pipeline (<200ms Target) ---")
    start_pipeline = time.perf_counter()

    # Process logs concurrently (as they arrive in the stream)
    tasks = [pipeline.process_stream_record(log) for log in user_logs]
    results = await asyncio.gather(*tasks)

    total_duration = (time.perf_counter() - start_pipeline) * 1000
    print(f"\n--- Pipeline Summary ---")
    print(f"Total Logs Processed: {len(results)}")
    print(f"Average Latency: {total_duration/len(results):.2f}ms")

if __name__ == "__main__":
    asyncio.run(run_pipeline_demo())# Note: if running this specific block, call run_pipeline_demo()
    # Corrected call for the standalone script:
    # asyncio.run(run_pipeline_demo())