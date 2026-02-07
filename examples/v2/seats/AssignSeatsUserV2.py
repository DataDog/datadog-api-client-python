"""
Assign seats to users returns "Created" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.seats_api import SeatsApi
from datadog_api_client.v2.model.assign_seats_user_request import AssignSeatsUserRequest
from datadog_api_client.v2.model.assign_seats_user_request_data import AssignSeatsUserRequestData
from datadog_api_client.v2.model.assign_seats_user_request_data_attributes import AssignSeatsUserRequestDataAttributes
from datadog_api_client.v2.model.seat_assignments_data_type import SeatAssignmentsDataType

body = AssignSeatsUserRequest(
    data=AssignSeatsUserRequestData(
        attributes=AssignSeatsUserRequestDataAttributes(
            product_code="",
            user_uuids=[
                "",
            ],
        ),
        type=SeatAssignmentsDataType.SEAT_ASSIGNMENTS,
    ),
)

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = SeatsApi(api_client)
    response = api_instance.assign_seats_user_v2(body=body)

    print(response)
