"""
List ownership inferences for a resource returns "OK" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.csm_ownership_api import CSMOwnershipApi

configuration = Configuration()
configuration.unstable_operations["list_ownership_inferences"] = True
with ApiClient(configuration) as api_client:
    api_instance = CSMOwnershipApi(api_client)
    response = api_instance.list_ownership_inferences(
        resource_id="test-resource",
    )

    print(response)
