"""
Create experiment protocol returns "Created" response
"""

from os import environ
from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.experiments_api import ExperimentsApi
from datadog_api_client.v2.model.experiments_create_experiment_protocol_request import (
    ExperimentsCreateExperimentProtocolRequest,
)
from datadog_api_client.v2.model.experiments_create_experiment_protocol_request_data import (
    ExperimentsCreateExperimentProtocolRequestData,
)
from datadog_api_client.v2.model.experiments_create_experiment_protocol_request_data_attributes import (
    ExperimentsCreateExperimentProtocolRequestDataAttributes,
)
from datadog_api_client.v2.model.experiments_public_protocol_response_data_type import (
    ExperimentsPublicProtocolResponseDataType,
)

body = ExperimentsCreateExperimentProtocolRequest(
    data=ExperimentsCreateExperimentProtocolRequestData(
        type=ExperimentsPublicProtocolResponseDataType.PROTOCOLS,
        attributes=ExperimentsCreateExperimentProtocolRequestDataAttributes(
            name="ex-protocol-14bb9543f523edde",
            description="Protocol created by the API test.",
        ),
    ),
)

configuration = Configuration()
configuration.access_token = environ["DD_BEARER_TOKEN"]
with ApiClient(configuration) as api_client:
    api_instance = ExperimentsApi(api_client)
    response = api_instance.create_experiment_protocol(body=body)

    print(response)
