"""
Update metric returns "OK" response
"""

from os import environ
from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.experiments_api import ExperimentsApi
from datadog_api_client.v2.model.experiments_update_metric_v2_request import ExperimentsUpdateMetricV2Request
from datadog_api_client.v2.model.experiments_update_metric_v2_request_data import ExperimentsUpdateMetricV2RequestData
from datadog_api_client.v2.model.experiments_update_metric_v2_request_data_attributes import (
    ExperimentsUpdateMetricV2RequestDataAttributes,
)
from datadog_api_client.v2.model.metric_type import MetricType

# there is a valid "experiment_metric" in the system
EXPERIMENT_METRIC_DATA_ID = environ["EXPERIMENT_METRIC_DATA_ID"]

body = ExperimentsUpdateMetricV2Request(
    data=ExperimentsUpdateMetricV2RequestData(
        type=MetricType.METRICS,
        id=EXPERIMENT_METRIC_DATA_ID,
        attributes=ExperimentsUpdateMetricV2RequestDataAttributes(
            name="ex-14bb9543f523edde updated",
        ),
    ),
)

configuration = Configuration()
configuration.access_token = environ["DD_BEARER_TOKEN"]
with ApiClient(configuration) as api_client:
    api_instance = ExperimentsApi(api_client)
    response = api_instance.update_metric(metric_id=EXPERIMENT_METRIC_DATA_ID, body=body)

    print(response)
