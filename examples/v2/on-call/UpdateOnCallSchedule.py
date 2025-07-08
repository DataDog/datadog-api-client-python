"""
Update On-Call schedule returns "OK" response
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
from datadog_api_client.v2.model.schedule_request_data_attributes_layers_items_members_items import (
    ScheduleRequestDataAttributesLayersItemsMembersItems,
)
from datadog_api_client.v2.model.schedule_request_data_attributes_layers_items_members_items_user import (
    ScheduleRequestDataAttributesLayersItemsMembersItemsUser,
)
from datadog_api_client.v2.model.schedule_update_request import ScheduleUpdateRequest
from datadog_api_client.v2.model.schedule_update_request_data import ScheduleUpdateRequestData
from datadog_api_client.v2.model.schedule_update_request_data_attributes import ScheduleUpdateRequestDataAttributes
from datadog_api_client.v2.model.schedule_update_request_data_attributes_layers_items import (
    ScheduleUpdateRequestDataAttributesLayersItems,
)
from datadog_api_client.v2.model.schedule_update_request_data_relationships import (
    ScheduleUpdateRequestDataRelationships,
)
from datadog_api_client.v2.model.schedule_update_request_data_type import ScheduleUpdateRequestDataType
from datadog_api_client.v2.model.time_restriction import TimeRestriction
from datadog_api_client.v2.model.weekday import Weekday

# there is a valid "schedule" in the system
SCHEDULE_DATA_ID = environ["SCHEDULE_DATA_ID"]
SCHEDULE_DATA_RELATIONSHIPS_LAYERS_DATA_0_ID = environ["SCHEDULE_DATA_RELATIONSHIPS_LAYERS_DATA_0_ID"]

# there is a valid "user" in the system
USER_DATA_ID = environ["USER_DATA_ID"]

# there is a valid "dd_team" in the system
DD_TEAM_DATA_ID = environ["DD_TEAM_DATA_ID"]

body = ScheduleUpdateRequest(
    data=ScheduleUpdateRequestData(
        id=SCHEDULE_DATA_ID,
        attributes=ScheduleUpdateRequestDataAttributes(
            layers=[
                ScheduleUpdateRequestDataAttributesLayersItems(
                    id=SCHEDULE_DATA_RELATIONSHIPS_LAYERS_DATA_0_ID,
                    effective_date=(datetime.now() + relativedelta(days=-10)),
                    end_date=(datetime.now() + relativedelta(days=10)),
                    interval=LayerAttributesInterval(
                        seconds=3600,
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
        relationships=ScheduleUpdateRequestDataRelationships(
            teams=DataRelationshipsTeams(
                data=[
                    DataRelationshipsTeamsDataItems(
                        id=DD_TEAM_DATA_ID,
                        type=DataRelationshipsTeamsDataItemsType.TEAMS,
                    ),
                ],
            ),
        ),
        type=ScheduleUpdateRequestDataType.SCHEDULES,
    ),
)

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = OnCallApi(api_client)
    response = api_instance.update_on_call_schedule(schedule_id=SCHEDULE_DATA_ID, body=body)

    print(response)
