# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import List, TYPE_CHECKING

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
)


if TYPE_CHECKING:
    from datadog_api_client.v2.model.fleet_schedule import FleetSchedule


class FleetSchedulesResponse(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.fleet_schedule import FleetSchedule

        return {
            "data": ([FleetSchedule],),
        }

    attribute_map = {
        "data": "data",
    }

    def __init__(self_, data: List[FleetSchedule], **kwargs):
        """
        Response containing a list of schedules.

        :param data: Array of schedules.
        :type data: [FleetSchedule]
        """
        super().__init__(kwargs)

        self_.data = data
