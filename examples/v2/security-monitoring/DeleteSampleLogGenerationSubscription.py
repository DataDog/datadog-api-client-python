"""
Unsubscribe from sample log generation returns "OK" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.security_monitoring_api import SecurityMonitoringApi

configuration = Configuration()
configuration.unstable_operations["delete_sample_log_generation_subscription"] = True
with ApiClient(configuration) as api_client:
    api_instance = SecurityMonitoringApi(api_client)
    response = api_instance.delete_sample_log_generation_subscription(
        content_pack_id="content_pack_id",
    )

    print(response)
