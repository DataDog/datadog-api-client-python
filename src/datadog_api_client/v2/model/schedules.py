# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import List, Union, TYPE_CHECKING

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    unset,
    UnsetType,
)


if TYPE_CHECKING:
    from datadog_api_client.v2.model.schedule_list_item import ScheduleListItem
    from datadog_api_client.v2.model.team_reference import TeamReference
    from datadog_api_client.v2.model.schedules_response_meta import SchedulesResponseMeta


class Schedules(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.schedule_list_item import ScheduleListItem
        from datadog_api_client.v2.model.team_reference import TeamReference
        from datadog_api_client.v2.model.schedules_response_meta import SchedulesResponseMeta

        return {
            "data": ([ScheduleListItem],),
            "included": ([TeamReference],),
            "meta": (SchedulesResponseMeta,),
        }

    attribute_map = {
        "data": "data",
        "included": "included",
        "meta": "meta",
    }

    def __init__(
        self_,
        data: Union[List[ScheduleListItem], UnsetType] = unset,
        included: Union[List[TeamReference], UnsetType] = unset,
        meta: Union[SchedulesResponseMeta, UnsetType] = unset,
        **kwargs,
    ):
        """
        A list of schedules with pagination metadata and any related included resources (such as teams).

        :param data: A list of schedules.
        :type data: [ScheduleListItem], optional

        :param included: Any additional resources related to the schedules, such as teams.
        :type included: [TeamReference], optional

        :param meta: Metadata that is included in the response when listing schedules.
        :type meta: SchedulesResponseMeta, optional
        """
        if data is not unset:
            kwargs["data"] = data
        if included is not unset:
            kwargs["included"] = included
        if meta is not unset:
            kwargs["meta"] = meta
        super().__init__(kwargs)
