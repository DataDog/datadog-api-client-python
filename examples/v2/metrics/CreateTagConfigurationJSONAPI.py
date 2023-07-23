"""
Create a tag configuration returns "Created" response using JSON:API models
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.metrics_api import MetricsApi
from datadog_api_client.v2.model.metric_tag_configuration_create_request import MetricTagConfigurationCreateRequestJSON
from datadog_api_client.v2.model.metric_tag_configuration_metric_types import MetricTagConfigurationMetricTypes

body = MetricTagConfigurationCreateRequestJSON(
    id="ExampleMetric",
    tags=[
        "app",
        "datacenter",
    ],
    metric_type=MetricTagConfigurationMetricTypes.GAUGE,
)

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = MetricsApi(api_client)
    response = api_instance.create_tag_configuration(metric_name="ExampleMetric", body=body)

    print(response)
