"""
Update experiment metric group returns "OK" response
"""

from os import environ
from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.experiments_api import ExperimentsApi
from datadog_api_client.v2.model.experiments_patch_experiment_metric_group_v2_request import (
    ExperimentsPatchExperimentMetricGroupV2Request,
)
from datadog_api_client.v2.model.experiments_patch_experiment_metric_group_v2_request_data import (
    ExperimentsPatchExperimentMetricGroupV2RequestData,
)
from datadog_api_client.v2.model.experiments_patch_experiment_metric_group_v2_request_data_attributes import (
    ExperimentsPatchExperimentMetricGroupV2RequestDataAttributes,
)
from datadog_api_client.v2.model.experiments_patch_experiment_metric_group_v2_request_data_type import (
    ExperimentsPatchExperimentMetricGroupV2RequestDataType,
)

# there is a valid "experiment" in the system
EXPERIMENT_DATA_ID = environ["EXPERIMENT_DATA_ID"]

# there is a valid "experiment_metric_group" in the system
EXPERIMENT_METRIC_GROUP_DATA_ID = environ["EXPERIMENT_METRIC_GROUP_DATA_ID"]

body = ExperimentsPatchExperimentMetricGroupV2Request(
    data=ExperimentsPatchExperimentMetricGroupV2RequestData(
        type=ExperimentsPatchExperimentMetricGroupV2RequestDataType.EXPERIMENT_METRIC_GROUPS,
        id=EXPERIMENT_METRIC_GROUP_DATA_ID,
        attributes=ExperimentsPatchExperimentMetricGroupV2RequestDataAttributes(
            name="ex-14bb9543f523edde updated",
        ),
    ),
)

configuration = Configuration()
configuration.access_token = environ["DD_BEARER_TOKEN"]
with ApiClient(configuration) as api_client:
    api_instance = ExperimentsApi(api_client)
    response = api_instance.update_experiment_metric_group(
        experiment_id=EXPERIMENT_DATA_ID, metric_group_id=EXPERIMENT_METRIC_GROUP_DATA_ID, body=body
    )

    print(response)
