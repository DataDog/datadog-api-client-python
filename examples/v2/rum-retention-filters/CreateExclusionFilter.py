"""
Create a RUM exclusion filter returns "Created" response
"""

from os import environ
from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.rum_retention_filters_api import RUMRetentionFiltersApi
from datadog_api_client.v2.model.rum_exclusion_filter_create_attributes import RUMExclusionFilterCreateAttributes
from datadog_api_client.v2.model.rum_exclusion_filter_create_data import RUMExclusionFilterCreateData
from datadog_api_client.v2.model.rum_exclusion_filter_create_request import RUMExclusionFilterCreateRequest
from datadog_api_client.v2.model.rum_exclusion_filter_event_type import RUMExclusionFilterEventType
from datadog_api_client.v2.model.rum_exclusion_filter_type import RUMExclusionFilterType

body = RUMExclusionFilterCreateRequest(
    data=RUMExclusionFilterCreateData(
        attributes=RUMExclusionFilterCreateAttributes(
            enabled=True,
            event_type=RUMExclusionFilterEventType.ERROR,
            name="Exclude noisy browser extension errors",
            query="@error.message:*extension*",
        ),
        type=RUMExclusionFilterType.EXCLUSION_FILTERS,
    ),
)

configuration = Configuration()
configuration.access_token = environ["DD_BEARER_TOKEN"]
with ApiClient(configuration) as api_client:
    api_instance = RUMRetentionFiltersApi(api_client)
    response = api_instance.create_exclusion_filter(app_id="app_id", body=body)

    print(response)
