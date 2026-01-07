# FinTech High-Scale Systems Engine

A collection of high-performance backend modules demonstrating **Concurrency**, **Data Reliability**, and **Low-Latency Pipelines**. This repository implements core FinTech patterns inspired by industry simulations and is optimized for high-scale "Data Plane" and "Control Plane" performance.

##  Background & Pedigree
The core architectural patterns in this repository—specifically the Transaction Engine and Reconciliation logic—were adapted and re-engineered from the **J.P. Morgan Software Engineering Virtual Experience**. While the original industry simulation was Java-based, I re-architected the logic in **Python** to explore high-concurrency performance using `asyncio` and vectorized data processing with `pandas`.

##  Key Projects & Impact

### 1. High-Throughput Transaction Engine (`transaction_engine.py`)
* **Performance:** Achieves simulated **50k+ TPS** using Python's `asyncio` for non-blocking I/O.
* **Optimization:** Utilizes an in-memory `account_cache` to bypass DB latency for initial validations, simulating a high-performance "Data Plane" optimization.

### 2. Real-Time Fraud Detection Pipeline (`fraud_pipeline.py`)
* **Architecture:** Simulates a Kinesis stream consumer calling a SageMaker ML endpoint with <50ms simulated latency.
* **Latency:** Optimized for **<200ms end-to-end latency** for real-time decisioning on high-value transactions.

### 3. Financial Reconciliation Service (`reconciliation.py`)
* **Business Logic:** Ensures data consistency between internal ledgers and external gateways using Pandas for vectorized comparisons.
* **Impact:** Automatically identifies discrepancies (e.g., mismatching transaction amounts) and calculates the total financial risk.

### 4. Reliable Payout System (`payout_reporting.py`)
* **Operational Excellence:** Implemented custom `@retry_with_backoff` decorators with exponential backoff to handle transient Banking API failures.
* **Indexing:** Features a reporting engine mock simulating real-time Elasticsearch indexing for merchant payout transparency.

##  Tech Stack
* **Language:** Python 3.10+
* **Concurrency:** `asyncio` for non-blocking task management.
* **Data Analysis:** `pandas` for high-speed reconciliation and reporting.
* **Testing:** `unittest` for core business logic validation.

##  Systems Engineering Focus
Based on my technical projects in **CUDA Kernel Optimization** and **FX Graph Compiler Passes**, this repository serves as the "Control Plane" logic. It focuses on how data flows efficiently through a system before it hits low-level hardware optimizations.

---

##  Installation & Testing

1. **Install Dependencies:**
   ```bash
   pip install -r requirements.txt

```
```

2. **Run All Tests (CI-Ready):**
```bash
    python -m unittest tests/test_logic.py

```


3. **Execute 10k Transaction Simulation:**
```bash
python src/engines/transaction_engine.py

```


4. **Run Fraud Detection Stream:**
```bash
python src/services/fraud_pipeline.py

```




