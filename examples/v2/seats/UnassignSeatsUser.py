"""
Unassign seats from users returns "No Content" response
"""

from os import environ
from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.seats_api import SeatsApi
from datadog_api_client.v2.model.seat_assignments_data_type import SeatAssignmentsDataType
from datadog_api_client.v2.model.unassign_seats_user_request import UnassignSeatsUserRequest
from datadog_api_client.v2.model.unassign_seats_user_request_data import UnassignSeatsUserRequestData
from datadog_api_client.v2.model.unassign_seats_user_request_data_attributes import (
    UnassignSeatsUserRequestDataAttributes,
)

# there is a valid "user" in the system
USER_DATA_ID = environ["USER_DATA_ID"]

body = UnassignSeatsUserRequest(
    data=UnassignSeatsUserRequestData(
        type=SeatAssignmentsDataType.SEAT_ASSIGNMENTS,
        attributes=UnassignSeatsUserRequestDataAttributes(
            product_code="incident_response",
            user_uuids=[
                USER_DATA_ID,
            ],
        ),
    ),
)

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = SeatsApi(api_client)
    api_instance.unassign_seats_user(body=body)
