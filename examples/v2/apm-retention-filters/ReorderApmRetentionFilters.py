"""
Re-order retention filters returns "OK" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.apm_retention_filters_api import APMRetentionFiltersApi
from datadog_api_client.v2.model.apm_retention_filter_type import ApmRetentionFilterType
from datadog_api_client.v2.model.reorder_retention_filters_request import ReorderRetentionFiltersRequest
from datadog_api_client.v2.model.retention_filter_without_attributes import RetentionFilterWithoutAttributes

body = ReorderRetentionFiltersRequest(
    data=[
        RetentionFilterWithoutAttributes(
            id="jdZrilSJQLqzb6Cu7aub9Q",
            type=ApmRetentionFilterType.apm_retention_filter,
        ),
        RetentionFilterWithoutAttributes(
            id="7RBOb7dLSYWI01yc3pIH8w",
            type=ApmRetentionFilterType.apm_retention_filter,
        ),
    ],
)

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = APMRetentionFiltersApi(api_client)
    api_instance.reorder_apm_retention_filters(body=body)
