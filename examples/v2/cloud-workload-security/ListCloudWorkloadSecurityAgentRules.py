"""
Get all Cloud Workload Security Agent rules returns "OK" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.cloud_workload_security_api import CloudWorkloadSecurityApi

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = CloudWorkloadSecurityApi(api_client)
    response = api_instance.list_cloud_workload_security_agent_rules()

    print(response)
