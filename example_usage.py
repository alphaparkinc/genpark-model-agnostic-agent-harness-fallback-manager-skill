from client import ModelAgnosticAgentHarnessFallbackManagerClient

def main():
    client = ModelAgnosticAgentHarnessFallbackManagerClient()
    res = client.route_harness("Claude_3.7_Sonnet", ["Gemini_3.7_Flash", "DeepSeek_V4"])
    print(f"Active Provider: {res['active_provider_routed']}")
    print(f"Failover: {res['failover_occurred']}")
    print(f"Routing Latency: {res['routing_latency_ms']}ms")

if __name__ == "__main__":
    main()
