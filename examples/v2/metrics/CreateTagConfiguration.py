"""
Create a tag configuration returns "Created" response
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
        type=MetricTagConfigurationType.MANAGE_TAGS,
        id="ExampleCreateatagconfigurationreturnsCreatedresponse",
        attributes=MetricTagConfigurationCreateAttributes(
            tags=[
                "app",
                "datacenter",
            ],
            metric_type=MetricTagConfigurationMetricTypes.GAUGE,
        ),
    ),
)

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = MetricsApi(api_client)
    response = api_instance.create_tag_configuration(
        metric_name="ExampleCreateatagconfigurationreturnsCreatedresponse", body=body
    )

    print(response)
