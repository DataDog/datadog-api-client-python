# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import Union, TYPE_CHECKING

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    unset,
    UnsetType,
)


if TYPE_CHECKING:
    from datadog_api_client.v2.model.fleet_schedule import FleetSchedule


class FleetScheduleResponse(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.fleet_schedule import FleetSchedule

        return {
            "data": (FleetSchedule,),
        }

    attribute_map = {
        "data": "data",
    }

    def __init__(self_, data: Union[FleetSchedule, UnsetType] = unset, **kwargs):
        """
        Response containing a single schedule.

        :param data: A schedule that automatically creates deployments based on a recurrence rule.
        :type data: FleetSchedule, optional
        """
        if data is not unset:
            kwargs["data"] = data
        super().__init__(kwargs)
