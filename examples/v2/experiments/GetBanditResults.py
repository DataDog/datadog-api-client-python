"""
Get bandit results returns "OK" response
"""

from os import environ
from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.experiments_api import ExperimentsApi
from uuid import UUID

configuration = Configuration()
configuration.access_token = environ["DD_BEARER_TOKEN"]
configuration.unstable_operations["get_bandit_results"] = True
with ApiClient(configuration) as api_client:
    api_instance = ExperimentsApi(api_client)
    response = api_instance.get_bandit_results(
        bandit_id=UUID("4b1f3c2e-8d5a-4f6b-9c7e-1a2b3c4d5e6f"),
    )

    print(response)
