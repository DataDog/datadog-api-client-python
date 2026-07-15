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
    from datadog_api_client.v2.model.schedule_on_call_responder_data_attributes import (
        ScheduleOnCallResponderDataAttributes,
    )
    from datadog_api_client.v2.model.schedule_on_call_responder_data_relationships import (
        ScheduleOnCallResponderDataRelationships,
    )
    from datadog_api_client.v2.model.schedule_on_call_responder_data_type import ScheduleOnCallResponderDataType


class ScheduleOnCallResponderData(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.schedule_on_call_responder_data_attributes import (
            ScheduleOnCallResponderDataAttributes,
        )
        from datadog_api_client.v2.model.schedule_on_call_responder_data_relationships import (
            ScheduleOnCallResponderDataRelationships,
        )
        from datadog_api_client.v2.model.schedule_on_call_responder_data_type import ScheduleOnCallResponderDataType

        return {
            "attributes": (ScheduleOnCallResponderDataAttributes,),
            "id": (str,),
            "relationships": (ScheduleOnCallResponderDataRelationships,),
            "type": (ScheduleOnCallResponderDataType,),
        }

    attribute_map = {
        "attributes": "attributes",
        "id": "id",
        "relationships": "relationships",
        "type": "type",
    }

    def __init__(
        self_,
        type: ScheduleOnCallResponderDataType,
        attributes: Union[ScheduleOnCallResponderDataAttributes, UnsetType] = unset,
        id: Union[str, UnsetType] = unset,
        relationships: Union[ScheduleOnCallResponderDataRelationships, UnsetType] = unset,
        **kwargs,
    ):
        """
        Represents one position's (previous, current, or next) group of on-call responder shifts. Positions with no matching shift are omitted entirely from the response.

        :param attributes: Attributes for one position's (previous, current, or next) group of on-call responder shifts.
        :type attributes: ScheduleOnCallResponderDataAttributes, optional

        :param id: Unique identifier of this responder group.
        :type id: str, optional

        :param relationships: Relationships for a single position's (previous, current, or next) responder group.
        :type relationships: ScheduleOnCallResponderDataRelationships, optional

        :param type: Represents the resource type for a single position's (previous, current, or next) group of on-call responder shifts.
        :type type: ScheduleOnCallResponderDataType
        """
        if attributes is not unset:
            kwargs["attributes"] = attributes
        if id is not unset:
            kwargs["id"] = id
        if relationships is not unset:
            kwargs["relationships"] = relationships
        super().__init__(kwargs)

        self_.type = type
