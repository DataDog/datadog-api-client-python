"""
Create rum segment returns "Segment created successfully" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.segments_api import SegmentsApi
from datadog_api_client.v2.model.segment import Segment
from datadog_api_client.v2.model.segment_data import SegmentData
from datadog_api_client.v2.model.segment_data_attributes import SegmentDataAttributes
from datadog_api_client.v2.model.segment_data_attributes_data_query import SegmentDataAttributesDataQuery
from datadog_api_client.v2.model.segment_data_attributes_data_query_event_platform_items import (
    SegmentDataAttributesDataQueryEventPlatformItems,
)
from datadog_api_client.v2.model.segment_data_source import SegmentDataSource
from datadog_api_client.v2.model.segment_data_type import SegmentDataType
from datetime import datetime
from dateutil.tz import tzutc

body = Segment(
    data=SegmentData(
        attributes=SegmentDataAttributes(
            created_at=datetime(1, 1, 1, 0, 0, tzinfo=tzutc()),
            created_by=SegmentDataSource(
                handle="",
                id="",
                uuid="",
            ),
            data_query=SegmentDataAttributesDataQuery(
                event_platform=[
                    SegmentDataAttributesDataQueryEventPlatformItems(
                        facet="@usr.id",
                        _from="2025-08-01",
                        name="high_value_users",
                        query="@type:view @view.name:/logs @usr.session_duration:>300000",
                        to="2025-09-01",
                    ),
                ],
            ),
            description="Users who frequently visit logs and have high session duration",
            modified_at=datetime(1, 1, 1, 0, 0, tzinfo=tzutc()),
            modified_by=SegmentDataSource(
                handle="",
                id="",
                uuid="",
            ),
            name="High-Value Users",
            org_id=123456,
            source=0,
            tags=[
                "high-value",
                "logs",
                "active",
            ],
            version=1,
        ),
        id="segment-12345",
        type=SegmentDataType.SEGMENT,
    ),
)

configuration = Configuration()
configuration.unstable_operations["create_rum_segment"] = True
with ApiClient(configuration) as api_client:
    api_instance = SegmentsApi(api_client)
    response = api_instance.create_rum_segment(body=body)

    print(response)
