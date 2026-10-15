"""
Update experiment protocol returns "OK" response
"""

from os import environ
from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.experiments_api import ExperimentsApi
from datadog_api_client.v2.model.experiments_patch_experiment_protocol_request import (
    ExperimentsPatchExperimentProtocolRequest,
)
from datadog_api_client.v2.model.experiments_patch_experiment_protocol_request_data import (
    ExperimentsPatchExperimentProtocolRequestData,
)
from datadog_api_client.v2.model.experiments_patch_experiment_protocol_request_data_attributes import (
    ExperimentsPatchExperimentProtocolRequestDataAttributes,
)
from datadog_api_client.v2.model.experiments_public_protocol_response_data_type import (
    ExperimentsPublicProtocolResponseDataType,
)

# there is a valid "experiment_protocol" in the system
EXPERIMENT_PROTOCOL_DATA_ID = environ["EXPERIMENT_PROTOCOL_DATA_ID"]

body = ExperimentsPatchExperimentProtocolRequest(
    data=ExperimentsPatchExperimentProtocolRequestData(
        type=ExperimentsPublicProtocolResponseDataType.PROTOCOLS,
        id=EXPERIMENT_PROTOCOL_DATA_ID,
        attributes=ExperimentsPatchExperimentProtocolRequestDataAttributes(
            description="Updated protocol description.",
        ),
    ),
)

configuration = Configuration()
configuration.access_token = environ["DD_BEARER_TOKEN"]
with ApiClient(configuration) as api_client:
    api_instance = ExperimentsApi(api_client)
    response = api_instance.patch_experiment_protocol(protocol_id=EXPERIMENT_PROTOCOL_DATA_ID, body=body)

    print(response)
