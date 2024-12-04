"""
Get SCIM group returns "OK" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.scim_api import ScimApi

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = ScimApi(api_client)
    response = api_instance.get_scim_group(
        group_id="group_id",
    )

    print(response)
