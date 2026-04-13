"""
List org group policy overrides returns "OK" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.org_groups_api import OrgGroupsApi
from uuid import UUID

configuration = Configuration()
configuration.unstable_operations["list_org_group_policy_overrides"] = True
with ApiClient(configuration) as api_client:
    api_instance = OrgGroupsApi(api_client)
    response = api_instance.list_org_group_policy_overrides(
        filter_org_group_id=UUID("a1b2c3d4-e5f6-7890-abcd-ef0123456789"),
    )

    print(response)
