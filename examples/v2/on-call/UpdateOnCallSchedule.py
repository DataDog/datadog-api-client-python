"""
Update on-call schedule returns "OK" response
"""

from datetime import datetime
from dateutil.relativedelta import relativedelta
from os import environ
from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.on_call_api import OnCallApi
from datadog_api_client.v2.model.schedule_update_request import ScheduleUpdateRequest
from datadog_api_client.v2.model.schedule_update_request_data import ScheduleUpdateRequestData
from datadog_api_client.v2.model.schedule_update_request_data_attributes import ScheduleUpdateRequestDataAttributes
from datadog_api_client.v2.model.schedule_update_request_data_attributes_layers_items import (
    ScheduleUpdateRequestDataAttributesLayersItems,
)
from datadog_api_client.v2.model.schedule_update_request_data_attributes_layers_items_interval import (
    ScheduleUpdateRequestDataAttributesLayersItemsInterval,
)
from datadog_api_client.v2.model.schedule_update_request_data_attributes_layers_items_members_items import (
    ScheduleUpdateRequestDataAttributesLayersItemsMembersItems,
)
from datadog_api_client.v2.model.schedule_update_request_data_attributes_layers_items_members_items_user import (
    ScheduleUpdateRequestDataAttributesLayersItemsMembersItemsUser,
)
from datadog_api_client.v2.model.schedule_update_request_data_attributes_layers_items_restrictions_items import (
    ScheduleUpdateRequestDataAttributesLayersItemsRestrictionsItems,
)
from datadog_api_client.v2.model.schedule_update_request_data_attributes_layers_items_restrictions_items_end_day import (
    ScheduleUpdateRequestDataAttributesLayersItemsRestrictionsItemsEndDay,
)
from datadog_api_client.v2.model.schedule_update_request_data_attributes_layers_items_restrictions_items_start_day import (
    ScheduleUpdateRequestDataAttributesLayersItemsRestrictionsItemsStartDay,
)
from datadog_api_client.v2.model.schedule_update_request_data_relationships import (
    ScheduleUpdateRequestDataRelationships,
)
from datadog_api_client.v2.model.schedule_update_request_data_relationships_teams import (
    ScheduleUpdateRequestDataRelationshipsTeams,
)
from datadog_api_client.v2.model.schedule_update_request_data_relationships_teams_data_items import (
    ScheduleUpdateRequestDataRelationshipsTeamsDataItems,
)
from datadog_api_client.v2.model.schedule_update_request_data_relationships_teams_data_items_type import (
    ScheduleUpdateRequestDataRelationshipsTeamsDataItemsType,
)
from datadog_api_client.v2.model.schedule_update_request_data_type import ScheduleUpdateRequestDataType

# there is a valid "schedule" in the system
SCHEDULE_DATA_ID = environ["SCHEDULE_DATA_ID"]
SCHEDULE_DATA_RELATIONSHIPS_LAYERS_DATA_0_ID = environ["SCHEDULE_DATA_RELATIONSHIPS_LAYERS_DATA_0_ID"]

# there is a valid "user" in the system
USER_DATA_ID = environ["USER_DATA_ID"]

# there is a valid "team" in the system
TEAM_DATA_ID = environ["TEAM_DATA_ID"]

body = ScheduleUpdateRequest(
    data=ScheduleUpdateRequestData(
        id=SCHEDULE_DATA_ID,
        attributes=ScheduleUpdateRequestDataAttributes(
            layers=[
                ScheduleUpdateRequestDataAttributesLayersItems(
                    id=SCHEDULE_DATA_RELATIONSHIPS_LAYERS_DATA_0_ID,
                    effective_date=(datetime.now() + relativedelta(days=-10)),
                    end_date=(datetime.now() + relativedelta(days=10)),
                    interval=ScheduleUpdateRequestDataAttributesLayersItemsInterval(
                        seconds=300,
                    ),
                    members=[
                        ScheduleUpdateRequestDataAttributesLayersItemsMembersItems(
                            user=ScheduleUpdateRequestDataAttributesLayersItemsMembersItemsUser(
                                id=USER_DATA_ID,
                            ),
                        ),
                    ],
                    name="Layer 1",
                    restrictions=[
                        ScheduleUpdateRequestDataAttributesLayersItemsRestrictionsItems(
                            end_day=ScheduleUpdateRequestDataAttributesLayersItemsRestrictionsItemsEndDay.FRIDAY,
                            end_time="17:00:00",
                            start_day=ScheduleUpdateRequestDataAttributesLayersItemsRestrictionsItemsStartDay.MONDAY,
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
                "tag3",
            ],
            time_zone="America/New_York",
        ),
        relationships=ScheduleUpdateRequestDataRelationships(
            teams=ScheduleUpdateRequestDataRelationshipsTeams(
                data=[
                    ScheduleUpdateRequestDataRelationshipsTeamsDataItems(
                        id=TEAM_DATA_ID,
                        type=ScheduleUpdateRequestDataRelationshipsTeamsDataItemsType.TEAMS,
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
