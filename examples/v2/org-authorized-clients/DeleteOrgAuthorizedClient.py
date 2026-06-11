"""
Delete an org authorized client returns "No Content" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.org_authorized_clients_api import OrgAuthorizedClientsApi

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = OrgAuthorizedClientsApi(api_client)
    api_instance.delete_org_authorized_client(
        org_authorized_client_id="00000000-0000-0000-0000-000000000001",
    )
