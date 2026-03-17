"""
Update a RUM segment returns "No Content" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.rum_user_segments_api import RUMUserSegmentsApi
from datadog_api_client.v2.model.rum_segment_data_query import RumSegmentDataQuery
from datadog_api_client.v2.model.rum_segment_event_platform import RumSegmentEventPlatform
from datadog_api_client.v2.model.rum_segment_journey import RumSegmentJourney
from datadog_api_client.v2.model.rum_segment_reference_table import RumSegmentReferenceTable
from datadog_api_client.v2.model.rum_segment_reference_table_column import RumSegmentReferenceTableColumn
from datadog_api_client.v2.model.rum_segment_reference_table_join_condition import RumSegmentReferenceTableJoinCondition
from datadog_api_client.v2.model.rum_segment_resource_type import RumSegmentResourceType
from datadog_api_client.v2.model.rum_segment_static_entry import RumSegmentStaticEntry
from datadog_api_client.v2.model.rum_segment_template_instance import RumSegmentTemplateInstance
from datadog_api_client.v2.model.rum_segment_update_attributes import RumSegmentUpdateAttributes
from datadog_api_client.v2.model.rum_segment_update_data import RumSegmentUpdateData
from datadog_api_client.v2.model.rum_segment_update_request import RumSegmentUpdateRequest

body = RumSegmentUpdateRequest(
    data=RumSegmentUpdateData(
        attributes=RumSegmentUpdateAttributes(
            data_query=RumSegmentDataQuery(
                combination="(logs && apm_home) && NOT(apm_trace)",
                event_platforms=[
                    RumSegmentEventPlatform(
                        facet="@usr.id",
                        _from=1709888355000,
                        name="logs",
                        query="@type:view @view.url_path:/logs",
                        to=1710493155000,
                    ),
                ],
                journeys=[
                    RumSegmentJourney(
                        conversion_type="any",
                        group_by="@usr.id",
                        name="my_journey",
                        search="@type:view",
                    ),
                ],
                reference_tables=[
                    RumSegmentReferenceTable(
                        columns=[
                            RumSegmentReferenceTableColumn(
                                name="user_id",
                            ),
                        ],
                        filter_query="",
                        join_condition=RumSegmentReferenceTableJoinCondition(
                            column_name="user_id",
                            facet="@usr.id",
                        ),
                        name="my_ref_table",
                        table_name="my_table",
                    ),
                ],
                static=[
                    RumSegmentStaticEntry(
                        id="static-list-1",
                        name="My Static List",
                        user_count=500,
                    ),
                ],
                templates=[
                    RumSegmentTemplateInstance(
                        _from=1709888355000,
                        parameters=dict(
                            threshold="5",
                        ),
                        template_id="stickiness-v1",
                        to=1710493155000,
                    ),
                ],
            ),
            description="Updated description.",
            name="Updated Segment Name",
            tags=[
                "team:backend",
            ],
        ),
        id="a1b2c3d4-1234-5678-9abc-123456789abc",
        type=RumSegmentResourceType.SEGMENT,
    ),
)

configuration = Configuration()
configuration.unstable_operations["update_rum_segment"] = True
with ApiClient(configuration) as api_client:
    api_instance = RUMUserSegmentsApi(api_client)
    api_instance.update_rum_segment(segment_id="a1b2c3d4-1234-5678-9abc-123456789abc", body=body)
