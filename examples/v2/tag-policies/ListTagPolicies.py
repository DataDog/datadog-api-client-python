"""
List tag policies returns "OK" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.tag_policies_api import TagPoliciesApi

configuration = Configuration()
configuration.unstable_operations["list_tag_policies"] = True
with ApiClient(configuration) as api_client:
    api_instance = TagPoliciesApi(api_client)
    response = api_instance.list_tag_policies()

    print(response)
