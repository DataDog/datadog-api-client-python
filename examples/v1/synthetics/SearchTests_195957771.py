"""
Search Synthetic tests with boolean query parameters
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v1.api.synthetics_api import SyntheticsApi

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = SyntheticsApi(api_client)
    response = api_instance.search_tests(
        include_full_config=True,
        search_suites=True,
        facets_only=True,
        start=10,
        count=5,
        sort="name,desc",
    )

    print(response)
