"""
Update a RUM exclusion filter returns "Updated" response
"""

from os import environ
from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.rum_retention_filters_api import RUMRetentionFiltersApi
from datadog_api_client.v2.model.rum_exclusion_filter_event_type import RUMExclusionFilterEventType
from datadog_api_client.v2.model.rum_exclusion_filter_type import RUMExclusionFilterType
from datadog_api_client.v2.model.rum_exclusion_filter_update_attributes import RUMExclusionFilterUpdateAttributes
from datadog_api_client.v2.model.rum_exclusion_filter_update_data import RUMExclusionFilterUpdateData
from datadog_api_client.v2.model.rum_exclusion_filter_update_request import RUMExclusionFilterUpdateRequest

body = RUMExclusionFilterUpdateRequest(
    data=RUMExclusionFilterUpdateData(
        attributes=RUMExclusionFilterUpdateAttributes(
            enabled=True,
            event_type=RUMExclusionFilterEventType.ERROR,
            name="Exclude noisy browser extension errors",
            query="@error.message:*extension*",
        ),
        id="051601eb-54a0-abc0-03f9-cc02efa18892",
        type=RUMExclusionFilterType.EXCLUSION_FILTERS,
    ),
)

configuration = Configuration()
configuration.access_token = environ["DD_BEARER_TOKEN"]
with ApiClient(configuration) as api_client:
    api_instance = RUMRetentionFiltersApi(api_client)
    response = api_instance.update_exclusion_filter(app_id="app_id", ef_id="ef_id", body=body)

    print(response)
