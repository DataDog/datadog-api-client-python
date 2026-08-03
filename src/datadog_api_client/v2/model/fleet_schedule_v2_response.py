# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import TYPE_CHECKING

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
)


if TYPE_CHECKING:
    from datadog_api_client.v2.model.fleet_schedule_v2 import FleetScheduleV2


class FleetScheduleV2Response(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.fleet_schedule_v2 import FleetScheduleV2

        return {
            "data": (FleetScheduleV2,),
        }

    attribute_map = {
        "data": "data",
    }

    def __init__(self_, data: FleetScheduleV2, **kwargs):
        """
        Response containing a single fleet schedule.

        :param data: A fleet upgrade schedule resource in the v2 API response.
        :type data: FleetScheduleV2
        """
        super().__init__(kwargs)

        self_.data = data
