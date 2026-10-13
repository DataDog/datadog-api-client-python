"""
Create On-Call schedule overrides returns "Created" response
"""

from datetime import datetime
from dateutil.relativedelta import relativedelta
from os import environ
from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.on_call_api import OnCallApi
from datadog_api_client.v2.model.create_override_request_attributes import CreateOverrideRequestAttributes
from datadog_api_client.v2.model.create_override_request_data import CreateOverrideRequestData
from datadog_api_client.v2.model.create_override_request_relationships import CreateOverrideRequestRelationships
from datadog_api_client.v2.model.create_overrides_request import CreateOverridesRequest
from datadog_api_client.v2.model.override_data_type import OverrideDataType
from datadog_api_client.v2.model.override_relationships_user import OverrideRelationshipsUser
from datadog_api_client.v2.model.override_relationships_user_data import OverrideRelationshipsUserData
from datadog_api_client.v2.model.override_relationships_user_data_type import OverrideRelationshipsUserDataType

# there is a valid "schedule" in the system
SCHEDULE_DATA_ID = environ["SCHEDULE_DATA_ID"]

# there is a valid "user" in the system
USER_DATA_ID = environ["USER_DATA_ID"]

body = CreateOverridesRequest(
    data=[
        CreateOverrideRequestData(
            attributes=CreateOverrideRequestAttributes(
                end=(datetime.now() + relativedelta(days=1)),
                start=datetime.now(),
            ),
            relationships=CreateOverrideRequestRelationships(
                user=OverrideRelationshipsUser(
                    data=OverrideRelationshipsUserData(
                        id=USER_DATA_ID,
                        type=OverrideRelationshipsUserDataType.USERS,
                    ),
                ),
            ),
            type=OverrideDataType.OVERRIDES,
        ),
    ],
)

configuration = Configuration()
configuration.access_token = environ["DD_BEARER_TOKEN"]
with ApiClient(configuration) as api_client:
    api_instance = OnCallApi(api_client)
    response = api_instance.create_schedule_overrides(schedule_id=SCHEDULE_DATA_ID, body=body)

    print(response)
