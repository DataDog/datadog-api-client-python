"""
Get pup bump test resource returns "OK" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.pup_bump_test_api import PupBumpTestApi

configuration = Configuration()
configuration.unstable_operations["get_pup_bump_test"] = True
with ApiClient(configuration) as api_client:
    api_instance = PupBumpTestApi(api_client)
    response = api_instance.get_pup_bump_test()

    print(response)
