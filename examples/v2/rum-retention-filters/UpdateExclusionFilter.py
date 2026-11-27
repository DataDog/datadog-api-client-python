"""
Update a RUM exclusion filter returns "Updated" response
"""

from os import environ
from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.rum_retention_filters_api import RumRetentionFiltersApi
from datadog_api_client.v2.model.rum_exclusion_filter_type import RumExclusionFilterType
from datadog_api_client.v2.model.rum_exclusion_filter_update_attributes import RumExclusionFilterUpdateAttributes
from datadog_api_client.v2.model.rum_exclusion_filter_update_data import RumExclusionFilterUpdateData
from datadog_api_client.v2.model.rum_exclusion_filter_update_request import RumExclusionFilterUpdateRequest

# there is a valid "rum_exclusion_filter" in the system
RUM_EXCLUSION_FILTER_DATA_ID = environ["RUM_EXCLUSION_FILTER_DATA_ID"]

body = RumExclusionFilterUpdateRequest(
    data=RumExclusionFilterUpdateData(
        id=RUM_EXCLUSION_FILTER_DATA_ID,
        type=RumExclusionFilterType.EXCLUSION_FILTERS,
        attributes=RumExclusionFilterUpdateAttributes(
            enabled=False,
            name="Example-Rum-Retention-Filter-updated",
        ),
    ),
)

configuration = Configuration()
configuration.access_token = environ["DD_BEARER_TOKEN"]
with ApiClient(configuration) as api_client:
    api_instance = RumRetentionFiltersApi(api_client)
    response = api_instance.update_exclusion_filter(
        app_id="a33671aa-24fd-4dcd-ba4b-5bbdbafe7690", ef_id=RUM_EXCLUSION_FILTER_DATA_ID, body=body
    )

    print(response)
