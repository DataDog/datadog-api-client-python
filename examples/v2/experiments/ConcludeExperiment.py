"""
Conclude experiment returns "The experiment was concluded and the winning variant was rolled out to its linked feature
flag allocation." response
"""

from os import environ
from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.experiments_api import ExperimentsApi
from datadog_api_client.v2.model.experiments_conclude_experiment_v2_request import (
    ExperimentsConcludeExperimentV2Request,
)
from datadog_api_client.v2.model.experiments_conclude_experiment_v2_request_data import (
    ExperimentsConcludeExperimentV2RequestData,
)
from datadog_api_client.v2.model.experiments_conclude_experiment_v2_request_data_attributes import (
    ExperimentsConcludeExperimentV2RequestDataAttributes,
)
from datadog_api_client.v2.model.experiments_conclude_experiment_v2_request_data_type import (
    ExperimentsConcludeExperimentV2RequestDataType,
)
from uuid import UUID

body = ExperimentsConcludeExperimentV2Request(
    data=ExperimentsConcludeExperimentV2RequestData(
        attributes=ExperimentsConcludeExperimentV2RequestDataAttributes(
            decision_variant_key="treatment",
        ),
        type=ExperimentsConcludeExperimentV2RequestDataType.CONCLUDE_EXPERIMENT_REQUEST,
    ),
)

configuration = Configuration()
configuration.access_token = environ["DD_BEARER_TOKEN"]
with ApiClient(configuration) as api_client:
    api_instance = ExperimentsApi(api_client)
    api_instance.conclude_experiment(experiment_id=UUID("550e8400-e29b-41d4-a716-446655440000"), body=body)
