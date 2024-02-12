"""
Search cases returns "OK" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.cases_api import CasesApi

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = CasesApi(api_client)
    response = api_instance.search_cases()

    print(response)
