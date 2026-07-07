"""
List org authorized clients returns "OK" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.org_authorized_clients_api import OrgAuthorizedClientsApi

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = OrgAuthorizedClientsApi(api_client)
    response = api_instance.list_org_authorized_clients()

    print(response)
