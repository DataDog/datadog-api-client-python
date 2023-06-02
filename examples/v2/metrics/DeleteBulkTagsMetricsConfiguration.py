"""
Delete tags for multiple metrics returns "Accepted" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.metrics_api import MetricsApi
from datadog_api_client.v2.model.metric_bulk_configure_tags_type import MetricBulkConfigureTagsType
from datadog_api_client.v2.model.metric_bulk_tag_config_delete import MetricBulkTagConfigDelete
from datadog_api_client.v2.model.metric_bulk_tag_config_delete_attributes import MetricBulkTagConfigDeleteAttributes
from datadog_api_client.v2.model.metric_bulk_tag_config_delete_request import MetricBulkTagConfigDeleteRequest
from datadog_api_client.v2.model.metric_bulk_tag_config_email_list import MetricBulkTagConfigEmailList

body = MetricBulkTagConfigDeleteRequest(
    data=MetricBulkTagConfigDelete(
        attributes=MetricBulkTagConfigDeleteAttributes(
            emails=MetricBulkTagConfigEmailList(
                [
                    "sue@example.com",
                    "bob@example.com",
                ]
            ),
        ),
        id="kafka.lag",
        type=MetricBulkConfigureTagsType.BULK_MANAGE_TAGS,
    ),
)

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = MetricsApi(api_client)
    response = api_instance.delete_bulk_tags_metrics_configuration(body=body)

    print(response)
