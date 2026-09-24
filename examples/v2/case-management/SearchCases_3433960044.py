"""
Search cases returns "OK" response with pagination
"""

from os import environ
from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.case_management_api import CaseManagementApi

configuration = Configuration()
configuration.access_token = environ["DD_BEARER_TOKEN"]
with ApiClient(configuration) as api_client:
    api_instance = CaseManagementApi(api_client)
    items = api_instance.search_cases_with_pagination(
        page_size=2,
        filter="status:closed",
    )
    for item in items:
        print(item)
