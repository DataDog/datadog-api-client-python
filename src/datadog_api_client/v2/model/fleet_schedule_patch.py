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
    from datadog_api_client.v2.model.fleet_schedule_patch_attributes import FleetSchedulePatchAttributes
    from datadog_api_client.v2.model.fleet_schedule_resource_type import FleetScheduleResourceType


class FleetSchedulePatch(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.fleet_schedule_patch_attributes import FleetSchedulePatchAttributes
        from datadog_api_client.v2.model.fleet_schedule_resource_type import FleetScheduleResourceType

        return {
            "attributes": (FleetSchedulePatchAttributes,),
            "type": (FleetScheduleResourceType,),
        }

    attribute_map = {
        "attributes": "attributes",
        "type": "type",
    }

    def __init__(
        self_,
        type: FleetScheduleResourceType,
        attributes: Union[FleetSchedulePatchAttributes, UnsetType] = unset,
        **kwargs,
    ):
        """
        Data for partially updating a schedule.

        :param attributes: Attributes for partially updating a schedule. All fields are optional.
        :type attributes: FleetSchedulePatchAttributes, optional

        :param type: The type of schedule resource.
        :type type: FleetScheduleResourceType
        """
        if attributes is not unset:
            kwargs["attributes"] = attributes
        super().__init__(kwargs)

        self_.type = type
