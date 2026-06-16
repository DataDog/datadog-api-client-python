"""
List ownership history by owner type returns "OK" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.csm_ownership_api import CSMOwnershipApi
from datadog_api_client.v2.model.ownership_owner_type import OwnershipOwnerType

configuration = Configuration()
configuration.unstable_operations["list_ownership_history_by_owner_type"] = True
with ApiClient(configuration) as api_client:
    api_instance = CSMOwnershipApi(api_client)
    response = api_instance.list_ownership_history_by_owner_type(
        resource_id="res-1",
        owner_type=OwnershipOwnerType.TEAM,
    )

    print(response)
