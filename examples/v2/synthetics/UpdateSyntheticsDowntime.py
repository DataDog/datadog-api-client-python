"""
Update a Synthetics downtime returns "OK" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.synthetics_api import SyntheticsApi
from datadog_api_client.v2.model.synthetics_downtime_data_attributes_request import (
    SyntheticsDowntimeDataAttributesRequest,
)
from datadog_api_client.v2.model.synthetics_downtime_data_request import SyntheticsDowntimeDataRequest
from datadog_api_client.v2.model.synthetics_downtime_request import SyntheticsDowntimeRequest
from datadog_api_client.v2.model.synthetics_downtime_resource_type import SyntheticsDowntimeResourceType
from datadog_api_client.v2.model.synthetics_downtime_time_slot_date import SyntheticsDowntimeTimeSlotDate
from datadog_api_client.v2.model.synthetics_downtime_time_slot_request import SyntheticsDowntimeTimeSlotRequest

body = SyntheticsDowntimeRequest(
    data=SyntheticsDowntimeDataRequest(
        attributes=SyntheticsDowntimeDataAttributesRequest(
            is_enabled=True,
            name="Weekly maintenance",
            test_ids=[
                "abc-def-123",
            ],
            time_slots=[
                SyntheticsDowntimeTimeSlotRequest(
                    duration=3600,
                    start=SyntheticsDowntimeTimeSlotDate(
                        day=15,
                        hour=10,
                        minute=30,
                        month=1,
                        year=2024,
                    ),
                    timezone="Europe/Paris",
                ),
            ],
        ),
        type=SyntheticsDowntimeResourceType.DOWNTIME,
    ),
)

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = SyntheticsApi(api_client)
    response = api_instance.update_synthetics_downtime(downtime_id="00000000-0000-0000-0000-000000000001", body=body)

    print(response)
