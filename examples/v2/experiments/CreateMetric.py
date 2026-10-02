"""
Create metric returns "Created" response
"""

from os import environ
from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.experiments_api import ExperimentsApi
from datadog_api_client.v2.model.experiments_create_metric_numerator_attributes import (
    ExperimentsCreateMetricNumeratorAttributes,
)
from datadog_api_client.v2.model.experiments_create_metric_v2_request import ExperimentsCreateMetricV2Request
from datadog_api_client.v2.model.experiments_create_metric_v2_request_data import ExperimentsCreateMetricV2RequestData
from datadog_api_client.v2.model.experiments_create_metric_v2_request_data_attributes_data_source_type import (
    ExperimentsCreateMetricV2RequestDataAttributesDataSourceType,
)
from datadog_api_client.v2.model.experiments_create_metric_v2_request_data_attributes_desired_change import (
    ExperimentsCreateMetricV2RequestDataAttributesDesiredChange,
)
from datadog_api_client.v2.model.experiments_datadog_metric_aggregation_input import (
    ExperimentsDatadogMetricAggregationInput,
)
from datadog_api_client.v2.model.experiments_datadog_metric_measure_input import ExperimentsDatadogMetricMeasureInput
from datadog_api_client.v2.model.metric_type import MetricType

body = ExperimentsCreateMetricV2Request(
    data=ExperimentsCreateMetricV2RequestData(
        type=MetricType.METRICS,
        attributes=ExperimentsCreateMetricNumeratorAttributes(
            name="ex-14bb9543f523edde",
            data_source_type=ExperimentsCreateMetricV2RequestDataAttributesDataSourceType.DATADOG,
            desired_change=ExperimentsCreateMetricV2RequestDataAttributesDesiredChange.METRIC_INCREASES,
            numerator_aggregation=ExperimentsDatadogMetricAggregationInput(
                operation="sum",
                datadog_metric_measure=ExperimentsDatadogMetricMeasureInput(
                    name="ex-14bb9543f523edde view duration",
                    source_type="PRODUCT_ANALYTICS",
                    source_subtype="RUM_VIEWS",
                    column_type="double",
                    column_name="@view.time_spent",
                ),
            ),
        ),
    ),
)

configuration = Configuration()
configuration.access_token = environ["DD_BEARER_TOKEN"]
with ApiClient(configuration) as api_client:
    api_instance = ExperimentsApi(api_client)
    response = api_instance.create_metric(body=body)

    print(response)
