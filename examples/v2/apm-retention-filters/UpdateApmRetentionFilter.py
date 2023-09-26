"""
Update a retention filter returns "OK" response
"""

from os import environ
from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.apm_retention_filters_api import APMRetentionFiltersApi
from datadog_api_client.v2.model.apm_retention_filter_type import ApmRetentionFilterType
from datadog_api_client.v2.model.retention_filter_create_attributes import RetentionFilterCreateAttributes
from datadog_api_client.v2.model.retention_filter_type import RetentionFilterType
from datadog_api_client.v2.model.retention_filter_update_data import RetentionFilterUpdateData
from datadog_api_client.v2.model.retention_filter_update_request import RetentionFilterUpdateRequest
from datadog_api_client.v2.model.spans_filter_create import SpansFilterCreate

# there is a valid "retention_filter" in the system
RETENTION_FILTER_DATA_ID = environ["RETENTION_FILTER_DATA_ID"]

body = RetentionFilterUpdateRequest(
    data=RetentionFilterUpdateData(
        attributes=RetentionFilterCreateAttributes(
            name="test",
            rate=0.9,
            filter=SpansFilterCreate(
                query="@_top_level:1 test:service-demo",
            ),
            enabled=True,
            filter_type=RetentionFilterType.SPANS_SAMPLING_PROCESSOR,
        ),
        id="test-id",
        type=ApmRetentionFilterType.apm_retention_filter,
    ),
)

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = APMRetentionFiltersApi(api_client)
    response = api_instance.update_apm_retention_filter(filter_id=RETENTION_FILTER_DATA_ID, body=body)

    print(response)
