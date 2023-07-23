# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from dataclasses import dataclass
from typing import List, Union, TYPE_CHECKING

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    none_type,
    unset,
    UnsetType,
)


if TYPE_CHECKING:
    from datadog_api_client.v2.model.downtime_create_request_data import DowntimeCreateRequestData
    from datadog_api_client.v2.model.downtime_monitor_identifier import DowntimeMonitorIdentifier
    from datadog_api_client.v2.model.downtime_schedule_create_request import DowntimeScheduleCreateRequest
    from datadog_api_client.v2.model.downtime_monitor_identifier_id import DowntimeMonitorIdentifierId
    from datadog_api_client.v2.model.downtime_monitor_identifier_tags import DowntimeMonitorIdentifierTags
    from datadog_api_client.v2.model.downtime_notify_end_state_types import DowntimeNotifyEndStateTypes
    from datadog_api_client.v2.model.downtime_notify_end_state_actions import DowntimeNotifyEndStateActions
    from datadog_api_client.v2.model.downtime_schedule_recurrences_create_request import (
        DowntimeScheduleRecurrencesCreateRequest,
    )
    from datadog_api_client.v2.model.downtime_schedule_one_time_create_update_request import (
        DowntimeScheduleOneTimeCreateUpdateRequest,
    )


@dataclass
class DowntimeCreateRequestJSON:
    display_timezone: Union[str, none_type, UnsetType] = unset
    message: Union[str, none_type, UnsetType] = unset
    monitor_identifier: Union[
        DowntimeMonitorIdentifier, DowntimeMonitorIdentifierId, DowntimeMonitorIdentifierTags, UnsetType
    ] = unset
    mute_first_recovery_notification: Union[bool, UnsetType] = unset
    notify_end_states: Union[List[DowntimeNotifyEndStateTypes], UnsetType] = unset
    notify_end_types: Union[List[DowntimeNotifyEndStateActions], UnsetType] = unset
    schedule: Union[
        DowntimeScheduleCreateRequest,
        DowntimeScheduleRecurrencesCreateRequest,
        DowntimeScheduleOneTimeCreateUpdateRequest,
        UnsetType,
    ] = unset
    scope: Union[str, UnsetType] = unset


class DowntimeCreateRequest(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.downtime_create_request_data import DowntimeCreateRequestData

        return {
            "data": (DowntimeCreateRequestData,),
        }

    attribute_map = {
        "data": "data",
    }
    json_api_model = DowntimeCreateRequestJSON

    def __init__(self_, data: DowntimeCreateRequestData, **kwargs):
        """
        Request for creating a downtime.

        :param data: Object to create a downtime.
        :type data: DowntimeCreateRequestData
        """
        super().__init__(kwargs)

        self_.data = data
