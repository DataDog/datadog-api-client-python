"""
Create a RUM exclusion filter returns "Created" response
"""

from os import environ
from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.rum_retention_filters_api import RumRetentionFiltersApi
from datadog_api_client.v2.model.rum_exclusion_filter_create_attributes import RumExclusionFilterCreateAttributes
from datadog_api_client.v2.model.rum_exclusion_filter_create_data import RumExclusionFilterCreateData
from datadog_api_client.v2.model.rum_exclusion_filter_create_request import RumExclusionFilterCreateRequest
from datadog_api_client.v2.model.rum_exclusion_filter_event_type import RumExclusionFilterEventType
from datadog_api_client.v2.model.rum_exclusion_filter_type import RumExclusionFilterType

body = RumExclusionFilterCreateRequest(
    data=RumExclusionFilterCreateData(
        type=RumExclusionFilterType.EXCLUSION_FILTERS,
        attributes=RumExclusionFilterCreateAttributes(
            name="Example-Rum-Retention-Filter",
            enabled=True,
            event_type=RumExclusionFilterEventType.ERROR,
            query="@error.message:*extension*",
        ),
    ),
)

configuration = Configuration()
configuration.access_token = environ["DD_BEARER_TOKEN"]
with ApiClient(configuration) as api_client:
    api_instance = RumRetentionFiltersApi(api_client)
    response = api_instance.create_exclusion_filter(app_id="a33671aa-24fd-4dcd-ba4b-5bbdbafe7690", body=body)

    print(response)
