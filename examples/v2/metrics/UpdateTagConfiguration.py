"""
Update a tag configuration returns "OK" response
"""

from os import environ
from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.metrics_api import MetricsApi
from datadog_api_client.v2.model.metric_tag_configuration_type import MetricTagConfigurationType
from datadog_api_client.v2.model.metric_tag_configuration_update_attributes import (
    MetricTagConfigurationUpdateAttributes,
)
from datadog_api_client.v2.model.metric_tag_configuration_update_data import MetricTagConfigurationUpdateData
from datadog_api_client.v2.model.metric_tag_configuration_update_request import MetricTagConfigurationUpdateRequest

# there is a valid "metric_tag_configuration" in the system
METRIC_TAG_CONFIGURATION_DATA_ID = environ["METRIC_TAG_CONFIGURATION_DATA_ID"]

body = MetricTagConfigurationUpdateRequest(
    data=MetricTagConfigurationUpdateData(
        type=MetricTagConfigurationType.MANAGE_TAGS,
        id=METRIC_TAG_CONFIGURATION_DATA_ID,
        attributes=MetricTagConfigurationUpdateAttributes(
            tags=[
                "app",
            ],
        ),
    ),
)

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = MetricsApi(api_client)
    response = api_instance.update_tag_configuration(metric_name=METRIC_TAG_CONFIGURATION_DATA_ID, body=body)

    print(response)
