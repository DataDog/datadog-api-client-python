"""
Get a tag pipeline ruleset returns "OK" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.cloud_cost_management_api import CloudCostManagementApi

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = CloudCostManagementApi(api_client)
    response = api_instance.get_tag_pipelines_ruleset(
        ruleset_id="a1e9de9b-b88e-41c6-a0cd-cc0ebd7092de",
    )

    print(response)
