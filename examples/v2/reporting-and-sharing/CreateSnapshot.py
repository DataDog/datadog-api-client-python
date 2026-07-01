"""
Create a graph snapshot returns "OK" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.reportingand_sharing_api import ReportingandSharingApi
from datadog_api_client.v2.model.create_snapshot_additional_config import CreateSnapshotAdditionalConfig
from datadog_api_client.v2.model.create_snapshot_data_attributes_request import CreateSnapshotDataAttributesRequest
from datadog_api_client.v2.model.create_snapshot_data_request import CreateSnapshotDataRequest
from datadog_api_client.v2.model.create_snapshot_request import CreateSnapshotRequest
from datadog_api_client.v2.model.create_snapshot_template_variable import CreateSnapshotTemplateVariable
from datadog_api_client.v2.model.create_snapshot_timeseries_legend_type import CreateSnapshotTimeseriesLegendType
from datadog_api_client.v2.model.create_snapshot_ttl import CreateSnapshotTTL
from datadog_api_client.v2.model.create_snapshot_type import CreateSnapshotType

body = CreateSnapshotRequest(
    data=CreateSnapshotDataRequest(
        attributes=CreateSnapshotDataAttributesRequest(
            additional_config=CreateSnapshotAdditionalConfig(
                template_variables=[
                    CreateSnapshotTemplateVariable(
                        name="host",
                        prefix="host",
                        values=[
                            "web-server-1",
                            "web-server-2",
                        ],
                    ),
                ],
                timeseries_legend_type=CreateSnapshotTimeseriesLegendType.EXPANDED,
                timezone_offset_minutes=300,
            ),
            end=1692464800000,
            height=185,
            is_authenticated=False,
            start=1692464000000,
            ttl=CreateSnapshotTTL.SIXTY_DAYS,
            widget_definition=dict([("requests", "[{'q': 'avg:system.cpu.user{*}'}]"), ("type", "timeseries")]),
            width=300,
        ),
        type=CreateSnapshotType.CREATE_SNAPSHOT,
    ),
)

configuration = Configuration()
configuration.unstable_operations["create_snapshot"] = True
with ApiClient(configuration) as api_client:
    api_instance = ReportingandSharingApi(api_client)
    response = api_instance.create_snapshot(body=body)

    print(response)
