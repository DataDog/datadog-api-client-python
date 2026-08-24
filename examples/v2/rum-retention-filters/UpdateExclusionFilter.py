"""
Update a RUM exclusion filter returns "Updated" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.rum_retention_filters_api import RumRetentionFiltersApi
from datadog_api_client.v2.model.rum_exclusion_filter_event_type import RumExclusionFilterEventType
from datadog_api_client.v2.model.rum_exclusion_filter_type import RumExclusionFilterType
from datadog_api_client.v2.model.rum_exclusion_filter_update_attributes import RumExclusionFilterUpdateAttributes
from datadog_api_client.v2.model.rum_exclusion_filter_update_data import RumExclusionFilterUpdateData
from datadog_api_client.v2.model.rum_exclusion_filter_update_request import RumExclusionFilterUpdateRequest

body = RumExclusionFilterUpdateRequest(
    data=RumExclusionFilterUpdateData(
        attributes=RumExclusionFilterUpdateAttributes(
            enabled=True,
            event_type=RumExclusionFilterEventType.ERROR,
            name="Exclude noisy browser extension errors",
            query="@error.message:*extension*",
        ),
        id="051601eb-54a0-abc0-03f9-cc02efa18892",
        type=RumExclusionFilterType.EXCLUSION_FILTERS,
    ),
)

configuration = Configuration()
configuration.unstable_operations["update_exclusion_filter"] = True
with ApiClient(configuration) as api_client:
    api_instance = RumRetentionFiltersApi(api_client)
    response = api_instance.update_exclusion_filter(app_id="app_id", ef_id="ef_id", body=body)

    print(response)
