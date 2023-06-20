"""
Delete tags for multiple metrics returns "Accepted" response using JSON:API models
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.metrics_api import MetricsApi
from datadog_api_client.v2.model.metric_bulk_tag_config_delete_request import MetricBulkTagConfigDeleteRequestJSON
from datadog_api_client.v2.model.metric_bulk_tag_config_email_list import MetricBulkTagConfigEmailList

body = MetricBulkTagConfigDeleteRequestJSON(
    emails=MetricBulkTagConfigEmailList(
        [
            "sue@example.com",
            "bob@example.com",
        ]
    ),
)

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = MetricsApi(api_client)
    response = api_instance.delete_bulk_tags_metrics_configuration(body=body)

    print(response)
