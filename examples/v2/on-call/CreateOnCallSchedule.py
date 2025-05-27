"""
Create On-Call schedule returns "Created" response
"""

from datetime import datetime
from dateutil.relativedelta import relativedelta
from os import environ
from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.on_call_api import OnCallApi
from datadog_api_client.v2.model.data_relationships_teams import DataRelationshipsTeams
from datadog_api_client.v2.model.data_relationships_teams_data_items import DataRelationshipsTeamsDataItems
from datadog_api_client.v2.model.data_relationships_teams_data_items_type import DataRelationshipsTeamsDataItemsType
from datadog_api_client.v2.model.layer_attributes_interval import LayerAttributesInterval
from datadog_api_client.v2.model.schedule_create_request import ScheduleCreateRequest
from datadog_api_client.v2.model.schedule_create_request_data import ScheduleCreateRequestData
from datadog_api_client.v2.model.schedule_create_request_data_attributes import ScheduleCreateRequestDataAttributes
from datadog_api_client.v2.model.schedule_create_request_data_attributes_layers_items import (
    ScheduleCreateRequestDataAttributesLayersItems,
)
from datadog_api_client.v2.model.schedule_create_request_data_relationships import (
    ScheduleCreateRequestDataRelationships,
)
from datadog_api_client.v2.model.schedule_create_request_data_type import ScheduleCreateRequestDataType
from datadog_api_client.v2.model.schedule_request_data_attributes_layers_items_members_items import (
    ScheduleRequestDataAttributesLayersItemsMembersItems,
)
from datadog_api_client.v2.model.schedule_request_data_attributes_layers_items_members_items_user import (
    ScheduleRequestDataAttributesLayersItemsMembersItemsUser,
)
from datadog_api_client.v2.model.time_restriction import TimeRestriction
from datadog_api_client.v2.model.weekday import Weekday

# there is a valid "user" in the system
USER_DATA_ID = environ["USER_DATA_ID"]

# there is a valid "dd_team" in the system
DD_TEAM_DATA_ID = environ["DD_TEAM_DATA_ID"]

body = ScheduleCreateRequest(
    data=ScheduleCreateRequestData(
        attributes=ScheduleCreateRequestDataAttributes(
            layers=[
                ScheduleCreateRequestDataAttributesLayersItems(
                    effective_date=(datetime.now() + relativedelta(days=-10)),
                    end_date=(datetime.now() + relativedelta(days=10)),
                    interval=LayerAttributesInterval(
                        days=1,
                    ),
                    members=[
                        ScheduleRequestDataAttributesLayersItemsMembersItems(
                            user=ScheduleRequestDataAttributesLayersItemsMembersItemsUser(
                                id=USER_DATA_ID,
                            ),
                        ),
                    ],
                    name="Layer 1",
                    restrictions=[
                        TimeRestriction(
                            end_day=Weekday.FRIDAY,
                            end_time="17:00:00",
                            start_day=Weekday.MONDAY,
                            start_time="09:00:00",
                        ),
                    ],
                    rotation_start=(datetime.now() + relativedelta(days=-5)),
                ),
            ],
            name="Example-On-Call",
            time_zone="America/New_York",
        ),
        relationships=ScheduleCreateRequestDataRelationships(
            teams=DataRelationshipsTeams(
                data=[
                    DataRelationshipsTeamsDataItems(
                        id=DD_TEAM_DATA_ID,
                        type=DataRelationshipsTeamsDataItemsType.TEAMS,
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
