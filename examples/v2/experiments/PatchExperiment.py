"""
Patch experiment returns "OK" response
"""

from os import environ
from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.experiments_api import ExperimentsApi
from datadog_api_client.v2.model.experiments_patch_experiment_v2_request import ExperimentsPatchExperimentV2Request
from datadog_api_client.v2.model.experiments_patch_experiment_v2_request_data import (
    ExperimentsPatchExperimentV2RequestData,
)
from datadog_api_client.v2.model.experiments_patch_experiment_v2_request_data_attributes import (
    ExperimentsPatchExperimentV2RequestDataAttributes,
)
from datadog_api_client.v2.model.experiments_patch_experiment_v2_response_data_type import (
    ExperimentsPatchExperimentV2ResponseDataType,
)

# there is a valid "experiment" in the system
EXPERIMENT_DATA_ID = environ["EXPERIMENT_DATA_ID"]

body = ExperimentsPatchExperimentV2Request(
    data=ExperimentsPatchExperimentV2RequestData(
        type=ExperimentsPatchExperimentV2ResponseDataType.EXPERIMENTS,
        attributes=ExperimentsPatchExperimentV2RequestDataAttributes(
            name="ex-14bb9543f523edde updated",
        ),
    ),
)

configuration = Configuration()
configuration.access_token = environ["DD_BEARER_TOKEN"]
with ApiClient(configuration) as api_client:
    api_instance = ExperimentsApi(api_client)
    response = api_instance.patch_experiment(experiment_id=EXPERIMENT_DATA_ID, body=body)

    print(response)
