"""
Get signals matching an event returns "OK" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.security_monitoring_api import SecurityMonitoringApi

configuration = Configuration()
configuration.unstable_operations["get_matching_signals"] = True
with ApiClient(configuration) as api_client:
    api_instance = SecurityMonitoringApi(api_client)
    response = api_instance.get_matching_signals(
        event_id="event_id",
        track="track",
    )

    print(response)
