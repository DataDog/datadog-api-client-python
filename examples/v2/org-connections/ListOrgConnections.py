"""
List Org Connections returns "OK" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.org_connections_api import OrgConnectionsApi

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = OrgConnectionsApi(api_client)
    response = api_instance.list_org_connections()

    print(response)
