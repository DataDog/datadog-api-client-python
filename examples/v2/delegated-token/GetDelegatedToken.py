"""
Get a delegated token returns "OK" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.delegated_token_api import DelegatedTokenApi

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = DelegatedTokenApi(api_client)
    response = api_instance.get_delegated_token()

    print(response)
