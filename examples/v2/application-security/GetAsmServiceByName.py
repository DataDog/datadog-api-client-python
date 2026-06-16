"""
Get Application Security details for a service returns "OK" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.application_security_api import ApplicationSecurityApi

configuration = Configuration()
configuration.unstable_operations["get_asm_service_by_name"] = True
with ApiClient(configuration) as api_client:
    api_instance = ApplicationSecurityApi(api_client)
    response = api_instance.get_asm_service_by_name(
        service_filter="service_filter",
    )

    print(response)
