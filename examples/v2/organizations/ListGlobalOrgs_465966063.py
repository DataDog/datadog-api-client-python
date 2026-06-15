"""
List global orgs returns "OK" response with pagination
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.organizations_api import OrganizationsApi

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = OrganizationsApi(api_client)
    items = api_instance.list_global_orgs_with_pagination(
        user_handle="user@example.com",
    )
    for item in items:
        print(item)
