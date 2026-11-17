"""
Update a segment returns "No Content" response
"""

from os import environ
from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.rum_audience_management_api import RumAudienceManagementApi
from datadog_api_client.v2.model.segment_resource_type import SegmentResourceType
from datadog_api_client.v2.model.segment_update_attributes import SegmentUpdateAttributes
from datadog_api_client.v2.model.segment_update_data import SegmentUpdateData
from datadog_api_client.v2.model.segment_update_request import SegmentUpdateRequest

body = SegmentUpdateRequest(
    data=SegmentUpdateData(
        attributes=SegmentUpdateAttributes(
            description="Users who viewed the logs page in the last 7 days.",
            name="High-value users",
        ),
        id="8a1b2c3d-4e5f-6a7b-8c9d-0e1f2a3b4c5d",
        type=SegmentResourceType.SEGMENT,
    ),
)

configuration = Configuration()
configuration.access_token = environ["DD_BEARER_TOKEN"]
configuration.unstable_operations["update_product_analytics_segment"] = True
with ApiClient(configuration) as api_client:
    api_instance = RumAudienceManagementApi(api_client)
    api_instance.update_product_analytics_segment(id="8a1b2c3d-4e5f-6a7b-8c9d-0e1f2a3b4c5d", body=body)
