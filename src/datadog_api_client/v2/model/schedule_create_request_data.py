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
    from datadog_api_client.v2.model.schedule_create_request_data_attributes import ScheduleCreateRequestDataAttributes
    from datadog_api_client.v2.model.schedule_create_request_data_relationships import (
        ScheduleCreateRequestDataRelationships,
    )
    from datadog_api_client.v2.model.schedule_create_request_data_type import ScheduleCreateRequestDataType


class ScheduleCreateRequestData(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.schedule_create_request_data_attributes import (
            ScheduleCreateRequestDataAttributes,
        )
        from datadog_api_client.v2.model.schedule_create_request_data_relationships import (
            ScheduleCreateRequestDataRelationships,
        )
        from datadog_api_client.v2.model.schedule_create_request_data_type import ScheduleCreateRequestDataType

        return {
            "attributes": (ScheduleCreateRequestDataAttributes,),
            "relationships": (ScheduleCreateRequestDataRelationships,),
            "type": (ScheduleCreateRequestDataType,),
        }

    attribute_map = {
        "attributes": "attributes",
        "relationships": "relationships",
        "type": "type",
    }

    def __init__(
        self_,
        attributes: ScheduleCreateRequestDataAttributes,
        type: ScheduleCreateRequestDataType,
        relationships: Union[ScheduleCreateRequestDataRelationships, UnsetType] = unset,
        **kwargs,
    ):
        """
        The core data wrapper for creating a schedule, encompassing attributes, relationships, and the resource type.

        :param attributes: Describes the main attributes for creating a new schedule, including name, layers, and time zone.
        :type attributes: ScheduleCreateRequestDataAttributes

        :param relationships: Gathers relationship objects for the schedule creation request, including the teams to associate.
        :type relationships: ScheduleCreateRequestDataRelationships, optional

        :param type: Schedules resource type.
        :type type: ScheduleCreateRequestDataType
        """
        if relationships is not unset:
            kwargs["relationships"] = relationships
        super().__init__(kwargs)

        self_.attributes = attributes
        self_.type = type
