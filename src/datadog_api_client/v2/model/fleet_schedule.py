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
    from datadog_api_client.v2.model.fleet_schedule_attributes import FleetScheduleAttributes
    from datadog_api_client.v2.model.fleet_schedule_resource_type import FleetScheduleResourceType


class FleetSchedule(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.fleet_schedule_attributes import FleetScheduleAttributes
        from datadog_api_client.v2.model.fleet_schedule_resource_type import FleetScheduleResourceType

        return {
            "attributes": (FleetScheduleAttributes,),
            "id": (str,),
            "type": (FleetScheduleResourceType,),
        }

    attribute_map = {
        "attributes": "attributes",
        "id": "id",
        "type": "type",
    }

    def __init__(self_, attributes: FleetScheduleAttributes, id: str, type: FleetScheduleResourceType, **kwargs):
        """
        A schedule that automatically creates deployments based on a recurrence rule.

        :param attributes: Attributes of a schedule in the response.
        :type attributes: FleetScheduleAttributes

        :param id: Unique identifier for the schedule.
        :type id: str

        :param type: The type of schedule resource.
        :type type: FleetScheduleResourceType
        """
        super().__init__(kwargs)

        self_.attributes = attributes
        self_.id = id
        self_.type = type
