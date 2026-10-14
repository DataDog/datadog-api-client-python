"""
Publish experiment protocol returns "OK" response
"""

from os import environ
from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.experiments_api import ExperimentsApi

# there is a valid "configured_experiment_protocol" in the system
CONFIGURED_EXPERIMENT_PROTOCOL_DATA_ID = environ["CONFIGURED_EXPERIMENT_PROTOCOL_DATA_ID"]

configuration = Configuration()
configuration.access_token = environ["DD_BEARER_TOKEN"]
with ApiClient(configuration) as api_client:
    api_instance = ExperimentsApi(api_client)
    response = api_instance.publish_experiment_protocol(
        protocol_id=CONFIGURED_EXPERIMENT_PROTOCOL_DATA_ID,
    )

    print(response)
