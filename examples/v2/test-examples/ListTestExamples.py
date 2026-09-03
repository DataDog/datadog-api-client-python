"""
List test examples returns "OK" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.test_examples_api import TestExamplesApi

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = TestExamplesApi(api_client)
    response = api_instance.list_test_examples()

    print(response)
