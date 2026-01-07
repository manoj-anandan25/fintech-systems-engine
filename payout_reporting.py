import time
import random
import pandas as pd
import logging
from functools import wraps

# Setup Logging to simulate "Operational Excellence"
logging.basicConfig(level=logging.INFO, format='%(message)s')

# =================================================================
# 1. SYSTEM RELIABILITY: Reusable Retry & Backoff Library
# =================================================================
def retry_with_backoff(max_retries=3, initial_delay=1):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            retries, delay = 0, initial_delay
            while retries < max_retries:
                try:
                    return func(*args, **kwargs)
                except Exception as e:
                    retries += 1
                    if retries == max_retries:
                        logging.error(f"FATAL: {func.__name__} failed after {max_retries} tries.")
                        raise e
                    logging.warning(f"RETRYING: {func.__name__} failed. Attempt {retries} in {delay}s...")
                    time.sleep(delay)
                    delay *= 2 # Exponential backoff
            return None
        return wrapper
    return decorator

# =================================================================
# 2. SEARCH & INDEXING: Mock Reporting Engine (Elasticsearch Sim)
# =================================================================
class ReportingEngine:
    def __init__(self):
        # Simulated DynamoDB (Primary) and Elasticsearch (Index)
        self.data_store = []

    def index_transaction(self, txn):
        """Simulates indexing for real-time reporting for 1M+ users"""
        self.data_store.append(txn)

    def search_merchant_payouts(self, merchant_id):
        """Simulates a complex Elasticsearch 'Match' Query for PM Reporting"""
        df = pd.DataFrame(self.data_store)
        if df.empty: return "No Data"
        # Logic: Filter by merchant and show 'Instant Payouts'
        results = df[df['merchant_id'] == merchant_id]
        return results

# =================================================================
# 3. PRODUCT FEATURE: Instant Payout System
# =================================================================
class PayoutService:
    def __init__(self, reporter):
        self.reporter = reporter

    @retry_with_backoff(max_retries=3)
    def call_banking_api(self, amount):
        """Simulates a bank API that is occasionally unstable"""
        if random.random() < 0.5: # 50% chance of transient failure
            raise ConnectionError("Bank API Timeout")
        return "PAID_SUCCESS"

    def trigger_instant_payout(self, m_id, amount):
        logging.info(f"--- Processing Instant Payout for {m_id} ---")
        try:
            status = self.call_banking_api(amount)
            # Once paid, index it for real-time reporting
            self.reporter.index_transaction({
                "merchant_id": m_id,
                "amount": amount,
                "type": "INSTANT",
                "timestamp": time.time()
            })
            logging.info("SUCCESS: Payout completed and indexed.")
        except:
            logging.error("FAILED: Could not complete payout.")

# =================================================================
# EXECUTION
# =================================================================
if __name__ == "__main__":
    report_engine = ReportingEngine()
    payout_system = PayoutService(report_engine)

    # 1. Simulate the "Instant Payout" feature (Product Collaboration)
    payout_system.trigger_instant_payout("MERCHANT_XYZ", 1500.0)

    # 2. Simulate Search & Indexing (Elasticsearch Logic)
    print("\n--- GENERATING PM REPORT (Real-time Indexing) ---")
    report = report_engine.search_merchant_payouts("MERCHANT_XYZ")
    print(report)