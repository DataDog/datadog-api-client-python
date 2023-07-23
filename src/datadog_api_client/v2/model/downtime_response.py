# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from dataclasses import dataclass
from typing import List, Union, TYPE_CHECKING

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    datetime,
    none_type,
    unset,
    UnsetType,
)


if TYPE_CHECKING:
    from datadog_api_client.v2.model.downtime_response_data import DowntimeResponseData
    from datadog_api_client.v2.model.downtime_response_included_item import DowntimeResponseIncludedItem
    from datadog_api_client.v2.model.user import User
    from datadog_api_client.v2.model.downtime_monitor_included_item import DowntimeMonitorIncludedItem
    from datadog_api_client.v2.model.downtime_monitor_identifier import DowntimeMonitorIdentifier
    from datadog_api_client.v2.model.downtime_schedule_response import DowntimeScheduleResponse
    from datadog_api_client.v2.model.downtime_status import DowntimeStatus
    from datadog_api_client.v2.model.downtime_monitor_identifier_id import DowntimeMonitorIdentifierId
    from datadog_api_client.v2.model.downtime_monitor_identifier_tags import DowntimeMonitorIdentifierTags
    from datadog_api_client.v2.model.downtime_notify_end_state_types import DowntimeNotifyEndStateTypes
    from datadog_api_client.v2.model.downtime_notify_end_state_actions import DowntimeNotifyEndStateActions
    from datadog_api_client.v2.model.downtime_schedule_recurrences_response import DowntimeScheduleRecurrencesResponse
    from datadog_api_client.v2.model.downtime_schedule_one_time_response import DowntimeScheduleOneTimeResponse


@dataclass
class DowntimeResponseJSON:
    id: str
    created_at: Union[datetime, UnsetType] = unset
    display_timezone: Union[str, none_type, UnsetType] = unset
    message: Union[str, none_type, UnsetType] = unset
    modified_at: Union[datetime, UnsetType] = unset
    monitor_identifier: Union[
        DowntimeMonitorIdentifier, DowntimeMonitorIdentifierId, DowntimeMonitorIdentifierTags, UnsetType
    ] = unset
    mute_first_recovery_notification: Union[bool, UnsetType] = unset
    notify_end_states: Union[List[DowntimeNotifyEndStateTypes], UnsetType] = unset
    notify_end_types: Union[List[DowntimeNotifyEndStateActions], UnsetType] = unset
    schedule: Union[
        DowntimeScheduleResponse, DowntimeScheduleRecurrencesResponse, DowntimeScheduleOneTimeResponse, UnsetType
    ] = unset
    scope: Union[str, UnsetType] = unset
    status: Union[DowntimeStatus, UnsetType] = unset
    created_by: Union[str, none_type, UnsetType] = unset
    monitor: Union[str, none_type, UnsetType] = unset


class DowntimeResponse(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.downtime_response_data import DowntimeResponseData
        from datadog_api_client.v2.model.downtime_response_included_item import DowntimeResponseIncludedItem

        return {
            "data": (DowntimeResponseData,),
            "included": ([DowntimeResponseIncludedItem],),
        }

    attribute_map = {
        "data": "data",
        "included": "included",
    }
    json_api_model = DowntimeResponseJSON

    def __init__(
        self_,
        data: Union[DowntimeResponseData, UnsetType] = unset,
        included: Union[
            List[Union[DowntimeResponseIncludedItem, User, DowntimeMonitorIncludedItem]], UnsetType
        ] = unset,
        **kwargs,
    ):
        """
        Downtiming gives you greater control over monitor notifications by
        allowing you to globally exclude scopes from alerting.
        Downtime settings, which can be scheduled with start and end times,
        prevent all alerting related to specified Datadog tags.

        :param data: Downtime data.
        :type data: DowntimeResponseData, optional

        :param included: Array of objects related to the downtime that the user requested.
        :type included: [DowntimeResponseIncludedItem], optional
        """
        if data is not unset:
            kwargs["data"] = data
        if included is not unset:
            kwargs["included"] = included
        super().__init__(kwargs)
