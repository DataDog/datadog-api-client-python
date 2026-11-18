"""
Preview a segment returns "OK" response
"""

from os import environ
from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.rum_audience_management_api import RumAudienceManagementApi
from datadog_api_client.v2.model.segment_data_query import SegmentDataQuery
from datadog_api_client.v2.model.segment_event_platform_block import SegmentEventPlatformBlock
from datadog_api_client.v2.model.segment_preview_attributes import SegmentPreviewAttributes
from datadog_api_client.v2.model.segment_preview_data import SegmentPreviewData
from datadog_api_client.v2.model.segment_preview_request import SegmentPreviewRequest
from datadog_api_client.v2.model.segment_preview_request_type import SegmentPreviewRequestType

body = SegmentPreviewRequest(
    data=SegmentPreviewData(
        attributes=SegmentPreviewAttributes(
            data_query=SegmentDataQuery(
                event_platform=[
                    SegmentEventPlatformBlock(
                        facet="@usr.id",
                        _from="-2592000000",
                        query="@type:view @view.name:/logs",
                        to="0",
                    ),
                ],
            ),
            limit=50,
            user_store_columns=[
                "user_id",
                "user_email",
                "user_name",
            ],
        ),
        type=SegmentPreviewRequestType.SEGMENT_PREVIEW_REQUEST,
    ),
)

configuration = Configuration()
configuration.access_token = environ["DD_BEARER_TOKEN"]
configuration.unstable_operations["preview_product_analytics_segment"] = True
with ApiClient(configuration) as api_client:
    api_instance = RumAudienceManagementApi(api_client)
    response = api_instance.preview_product_analytics_segment(body=body)

    print(response)
