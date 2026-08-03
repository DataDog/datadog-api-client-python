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
    from datadog_api_client.v2.model.fleet_schedule_v2 import FleetScheduleV2
    from datadog_api_client.v2.model.fleet_schedules_v2_response_meta import FleetSchedulesV2ResponseMeta


class FleetSchedulesV2Response(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.fleet_schedule_v2 import FleetScheduleV2
        from datadog_api_client.v2.model.fleet_schedules_v2_response_meta import FleetSchedulesV2ResponseMeta

        return {
            "data": ([FleetScheduleV2],),
            "meta": (FleetSchedulesV2ResponseMeta,),
        }

    attribute_map = {
        "data": "data",
        "meta": "meta",
    }

    def __init__(
        self_, data: List[FleetScheduleV2], meta: Union[FleetSchedulesV2ResponseMeta, UnsetType] = unset, **kwargs
    ):
        """
        Response containing a list of fleet schedules.

        :param data: Array of schedules for the organization.
        :type data: [FleetScheduleV2]

        :param meta: Metadata for the v2 list of schedules response.
        :type meta: FleetSchedulesV2ResponseMeta, optional
        """
        if meta is not unset:
            kwargs["meta"] = meta
        super().__init__(kwargs)

        self_.data = data
