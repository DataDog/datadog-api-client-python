"""
Get an org group membership returns "OK" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.org_groups_api import OrgGroupsApi
from uuid import UUID

configuration = Configuration()
configuration.unstable_operations["get_org_group_membership"] = True
with ApiClient(configuration) as api_client:
    api_instance = OrgGroupsApi(api_client)
    response = api_instance.get_org_group_membership(
        org_group_membership_id=UUID("f1e2d3c4-b5a6-7890-1234-567890abcdef"),
    )

    print(response)
