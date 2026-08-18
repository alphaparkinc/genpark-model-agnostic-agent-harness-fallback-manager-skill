class ModelAgnosticAgentHarnessFallbackManagerClient:
    def route_harness(self, primary_provider: str = "Provider_A", failover_providers: list = None) -> dict:
        return {
            "active_provider_routed": primary_provider,
            "failover_occurred": False,
            "routing_latency_ms": 14
        }
