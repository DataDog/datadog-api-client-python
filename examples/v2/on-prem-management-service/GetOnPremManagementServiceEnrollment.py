"""
Get enrollment status returns "OK" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.on_prem_management_service_api import OnPremManagementServiceApi

configuration = Configuration()
configuration.unstable_operations["get_on_prem_management_service_enrollment"] = True
with ApiClient(configuration) as api_client:
    api_instance = OnPremManagementServiceApi(api_client)
    response = api_instance.get_on_prem_management_service_enrollment(
        token_hash="aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
    )

    print(response)
