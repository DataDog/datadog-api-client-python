"""
Create experiment returns "Created" response
"""

from os import environ
from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.experiments_api import ExperimentsApi
from datadog_api_client.v2.model.experiments_create_experiment_v2_request import ExperimentsCreateExperimentV2Request
from datadog_api_client.v2.model.experiments_create_experiment_v2_request_data import (
    ExperimentsCreateExperimentV2RequestData,
)
from datadog_api_client.v2.model.experiments_create_experiment_v2_request_data_attributes import (
    ExperimentsCreateExperimentV2RequestDataAttributes,
)
from datadog_api_client.v2.model.experiments_patch_experiment_v2_response_data_type import (
    ExperimentsPatchExperimentV2ResponseDataType,
)

body = ExperimentsCreateExperimentV2Request(
    data=ExperimentsCreateExperimentV2RequestData(
        type=ExperimentsPatchExperimentV2ResponseDataType.EXPERIMENTS,
        attributes=ExperimentsCreateExperimentV2RequestDataAttributes(
            name="ex-14bb9543f523edde",
        ),
    ),
)

configuration = Configuration()
configuration.access_token = environ["DD_BEARER_TOKEN"]
with ApiClient(configuration) as api_client:
    api_instance = ExperimentsApi(api_client)
    response = api_instance.create_experiment(body=body)

    print(response)
