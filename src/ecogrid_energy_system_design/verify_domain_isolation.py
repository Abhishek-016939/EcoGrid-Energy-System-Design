

from ecogrid_energy_system_design.meta_data import SYSTEM_DEPENDENCIES


def fitness_verify_domain_isolation():
    """
    Fitness Function 2: Evolvability & Maintainability Rule (Domain Separation)
    Ensures that Marketplace logic does NOT directly communicate with or depend on
    the Smart Meter Ingestion internals. Everything must pass through the Event Bus.
    """
    print("--- Running Domain Separation Isolation Fitness Function ---")
    
    # Get what components the Marketplace is touching directly
    marketplace_deps = SYSTEM_DEPENDENCIES.get("MarketplaceContext", [])
    
    # Violation Check: Did anyone bypass the Event Bus and tightly couple them?
    forbidden_dependency = "SmartMeterDataIngestion"
    
    if forbidden_dependency in marketplace_deps:
        print(f"STATUS: FAILED! Marketplace directly imports '{forbidden_dependency}'.")
        print("Architecture Violation: Must go through the Asynchronous Event Bus instead!\n")
        return False
    else:
        print("STATUS: PASSED (Marketplace and Smart Meter domains are cleanly separated)\n")
        return True