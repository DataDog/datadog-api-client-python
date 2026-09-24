"""
Get all hosts with metadata for your organization returns "OK" response
"""

from os import environ
from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v1.api.hosts_api import HostsApi

configuration = Configuration()
configuration.access_token = environ["DD_BEARER_TOKEN"]
with ApiClient(configuration) as api_client:
    api_instance = HostsApi(api_client)
    response = api_instance.list_hosts(
        include_hosts_metadata=True,
    )

    print(response)
