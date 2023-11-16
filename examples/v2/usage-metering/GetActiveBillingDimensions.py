"""
Get active billing dimensions for cost attribution returns "OK" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.usage_metering_api import UsageMeteringApi

configuration = Configuration()
configuration.unstable_operations["get_active_billing_dimensions"] = True
with ApiClient(configuration) as api_client:
    api_instance = UsageMeteringApi(api_client)
    response = api_instance.get_active_billing_dimensions()

    print(response)
