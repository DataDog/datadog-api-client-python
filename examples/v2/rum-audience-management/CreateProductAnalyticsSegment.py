"""
Create a segment returns "Created" response
"""

from os import environ
from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.rum_audience_management_api import RumAudienceManagementApi
from datadog_api_client.v2.model.segment_create_attributes import SegmentCreateAttributes
from datadog_api_client.v2.model.segment_create_data import SegmentCreateData
from datadog_api_client.v2.model.segment_create_request import SegmentCreateRequest
from datadog_api_client.v2.model.segment_data_query import SegmentDataQuery
from datadog_api_client.v2.model.segment_event_platform_block import SegmentEventPlatformBlock
from datadog_api_client.v2.model.segment_resource_type import SegmentResourceType

body = SegmentCreateRequest(
    data=SegmentCreateData(
        attributes=SegmentCreateAttributes(
            data_query=SegmentDataQuery(
                event_platform=[
                    SegmentEventPlatformBlock(
                        facet="@usr.id",
                        _from="-2592000000",
                        name="viewed_logs",
                        query="@type:view @view.name:/logs",
                        to="0",
                    ),
                ],
            ),
            description="Users who viewed the logs page in the last 30 days.",
            name="High-value users",
            tags=[
                "team:growth",
            ],
        ),
        type=SegmentResourceType.SEGMENT,
    ),
)

configuration = Configuration()
configuration.access_token = environ["DD_BEARER_TOKEN"]
configuration.unstable_operations["create_product_analytics_segment"] = True
with ApiClient(configuration) as api_client:
    api_instance = RumAudienceManagementApi(api_client)
    response = api_instance.create_product_analytics_segment(body=body)

    print(response)
