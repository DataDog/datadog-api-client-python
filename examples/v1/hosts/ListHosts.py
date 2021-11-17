"""
Get all hosts for your organization returns "OK" response
"""

from datadog_api_client.v1 import ApiClient, Configuration
from datadog_api_client.v1.api.hosts_api import HostsApi

with ApiClient(Configuration()) as api_client:
    api_instance = HostsApi(api_client)
    response = api_instance.list_hosts(filter="env:ci", include_hosts_metadata=True)

    print(response)
