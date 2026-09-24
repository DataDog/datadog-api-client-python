"""
List org groups returns "OK" response
"""

from os import environ
from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.org_groups_api import OrgGroupsApi

configuration = Configuration()
configuration.access_token = environ["DD_BEARER_TOKEN"]
configuration.unstable_operations["list_org_groups"] = True
with ApiClient(configuration) as api_client:
    api_instance = OrgGroupsApi(api_client)
    response = api_instance.list_org_groups()

    print(response)
