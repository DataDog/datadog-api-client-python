"""
List case links returns "OK" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.case_management_api import CaseManagementApi

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = CaseManagementApi(api_client)
    response = api_instance.list_case_links(
        entity_type="CASE",
        entity_id="bf0cbac6-4c16-4cfb-b6bf-ca5e0ec37a4f",
    )

    print(response)
