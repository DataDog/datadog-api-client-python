"""
Create experiment metric group returns "Created" response
"""

from os import environ
from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.experiments_api import ExperimentsApi
from datadog_api_client.v2.model.experiments_create_experiment_metric_group_v2_request import (
    ExperimentsCreateExperimentMetricGroupV2Request,
)
from datadog_api_client.v2.model.experiments_create_experiment_metric_group_v2_request_data import (
    ExperimentsCreateExperimentMetricGroupV2RequestData,
)
from datadog_api_client.v2.model.experiments_create_experiment_metric_group_v2_request_data_attributes import (
    ExperimentsCreateExperimentMetricGroupV2RequestDataAttributes,
)
from datadog_api_client.v2.model.experiments_create_experiment_metric_group_v2_request_data_attributes_metrics_items import (
    ExperimentsCreateExperimentMetricGroupV2RequestDataAttributesMetricsItems,
)
from datadog_api_client.v2.model.experiments_patch_experiment_metric_group_v2_request_data_type import (
    ExperimentsPatchExperimentMetricGroupV2RequestDataType,
)

# there is a valid "experiment" in the system
EXPERIMENT_DATA_ID = environ["EXPERIMENT_DATA_ID"]

# there is a valid "experiment_metric" in the system
EXPERIMENT_METRIC_DATA_ID = environ["EXPERIMENT_METRIC_DATA_ID"]

body = ExperimentsCreateExperimentMetricGroupV2Request(
    data=ExperimentsCreateExperimentMetricGroupV2RequestData(
        type=ExperimentsPatchExperimentMetricGroupV2RequestDataType.EXPERIMENT_METRIC_GROUPS,
        attributes=ExperimentsCreateExperimentMetricGroupV2RequestDataAttributes(
            name="ex-14bb9543f523edde",
            metrics=[
                ExperimentsCreateExperimentMetricGroupV2RequestDataAttributesMetricsItems(
                    metric_id=EXPERIMENT_METRIC_DATA_ID,
                ),
            ],
        ),
    ),
)

configuration = Configuration()
configuration.access_token = environ["DD_BEARER_TOKEN"]
with ApiClient(configuration) as api_client:
    api_instance = ExperimentsApi(api_client)
    response = api_instance.create_experiment_metric_group(experiment_id=EXPERIMENT_DATA_ID, body=body)

    print(response)
