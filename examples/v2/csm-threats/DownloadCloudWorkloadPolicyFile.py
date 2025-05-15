"""
Download the Workload Protection policy (US1-FED) returns "OK" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.csm_threats_api import CSMThreatsApi

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = CSMThreatsApi(api_client)
    response = api_instance.download_cloud_workload_policy_file()

    print(response.read())
