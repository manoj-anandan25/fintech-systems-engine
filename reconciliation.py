import pandas as pd

def run_reconciliation():
    # SIMULATED DATA: Internal App Database
    internal_db = pd.DataFrame([
        {"txn_id": "T1", "amount": 100.0, "provider": "STRIPE"},
        {"txn_id": "T2", "amount": 250.0, "provider": "STRIPE"},
        {"txn_id": "T3", "amount": 50.0,  "provider": "PAYPAL"},
        {"txn_id": "T4", "amount": 300.0, "provider": "STRIPE"},
    ])

    # SIMULATED DATA: External Gateway (e.g., Stripe API logs)
    gateway_db = pd.DataFrame([
        {"txn_id": "T1", "amount": 100.0},
        {"txn_id": "T2", "amount": 250.0},
        {"txn_id": "T3", "amount": 50.0},
        {"txn_id": "T4", "amount": 290.0}, # MISMATCH: 300 vs 290
    ])

    print("Checking for Data Consistency...")

    # Perform a LEFT JOIN to find missing or mismatched records
    comparison = pd.merge(internal_db, gateway_db, on="txn_id", how="left", suffixes=('_internal', '_external'))

    # Logic to identify 'Mismatches' (The 99.99% Consistency Check)
    mismatches = comparison[comparison['amount_internal'] != comparison['amount_external']]

    if not mismatches.empty:
        print(f"ALERT: Discrepancy Found in {len(mismatches)} transaction(s)!")
        print(mismatches[['txn_id', 'amount_internal', 'amount_external']])
        
        # Financial Impact Calculation (mentioned on your resume)
        total_mismatch_value = (mismatches['amount_internal'] - mismatches['amount_external']).abs().sum()
        print(f"Total Value to Resolve: ${total_mismatch_value}")
    else:
        print("Data is 100% consistent.")

if __name__ == "__main__":
    run_reconciliation()