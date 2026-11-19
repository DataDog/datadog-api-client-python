"""
Get bandit results returns "OK" response
"""

from os import environ
from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.experiments_api import ExperimentsApi

# there is a valid "bandit" in the system
BANDIT_DATA_ID = environ["BANDIT_DATA_ID"]

configuration = Configuration()
configuration.access_token = environ["DD_BEARER_TOKEN"]
configuration.unstable_operations["create_bandit"] = True
configuration.unstable_operations["get_bandit_results"] = True
with ApiClient(configuration) as api_client:
    api_instance = ExperimentsApi(api_client)
    response = api_instance.get_bandit_results(
        bandit_id=BANDIT_DATA_ID,
    )

    print(response)
