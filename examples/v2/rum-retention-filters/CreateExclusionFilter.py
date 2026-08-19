"""
Create a RUM exclusion filter returns "Created" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.rum_retention_filters_api import RumRetentionFiltersApi
from datadog_api_client.v2.model.rum_exclusion_filter_create_attributes import RumExclusionFilterCreateAttributes
from datadog_api_client.v2.model.rum_exclusion_filter_create_data import RumExclusionFilterCreateData
from datadog_api_client.v2.model.rum_exclusion_filter_create_request import RumExclusionFilterCreateRequest
from datadog_api_client.v2.model.rum_exclusion_filter_event_type import RumExclusionFilterEventType
from datadog_api_client.v2.model.rum_exclusion_filter_type import RumExclusionFilterType

body = RumExclusionFilterCreateRequest(
    data=RumExclusionFilterCreateData(
        attributes=RumExclusionFilterCreateAttributes(
            enabled=True,
            event_type=RumExclusionFilterEventType.ERROR,
            name="Exclude noisy browser extension errors",
            query="@error.message:*extension*",
        ),
        type=RumExclusionFilterType.EXCLUSION_FILTERS,
    ),
)

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = RumRetentionFiltersApi(api_client)
    response = api_instance.create_exclusion_filter(app_id="app_id", body=body)

    print(response)
