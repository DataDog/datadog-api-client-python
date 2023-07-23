"""
Update a tag configuration returns "OK" response using JSON:API models
"""

from os import environ
from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.metrics_api import MetricsApi
from datadog_api_client.v2.model.metric_tag_configuration_update_request import MetricTagConfigurationUpdateRequestJSON

# there is a valid "metric_tag_configuration" in the system
METRIC_TAG_CONFIGURATION_DATA_ID = environ["METRIC_TAG_CONFIGURATION_DATA_ID"]

body = MetricTagConfigurationUpdateRequestJSON(
    id=METRIC_TAG_CONFIGURATION_DATA_ID,
    tags=[
        "app",
    ],
)

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = MetricsApi(api_client)
    response = api_instance.update_tag_configuration(metric_name=METRIC_TAG_CONFIGURATION_DATA_ID, body=body)

    print(response)
