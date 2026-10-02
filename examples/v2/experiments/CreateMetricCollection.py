"""
Create metric collection returns "Created" response
"""

from os import environ
from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.experiments_api import ExperimentsApi
from datadog_api_client.v2.model.experiments_create_metric_collection_v2_request import (
    ExperimentsCreateMetricCollectionV2Request,
)
from datadog_api_client.v2.model.experiments_create_metric_collection_v2_request_data import (
    ExperimentsCreateMetricCollectionV2RequestData,
)
from datadog_api_client.v2.model.experiments_create_metric_collection_v2_request_data_attributes import (
    ExperimentsCreateMetricCollectionV2RequestDataAttributes,
)
from datadog_api_client.v2.model.experiments_patch_metric_collection_v2_request_data_type import (
    ExperimentsPatchMetricCollectionV2RequestDataType,
)

body = ExperimentsCreateMetricCollectionV2Request(
    data=ExperimentsCreateMetricCollectionV2RequestData(
        type=ExperimentsPatchMetricCollectionV2RequestDataType.METRIC_COLLECTIONS,
        attributes=ExperimentsCreateMetricCollectionV2RequestDataAttributes(
            name="ex-14bb9543f523edde",
        ),
    ),
)

configuration = Configuration()
configuration.access_token = environ["DD_BEARER_TOKEN"]
with ApiClient(configuration) as api_client:
    api_instance = ExperimentsApi(api_client)
    response = api_instance.create_metric_collection(body=body)

    print(response)
