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
    from datadog_api_client.v2.model.schedule_data import ScheduleData
    from datadog_api_client.v2.model.schedule_data_included_item import ScheduleDataIncludedItem
    from datadog_api_client.v2.model.team_reference import TeamReference
    from datadog_api_client.v2.model.layer import Layer
    from datadog_api_client.v2.model.schedule_member import ScheduleMember
    from datadog_api_client.v2.model.schedule_user import ScheduleUser


class Schedule(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.schedule_data import ScheduleData
        from datadog_api_client.v2.model.schedule_data_included_item import ScheduleDataIncludedItem

        return {
            "data": (ScheduleData,),
            "included": ([ScheduleDataIncludedItem],),
        }

    attribute_map = {
        "data": "data",
        "included": "included",
    }

    def __init__(
        self_,
        data: Union[ScheduleData, UnsetType] = unset,
        included: Union[
            List[Union[ScheduleDataIncludedItem, TeamReference, Layer, ScheduleMember, ScheduleUser]], UnsetType
        ] = unset,
        **kwargs,
    ):
        """
        Top-level container for a schedule object, including both the ``data`` payload and any related ``included`` resources (such as teams, layers, or members).

        :param data: Represents the primary data object for a schedule, linking attributes and relationships.
        :type data: ScheduleData, optional

        :param included: Any additional resources related to this schedule, such as teams and layers.
        :type included: [ScheduleDataIncludedItem], optional
        """
        if data is not unset:
            kwargs["data"] = data
        if included is not unset:
            kwargs["included"] = included
        super().__init__(kwargs)
