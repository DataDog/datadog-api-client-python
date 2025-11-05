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
    from datadog_api_client.v2.model.fleet_schedule_create_attributes import FleetScheduleCreateAttributes
    from datadog_api_client.v2.model.fleet_schedule_resource_type import FleetScheduleResourceType


class FleetScheduleCreate(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.fleet_schedule_create_attributes import FleetScheduleCreateAttributes
        from datadog_api_client.v2.model.fleet_schedule_resource_type import FleetScheduleResourceType

        return {
            "attributes": (FleetScheduleCreateAttributes,),
            "type": (FleetScheduleResourceType,),
        }

    attribute_map = {
        "attributes": "attributes",
        "type": "type",
    }

    def __init__(self_, attributes: FleetScheduleCreateAttributes, type: FleetScheduleResourceType, **kwargs):
        """
        Data for creating a new schedule.

        :param attributes: Attributes for creating a new schedule.
        :type attributes: FleetScheduleCreateAttributes

        :param type: The type of schedule resource.
        :type type: FleetScheduleResourceType
        """
        super().__init__(kwargs)

        self_.attributes = attributes
        self_.type = type
