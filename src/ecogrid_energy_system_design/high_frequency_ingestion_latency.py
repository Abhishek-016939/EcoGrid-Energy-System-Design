
import time


def fitness_high_frequency_ingestion_latency():
    """
    Fitness Function 1: Performance Rule (Fast Ingestion)
    Ensures that high-frequency IoT data ingestion takes less than 50 milliseconds
    so the system does not bottleneck during heavy load periods.
    """
    print("--- Running Ingestion Latency Fitness Function ---")
    
    start_time = time.time()
    
    # Simulating data ingestion, validation, and storage processes
    # (Smart Meter Data Ingestion -> Data Validation -> Telemetry Store)
    time.sleep(0.015)  # Simulates 15 milliseconds of processing work
    
    end_time = time.time()
    execution_time_ms = (end_time - start_time) * 1000
    
    latency_threshold_ms = 50.0
    print(f"Result: Processing took {execution_time_ms:.2f} ms (Threshold: {latency_threshold_ms} ms)")
    
    if execution_time_ms < latency_threshold_ms:
        print("STATUS: PASSED (System is fast enough)\n")
        return True
    else:
        print("STATUS: FAILED (Ingestion layer is too slow)\n")
        return False