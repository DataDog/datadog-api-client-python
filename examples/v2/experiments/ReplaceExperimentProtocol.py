"""
Replace experiment protocol returns "OK" response
"""

from os import environ
from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.experiments_api import ExperimentsApi
from datadog_api_client.v2.model.experiments_public_protocol_response_data_type import (
    ExperimentsPublicProtocolResponseDataType,
)
from datadog_api_client.v2.model.experiments_replace_experiment_protocol_request import (
    ExperimentsReplaceExperimentProtocolRequest,
)
from datadog_api_client.v2.model.experiments_replace_experiment_protocol_request_data import (
    ExperimentsReplaceExperimentProtocolRequestData,
)
from datadog_api_client.v2.model.experiments_replace_experiment_protocol_request_data_attributes import (
    ExperimentsReplaceExperimentProtocolRequestDataAttributes,
)

# there is a valid "published_protocol" in the system
PUBLISHED_PROTOCOL_DATA_ATTRIBUTES_UPDATED_AT = environ["PUBLISHED_PROTOCOL_DATA_ATTRIBUTES_UPDATED_AT"]
PUBLISHED_PROTOCOL_DATA_ID = environ["PUBLISHED_PROTOCOL_DATA_ID"]

# there is a valid "experiment_subject_type" in the system
EXPERIMENT_SUBJECT_TYPE_DATA_ID = environ["EXPERIMENT_SUBJECT_TYPE_DATA_ID"]

body = ExperimentsReplaceExperimentProtocolRequest(
    data=ExperimentsReplaceExperimentProtocolRequestData(
        type=ExperimentsPublicProtocolResponseDataType.PROTOCOLS,
        id=PUBLISHED_PROTOCOL_DATA_ID,
        attributes=ExperimentsReplaceExperimentProtocolRequestDataAttributes(
            subject_type_id=EXPERIMENT_SUBJECT_TYPE_DATA_ID,
            is_equal_split_enforced=False,
            is_minimum_duration_enabled=False,
            is_duration_required_to_start=False,
            is_metric_limit_enabled=False,
            metric_groups=[],
            default_duration_days=14,
        ),
    ),
)

configuration = Configuration()
configuration.access_token = environ["DD_BEARER_TOKEN"]
with ApiClient(configuration) as api_client:
    api_instance = ExperimentsApi(api_client)
    response = api_instance.replace_experiment_protocol(
        protocol_id=PUBLISHED_PROTOCOL_DATA_ID,
        expected_updated_at=PUBLISHED_PROTOCOL_DATA_ATTRIBUTES_UPDATED_AT,
        body=body,
    )

    print(response)
