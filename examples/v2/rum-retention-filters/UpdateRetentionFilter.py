"""
Update a RUM retention filter returns "Updated" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.rum_retention_filters_api import RumRetentionFiltersApi
from datadog_api_client.v2.model.rum_retention_filter_event_type import RumRetentionFilterEventType
from datadog_api_client.v2.model.rum_retention_filter_type import RumRetentionFilterType
from datadog_api_client.v2.model.rum_retention_filter_update_attributes import RumRetentionFilterUpdateAttributes
from datadog_api_client.v2.model.rum_retention_filter_update_data import RumRetentionFilterUpdateData
from datadog_api_client.v2.model.rum_retention_filter_update_request import RumRetentionFilterUpdateRequest

body = RumRetentionFilterUpdateRequest(
    data=RumRetentionFilterUpdateData(
        id="4b95d361-f65d-4515-9824-c9aaeba5ac2a",
        type=RumRetentionFilterType.RETENTION_FILTERS,
        attributes=RumRetentionFilterUpdateAttributes(
            name="Test updating retention filter",
            event_type=RumRetentionFilterEventType.VIEW,
            query="view_query",
            sample_rate=100,
            enabled=True,
        ),
    ),
)

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = RumRetentionFiltersApi(api_client)
    response = api_instance.update_retention_filter(
        app_id="a33671aa-24fd-4dcd-ba4b-5bbdbafe7690", rf_id="4b95d361-f65d-4515-9824-c9aaeba5ac2a", body=body
    )

    print(response)
