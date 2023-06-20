"""
Configure tags for multiple metrics returns "Accepted" response using JSON:API models
"""

from os import environ
from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.metrics_api import MetricsApi
from datadog_api_client.v2.model.metric_bulk_tag_config_create_request import MetricBulkTagConfigCreateRequestJSON
from datadog_api_client.v2.model.metric_bulk_tag_config_email_list import MetricBulkTagConfigEmailList
from datadog_api_client.v2.model.metric_bulk_tag_config_tag_name_list import MetricBulkTagConfigTagNameList

# there is a valid "user" in the system
USER_DATA_ATTRIBUTES_EMAIL = environ["USER_DATA_ATTRIBUTES_EMAIL"]

body = MetricBulkTagConfigCreateRequestJSON(
    emails=MetricBulkTagConfigEmailList(
        [
            USER_DATA_ATTRIBUTES_EMAIL,
        ]
    ),
    tags=MetricBulkTagConfigTagNameList(
        [
            "test",
            "examplemetric",
        ]
    ),
)

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = MetricsApi(api_client)
    response = api_instance.create_bulk_tags_metrics_configuration(body=body)

    print(response)
