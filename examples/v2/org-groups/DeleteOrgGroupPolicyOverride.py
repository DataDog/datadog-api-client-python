"""
Delete an org group policy override returns "No Content" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.org_groups_api import OrgGroupsApi
from uuid import UUID

configuration = Configuration()
configuration.unstable_operations["delete_org_group_policy_override"] = True
with ApiClient(configuration) as api_client:
    api_instance = OrgGroupsApi(api_client)
    api_instance.delete_org_group_policy_override(
        org_group_policy_override_id=UUID("9f8e7d6c-5b4a-3210-fedc-ba0987654321"),
    )
