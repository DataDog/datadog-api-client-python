"""
Search cases returns "OK" response with pagination
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.cases_api import CasesApi

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = CasesApi(api_client)
    items = api_instance.search_cases_with_pagination()
    for item in items:
        print(item)
