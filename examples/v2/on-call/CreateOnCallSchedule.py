"""
Create on-call schedule returns "Created" response
"""

from datetime import datetime
from dateutil.relativedelta import relativedelta
from os import environ
from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.on_call_api import OnCallApi
from datadog_api_client.v2.model.schedule_create_request import ScheduleCreateRequest
from datadog_api_client.v2.model.schedule_create_request_data import ScheduleCreateRequestData
from datadog_api_client.v2.model.schedule_create_request_data_attributes import ScheduleCreateRequestDataAttributes
from datadog_api_client.v2.model.schedule_create_request_data_attributes_layers_items import (
    ScheduleCreateRequestDataAttributesLayersItems,
)
from datadog_api_client.v2.model.schedule_create_request_data_attributes_layers_items_interval import (
    ScheduleCreateRequestDataAttributesLayersItemsInterval,
)
from datadog_api_client.v2.model.schedule_create_request_data_attributes_layers_items_members_items import (
    ScheduleCreateRequestDataAttributesLayersItemsMembersItems,
)
from datadog_api_client.v2.model.schedule_create_request_data_attributes_layers_items_members_items_user import (
    ScheduleCreateRequestDataAttributesLayersItemsMembersItemsUser,
)
from datadog_api_client.v2.model.schedule_create_request_data_attributes_layers_items_restrictions_items import (
    ScheduleCreateRequestDataAttributesLayersItemsRestrictionsItems,
)
from datadog_api_client.v2.model.schedule_create_request_data_attributes_layers_items_restrictions_items_end_day import (
    ScheduleCreateRequestDataAttributesLayersItemsRestrictionsItemsEndDay,
)
from datadog_api_client.v2.model.schedule_create_request_data_attributes_layers_items_restrictions_items_start_day import (
    ScheduleCreateRequestDataAttributesLayersItemsRestrictionsItemsStartDay,
)
from datadog_api_client.v2.model.schedule_create_request_data_relationships import (
    ScheduleCreateRequestDataRelationships,
)
from datadog_api_client.v2.model.schedule_create_request_data_relationships_teams import (
    ScheduleCreateRequestDataRelationshipsTeams,
)
from datadog_api_client.v2.model.schedule_create_request_data_relationships_teams_data_items import (
    ScheduleCreateRequestDataRelationshipsTeamsDataItems,
)
from datadog_api_client.v2.model.schedule_create_request_data_relationships_teams_data_items_type import (
    ScheduleCreateRequestDataRelationshipsTeamsDataItemsType,
)
from datadog_api_client.v2.model.schedule_create_request_data_type import ScheduleCreateRequestDataType

# there is a valid "user" in the system
USER_DATA_ID = environ["USER_DATA_ID"]

# there is a valid "team" in the system
TEAM_DATA_ID = environ["TEAM_DATA_ID"]

body = ScheduleCreateRequest(
    data=ScheduleCreateRequestData(
        attributes=ScheduleCreateRequestDataAttributes(
            layers=[
                ScheduleCreateRequestDataAttributesLayersItems(
                    effective_date=(datetime.now() + relativedelta(days=-10)),
                    end_date=(datetime.now() + relativedelta(days=10)),
                    interval=ScheduleCreateRequestDataAttributesLayersItemsInterval(
                        days=1,
                    ),
                    members=[
                        ScheduleCreateRequestDataAttributesLayersItemsMembersItems(
                            user=ScheduleCreateRequestDataAttributesLayersItemsMembersItemsUser(
                                id=USER_DATA_ID,
                            ),
                        ),
                    ],
                    name="Layer 1",
                    restrictions=[
                        ScheduleCreateRequestDataAttributesLayersItemsRestrictionsItems(
                            end_day=ScheduleCreateRequestDataAttributesLayersItemsRestrictionsItemsEndDay.FRIDAY,
                            end_time="17:00:00",
                            start_day=ScheduleCreateRequestDataAttributesLayersItemsRestrictionsItemsStartDay.MONDAY,
                            start_time="09:00:00",
                        ),
                    ],
                    rotation_start=(datetime.now() + relativedelta(days=-5)),
                ),
            ],
            name="Example-On-Call",
            tags=[
                "tag1",
                "tag2",
            ],
            time_zone="America/New_York",
        ),
        relationships=ScheduleCreateRequestDataRelationships(
            teams=ScheduleCreateRequestDataRelationshipsTeams(
                data=[
                    ScheduleCreateRequestDataRelationshipsTeamsDataItems(
                        id=TEAM_DATA_ID,
                        type=ScheduleCreateRequestDataRelationshipsTeamsDataItemsType.TEAMS,
                    ),
                ],
            ),
        ),
        type=ScheduleCreateRequestDataType.SCHEDULES,
    ),
)

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = OnCallApi(api_client)
    response = api_instance.create_on_call_schedule(body=body)

    print(response)
