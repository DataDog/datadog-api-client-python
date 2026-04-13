"""
List org group policy configs returns "OK" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.org_groups_api import OrgGroupsApi

configuration = Configuration()
configuration.unstable_operations["list_org_group_policy_configs"] = True
with ApiClient(configuration) as api_client:
    api_instance = OrgGroupsApi(api_client)
    response = api_instance.list_org_group_policy_configs()

    print(response)
