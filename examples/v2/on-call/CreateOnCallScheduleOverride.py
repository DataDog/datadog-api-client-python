"""
Create an override returns "Created" response
"""

from datetime import datetime
from dateutil.relativedelta import relativedelta
from os import environ
from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.on_call_api import OnCallApi
from datadog_api_client.v2.model.on_call_user_relationship import OnCallUserRelationship
from datadog_api_client.v2.model.on_call_user_relationship_data import OnCallUserRelationshipData
from datadog_api_client.v2.model.on_call_user_relationship_type import OnCallUserRelationshipType
from datadog_api_client.v2.model.override_create_data import OverrideCreateData
from datadog_api_client.v2.model.override_create_data_attributes import OverrideCreateDataAttributes
from datadog_api_client.v2.model.override_create_data_relationships import OverrideCreateDataRelationships
from datadog_api_client.v2.model.override_create_data_type import OverrideCreateDataType
from datadog_api_client.v2.model.override_request import OverrideRequest

# there is a valid "schedule" in the system
SCHEDULE_DATA_ID = environ["SCHEDULE_DATA_ID"]

# there is a valid "user" in the system
USER_DATA_ID = environ["USER_DATA_ID"]

body = OverrideRequest(
    data=[
        OverrideCreateData(
            attributes=OverrideCreateDataAttributes(
                start=datetime.now(),
                end=(datetime.now() + relativedelta(hours=1)),
            ),
            relationships=OverrideCreateDataRelationships(
                user=OnCallUserRelationship(
                    data=OnCallUserRelationshipData(
                        id=USER_DATA_ID,
                        type=OnCallUserRelationshipType.USERS,
                    ),
                ),
            ),
            type=OverrideCreateDataType.OVERRIDES,
        ),
    ],
)

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = OnCallApi(api_client)
    response = api_instance.create_on_call_schedule_override(schedule_id=SCHEDULE_DATA_ID, body=body)

    print(response)
