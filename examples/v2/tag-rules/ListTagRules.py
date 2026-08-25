"""
List tag rules returns "OK" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.tag_rules_api import TagRulesApi

configuration = Configuration()
configuration.unstable_operations["list_tag_rules"] = True
with ApiClient(configuration) as api_client:
    api_instance = TagRulesApi(api_client)
    response = api_instance.list_tag_rules()

    print(response)
