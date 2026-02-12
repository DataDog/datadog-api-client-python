"""
Assign seats to users returns "Created" response
"""

from os import environ
from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.seats_api import SeatsApi
from datadog_api_client.v2.model.assign_seats_user_request import AssignSeatsUserRequest
from datadog_api_client.v2.model.assign_seats_user_request_data import AssignSeatsUserRequestData
from datadog_api_client.v2.model.assign_seats_user_request_data_attributes import AssignSeatsUserRequestDataAttributes
from datadog_api_client.v2.model.seat_assignments_data_type import SeatAssignmentsDataType

# there is a valid "user" in the system
USER_DATA_ID = environ["USER_DATA_ID"]

body = AssignSeatsUserRequest(
    data=AssignSeatsUserRequestData(
        type=SeatAssignmentsDataType.SEAT_ASSIGNMENTS,
        attributes=AssignSeatsUserRequestDataAttributes(
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
    response = api_instance.assign_seats_user(body=body)

    print(response)
