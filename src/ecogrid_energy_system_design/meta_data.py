
# SIMULATED ARCHITECTURAL METADATA (SYSTEM PROTOTYPE)

#Dependency maps to verify domain boundaries are preserved
SYSTEM_DEPENDENCIES = {
    "MarketplaceContext": ["AsynchronousEventBus", "MarketplaceDataStore"],
    "SmartMeterIntegrationContext": ["AsynchronousEventBus", "MeterTelemetryDataStore"],
    "FinancialSettlementContext": ["AsynchronousEventBus", "SettlementLedgerStore"]
}

#  packet to simulate high-frequency incoming IoT data
sample_iot_packet = {
    "meter_id": "METER-1092",
    "energy_kwh": 4.5,
    "timestamp": 1711881600
}

# Mock transaction packet entering Financial Settlement
sample_settlement_packet = {
    "trade_id": "TXN-88392",
    "amount_aud": 12.50,
    "has_auth_token": True  # Simulating access security status
}

