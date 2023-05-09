"""
Configure tags for multiple metrics returns "Accepted" response
"""

from os import environ
from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.metrics_api import MetricsApi
from datadog_api_client.v2.model.metric_bulk_configure_tags_type import MetricBulkConfigureTagsType
from datadog_api_client.v2.model.metric_bulk_tag_config_create import MetricBulkTagConfigCreate
from datadog_api_client.v2.model.metric_bulk_tag_config_create_attributes import MetricBulkTagConfigCreateAttributes
from datadog_api_client.v2.model.metric_bulk_tag_config_create_request import MetricBulkTagConfigCreateRequest

# there is a valid "user" in the system
USER_DATA_ATTRIBUTES_EMAIL = environ["USER_DATA_ATTRIBUTES_EMAIL"]

body = MetricBulkTagConfigCreateRequest(
    data=MetricBulkTagConfigCreate(
        attributes=MetricBulkTagConfigCreateAttributes(
            emails=[
                USER_DATA_ATTRIBUTES_EMAIL,
            ],
            tags=[
                "test",
                "examplemetric",
            ],
        ),
        id="system.load.1",
        type=MetricBulkConfigureTagsType.BULK_MANAGE_TAGS,
    ),
)

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = MetricsApi(api_client)
    response = api_instance.create_bulk_tags_metrics_configuration(body=body)

    print(response)
