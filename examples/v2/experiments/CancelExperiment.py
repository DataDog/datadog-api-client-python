"""
Cancel experiment returns "The experiment was canceled and unlinked from its feature flag allocations." response
"""

from os import environ
from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.experiments_api import ExperimentsApi
from datadog_api_client.v2.model.experiments_cancel_experiment_v2_request import ExperimentsCancelExperimentV2Request
from datadog_api_client.v2.model.experiments_cancel_experiment_v2_request_data import (
    ExperimentsCancelExperimentV2RequestData,
)
from datadog_api_client.v2.model.experiments_cancel_experiment_v2_request_data_attributes import (
    ExperimentsCancelExperimentV2RequestDataAttributes,
)
from datadog_api_client.v2.model.experiments_cancel_experiment_v2_request_data_type import (
    ExperimentsCancelExperimentV2RequestDataType,
)

# there is a valid "experiment" in the system
EXPERIMENT_DATA_ID = environ["EXPERIMENT_DATA_ID"]

body = ExperimentsCancelExperimentV2Request(
    data=ExperimentsCancelExperimentV2RequestData(
        type=ExperimentsCancelExperimentV2RequestDataType.CANCEL_EXPERIMENT_REQUEST,
        attributes=ExperimentsCancelExperimentV2RequestDataAttributes(
            reason="Cancel the test experiment",
        ),
    ),
)

configuration = Configuration()
configuration.access_token = environ["DD_BEARER_TOKEN"]
with ApiClient(configuration) as api_client:
    api_instance = ExperimentsApi(api_client)
    api_instance.cancel_experiment(experiment_id=EXPERIMENT_DATA_ID, body=body)
