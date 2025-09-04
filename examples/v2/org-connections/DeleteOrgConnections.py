"""
Delete Org Connection returns "OK" response
"""

from os import environ
from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.org_connections_api import OrgConnectionsApi

# there is a valid "org_connection" in the system
ORG_CONNECTION_DATA_ID = environ["ORG_CONNECTION_DATA_ID"]

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = OrgConnectionsApi(api_client)
    api_instance.delete_org_connections(
        connection_id=ORG_CONNECTION_DATA_ID,
    )
