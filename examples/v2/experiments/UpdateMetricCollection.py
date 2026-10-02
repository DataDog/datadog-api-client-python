"""
Update metric collection returns "OK" response
"""

from os import environ
from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.experiments_api import ExperimentsApi
from datadog_api_client.v2.model.experiments_patch_metric_collection_v2_request import (
    ExperimentsPatchMetricCollectionV2Request,
)
from datadog_api_client.v2.model.experiments_patch_metric_collection_v2_request_data import (
    ExperimentsPatchMetricCollectionV2RequestData,
)
from datadog_api_client.v2.model.experiments_patch_metric_collection_v2_request_data_attributes import (
    ExperimentsPatchMetricCollectionV2RequestDataAttributes,
)
from datadog_api_client.v2.model.experiments_patch_metric_collection_v2_request_data_type import (
    ExperimentsPatchMetricCollectionV2RequestDataType,
)

# there is a valid "experiment_metric_collection" in the system
EXPERIMENT_METRIC_COLLECTION_DATA_ID = environ["EXPERIMENT_METRIC_COLLECTION_DATA_ID"]

body = ExperimentsPatchMetricCollectionV2Request(
    data=ExperimentsPatchMetricCollectionV2RequestData(
        type=ExperimentsPatchMetricCollectionV2RequestDataType.METRIC_COLLECTIONS,
        attributes=ExperimentsPatchMetricCollectionV2RequestDataAttributes(
            name="ex-14bb9543f523edde updated",
        ),
    ),
)

configuration = Configuration()
configuration.access_token = environ["DD_BEARER_TOKEN"]
with ApiClient(configuration) as api_client:
    api_instance = ExperimentsApi(api_client)
    response = api_instance.update_metric_collection(
        metric_collection_id=EXPERIMENT_METRIC_COLLECTION_DATA_ID, body=body
    )

    print(response)
