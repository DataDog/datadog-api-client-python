"""
Get a monitor configuration policy returns "Created" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.metrics_api import MetricsApi
from datadog_api_client.v2.model.metric_tag_configuration_create_attributes import (
    MetricTagConfigurationCreateAttributes,
)
from datadog_api_client.v2.model.metric_tag_configuration_create_data import MetricTagConfigurationCreateData
from datadog_api_client.v2.model.metric_tag_configuration_create_request import MetricTagConfigurationCreateRequest
from datadog_api_client.v2.model.metric_tag_configuration_metric_types import MetricTagConfigurationMetricTypes
from datadog_api_client.v2.model.metric_tag_configuration_type import MetricTagConfigurationType

body = MetricTagConfigurationCreateRequest(
    data=MetricTagConfigurationCreateData(
        attributes=MetricTagConfigurationCreateAttributes(
            include_percentiles=False,
            metric_type=MetricTagConfigurationMetricTypes.DISTRIBUTION,
            tags=[
                "app",
                "datacenter",
            ],
        ),
        id="http.endpoint.request",
        type=MetricTagConfigurationType.MANAGE_TAGS,
    ),
)

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = MetricsApi(api_client)
    response = api_instance.create_tag_configuration(metric_name="metric_name", body=body)

    print(response)
