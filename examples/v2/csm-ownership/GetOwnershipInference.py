"""
Get an ownership inference by owner type returns "OK" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.csm_ownership_api import CSMOwnershipApi
from datadog_api_client.v2.model.ownership_owner_type import OwnershipOwnerType

configuration = Configuration()
configuration.unstable_operations["get_ownership_inference"] = True
with ApiClient(configuration) as api_client:
    api_instance = CSMOwnershipApi(api_client)
    response = api_instance.get_ownership_inference(
        resource_id="test-resource",
        owner_type=OwnershipOwnerType.TEAM,
    )

    print(response)
