"""
Get an org group returns "OK" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.org_groups_api import OrgGroupsApi
from uuid import UUID

configuration = Configuration()
configuration.unstable_operations["get_org_group"] = True
with ApiClient(configuration) as api_client:
    api_instance = OrgGroupsApi(api_client)
    response = api_instance.get_org_group(
        org_group_id=UUID("a1b2c3d4-e5f6-7890-abcd-ef0123456789"),
    )

    print(response)
