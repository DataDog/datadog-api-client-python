"""
Update a RUM retention filter returns "Updated" response
"""

from os import environ
from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.rum_retention_filters_api import RUMRetentionFiltersApi
from datadog_api_client.v2.model.rum_retention_filter_event_type import RUMRetentionFilterEventType
from datadog_api_client.v2.model.rum_retention_filter_type import RUMRetentionFilterType
from datadog_api_client.v2.model.rum_retention_filter_update_attributes import RUMRetentionFilterUpdateAttributes
from datadog_api_client.v2.model.rum_retention_filter_update_data import RUMRetentionFilterUpdateData
from datadog_api_client.v2.model.rum_retention_filter_update_request import RUMRetentionFilterUpdateRequest

body = RUMRetentionFilterUpdateRequest(
    data=RUMRetentionFilterUpdateData(
        id="4b95d361-f65d-4515-9824-c9aaeba5ac2a",
        type=RUMRetentionFilterType.RETENTION_FILTERS,
        attributes=RUMRetentionFilterUpdateAttributes(
            name="Test updating retention filter",
            event_type=RUMRetentionFilterEventType.VIEW,
            query="view_query",
            sample_rate=100.0,
            enabled=True,
        ),
    ),
)

configuration = Configuration()
configuration.access_token = environ["DD_BEARER_TOKEN"]
with ApiClient(configuration) as api_client:
    api_instance = RUMRetentionFiltersApi(api_client)
    response = api_instance.update_retention_filter(
        app_id="a33671aa-24fd-4dcd-ba4b-5bbdbafe7690", rf_id="4b95d361-f65d-4515-9824-c9aaeba5ac2a", body=body
    )

    print(response)
