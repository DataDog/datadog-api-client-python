"""
Get an org group policy returns "OK" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.org_groups_api import OrgGroupsApi
from uuid import UUID

configuration = Configuration()
configuration.unstable_operations["get_org_group_policy"] = True
with ApiClient(configuration) as api_client:
    api_instance = OrgGroupsApi(api_client)
    response = api_instance.get_org_group_policy(
        org_group_policy_id=UUID("1a2b3c4d-5e6f-7890-abcd-ef0123456789"),
    )

    print(response)
