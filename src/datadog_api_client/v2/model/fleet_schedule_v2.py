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
    from datadog_api_client.v2.model.fleet_schedule_v2_attributes import FleetScheduleV2Attributes
    from datadog_api_client.v2.model.fleet_schedule_resource_type import FleetScheduleResourceType


class FleetScheduleV2(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.fleet_schedule_v2_attributes import FleetScheduleV2Attributes
        from datadog_api_client.v2.model.fleet_schedule_resource_type import FleetScheduleResourceType

        return {
            "attributes": (FleetScheduleV2Attributes,),
            "id": (str,),
            "type": (FleetScheduleResourceType,),
        }

    attribute_map = {
        "attributes": "attributes",
        "id": "id",
        "type": "type",
    }

    def __init__(self_, attributes: FleetScheduleV2Attributes, id: str, type: FleetScheduleResourceType, **kwargs):
        """
        A fleet upgrade schedule resource in the v2 API response.

        :param attributes: Attributes of a fleet schedule in the v2 API response.
        :type attributes: FleetScheduleV2Attributes

        :param id: Unique identifier for the schedule.
        :type id: str

        :param type: The type of schedule resource.
        :type type: FleetScheduleResourceType
        """
        super().__init__(kwargs)

        self_.attributes = attributes
        self_.id = id
        self_.type = type
