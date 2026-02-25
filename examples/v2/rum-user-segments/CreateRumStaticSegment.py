"""
Create a static RUM segment returns "Created" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.rum_user_segments_api import RUMUserSegmentsApi
from datadog_api_client.v2.model.rum_static_segment_create_attributes import RumStaticSegmentCreateAttributes
from datadog_api_client.v2.model.rum_static_segment_create_data import RumStaticSegmentCreateData
from datadog_api_client.v2.model.rum_static_segment_create_request import RumStaticSegmentCreateRequest
from datadog_api_client.v2.model.rum_static_segment_journey_filter import RumStaticSegmentJourneyFilter
from datadog_api_client.v2.model.rum_static_segment_journey_node import RumStaticSegmentJourneyNode
from datadog_api_client.v2.model.rum_static_segment_journey_query_object import RumStaticSegmentJourneyQueryObject
from datadog_api_client.v2.model.rum_static_segment_request_type import RumStaticSegmentRequestType

body = RumStaticSegmentCreateRequest(
    data=RumStaticSegmentCreateData(
        attributes=RumStaticSegmentCreateAttributes(
            description="Users from a specific journey.",
            journey_query_object=RumStaticSegmentJourneyQueryObject(
                nodes=[
                    RumStaticSegmentJourneyNode(
                        filters=[
                            RumStaticSegmentJourneyFilter(
                                attribute="@type",
                                value="view",
                            ),
                        ],
                    ),
                ],
            ),
            name="My Static Segment",
            tags=[
                "team:frontend",
            ],
        ),
        type=RumStaticSegmentRequestType.CREATE_STATIC_SEGMENT_REQUEST,
    ),
)

configuration = Configuration()
configuration.unstable_operations["create_rum_static_segment"] = True
with ApiClient(configuration) as api_client:
    api_instance = RUMUserSegmentsApi(api_client)
    response = api_instance.create_rum_static_segment(body=body)

    print(response)
