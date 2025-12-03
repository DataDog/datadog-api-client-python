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
    from datadog_api_client.v2.model.configured_schedule_target_attributes import ConfiguredScheduleTargetAttributes
    from datadog_api_client.v2.model.configured_schedule_target_relationships import (
        ConfiguredScheduleTargetRelationships,
    )
    from datadog_api_client.v2.model.configured_schedule_target_type import ConfiguredScheduleTargetType


class ConfiguredSchedule(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.configured_schedule_target_attributes import ConfiguredScheduleTargetAttributes
        from datadog_api_client.v2.model.configured_schedule_target_relationships import (
            ConfiguredScheduleTargetRelationships,
        )
        from datadog_api_client.v2.model.configured_schedule_target_type import ConfiguredScheduleTargetType

        return {
            "attributes": (ConfiguredScheduleTargetAttributes,),
            "id": (str,),
            "relationships": (ConfiguredScheduleTargetRelationships,),
            "type": (ConfiguredScheduleTargetType,),
        }

    attribute_map = {
        "attributes": "attributes",
        "id": "id",
        "relationships": "relationships",
        "type": "type",
    }

    def __init__(
        self_,
        attributes: ConfiguredScheduleTargetAttributes,
        id: str,
        relationships: ConfiguredScheduleTargetRelationships,
        type: ConfiguredScheduleTargetType,
        **kwargs,
    ):
        """
        Full resource representation of a configured schedule target with position (previous, current, or next).

        :param attributes: Attributes for a configured schedule target, including position.
        :type attributes: ConfiguredScheduleTargetAttributes

        :param id: Specifies the unique identifier of the configured schedule target.
        :type id: str

        :param relationships: Represents the relationships of a configured schedule target.
        :type relationships: ConfiguredScheduleTargetRelationships

        :param type: Indicates that the resource is of type ``schedule_target``.
        :type type: ConfiguredScheduleTargetType
        """
        super().__init__(kwargs)

        self_.attributes = attributes
        self_.id = id
        self_.relationships = relationships
        self_.type = type
