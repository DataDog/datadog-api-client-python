"""
Create a RUM retention filter returns "Created" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.rum_retention_filters_api import RumRetentionFiltersApi
from datadog_api_client.v2.model.rum_retention_filter_create_attributes import RumRetentionFilterCreateAttributes
from datadog_api_client.v2.model.rum_retention_filter_create_data import RumRetentionFilterCreateData
from datadog_api_client.v2.model.rum_retention_filter_create_request import RumRetentionFilterCreateRequest
from datadog_api_client.v2.model.rum_retention_filter_event_type import RumRetentionFilterEventType
from datadog_api_client.v2.model.rum_retention_filter_type import RumRetentionFilterType

body = RumRetentionFilterCreateRequest(
    data=RumRetentionFilterCreateData(
        type=RumRetentionFilterType.RETENTION_FILTERS,
        attributes=RumRetentionFilterCreateAttributes(
            name="Test creating retention filter",
            event_type=RumRetentionFilterEventType.SESSION,
            query="custom_query",
            sample_rate=50,
            enabled=True,
        ),
    ),
)

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = RumRetentionFiltersApi(api_client)
    response = api_instance.create_retention_filter(app_id="a33671aa-24fd-4dcd-ba4b-5bbdbafe7690", body=body)

    print(response)
