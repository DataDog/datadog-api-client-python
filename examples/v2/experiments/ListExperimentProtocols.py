"""
List experiment protocols returns "OK" response
"""

from os import environ
from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.experiments_api import ExperimentsApi
from datadog_api_client.v2.model.experiments_public_protocol_response_data_attributes_status import (
    ExperimentsPublicProtocolResponseDataAttributesStatus,
)

# there is a valid "experiment_protocol" in the system
EXPERIMENT_PROTOCOL_DATA_ATTRIBUTES_NAME = environ["EXPERIMENT_PROTOCOL_DATA_ATTRIBUTES_NAME"]

configuration = Configuration()
configuration.access_token = environ["DD_BEARER_TOKEN"]
with ApiClient(configuration) as api_client:
    api_instance = ExperimentsApi(api_client)
    response = api_instance.list_experiment_protocols(
        filter_status=[
            ExperimentsPublicProtocolResponseDataAttributesStatus.DRAFT,
        ],
        filter_query=EXPERIMENT_PROTOCOL_DATA_ATTRIBUTES_NAME,
    )

    print(response)
