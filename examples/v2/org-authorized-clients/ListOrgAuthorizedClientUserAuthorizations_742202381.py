"""
List user authorizations for a client returns "OK" response with pagination
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.org_authorized_clients_api import OrgAuthorizedClientsApi

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = OrgAuthorizedClientsApi(api_client)
    items = api_instance.list_org_authorized_client_user_authorizations_with_pagination(
        org_authorized_client_id="00000000-0000-0000-0000-000000000001",
    )
    for item in items:
        print(item)
