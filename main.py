
# MAIN AUTOMATED EXECUTION RUNNER



from src.ecogrid_energy_system_design.meta_data import sample_settlement_packet
from src.ecogrid_energy_system_design.high_frequency_ingestion_latency import fitness_high_frequency_ingestion_latency
from src.ecogrid_energy_system_design.verify_domain_isolation import fitness_verify_domain_isolation
from src.ecogrid_energy_system_design.verify_settlement_security import fitness_verify_settlement_security

# =====================================================================
# MAIN AUTOMATED EXECUTION RUNNER
# =====================================================================
if __name__ == "__main__":
    print("====================================================")
    print("STARTING ECOGRID ENERGY ARCHITECTURAL FITNESS CHECKS")
    print("====================================================\n")
    
    # Run all automated architectural guardrails
    results = [
        fitness_high_frequency_ingestion_latency(),
        fitness_verify_domain_isolation(),
        fitness_verify_settlement_security()
    ]
    
    # Evaluate general build status
    if all(results):
        print("SUMMARY: All fitness functions passed! System remains clean and evolvable.")
    else:
        print("SUMMARY: Architecture rules broken! Please fix design decoupling violations.")