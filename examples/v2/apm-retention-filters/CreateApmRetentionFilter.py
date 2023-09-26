"""
Create a retention filter returns "OK" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.apm_retention_filters_api import APMRetentionFiltersApi
from datadog_api_client.v2.model.apm_retention_filter_type import ApmRetentionFilterType
from datadog_api_client.v2.model.retention_filter_create_attributes import RetentionFilterCreateAttributes
from datadog_api_client.v2.model.retention_filter_create_data import RetentionFilterCreateData
from datadog_api_client.v2.model.retention_filter_create_request import RetentionFilterCreateRequest
from datadog_api_client.v2.model.retention_filter_type import RetentionFilterType
from datadog_api_client.v2.model.spans_filter_create import SpansFilterCreate

body = RetentionFilterCreateRequest(
    data=RetentionFilterCreateData(
        attributes=RetentionFilterCreateAttributes(
            enabled=True,
            filter=SpansFilterCreate(
                query="@http.status_code:200 service:my-service",
            ),
            filter_type=RetentionFilterType.SPANS_SAMPLING_PROCESSOR,
            name="my retention filter",
            rate=1.0,
        ),
        type=ApmRetentionFilterType.apm_retention_filter,
    ),
)

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = APMRetentionFiltersApi(api_client)
    response = api_instance.create_apm_retention_filter(body=body)

    print(response)
