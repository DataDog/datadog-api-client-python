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
    from datadog_api_client.v2.model.escalation_relationships import EscalationRelationships
    from datadog_api_client.v2.model.escalation_type import EscalationType


class Escalation(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.escalation_relationships import EscalationRelationships
        from datadog_api_client.v2.model.escalation_type import EscalationType

        return {
            "id": (str,),
            "relationships": (EscalationRelationships,),
            "type": (EscalationType,),
        }

    attribute_map = {
        "id": "id",
        "relationships": "relationships",
        "type": "type",
    }

    def __init__(
        self_,
        type: EscalationType,
        id: Union[str, UnsetType] = unset,
        relationships: Union[EscalationRelationships, UnsetType] = unset,
        **kwargs,
    ):
        """
        Represents an escalation policy step.

        :param id: Unique identifier of the escalation step.
        :type id: str, optional

        :param relationships: Contains the relationships of an escalation object, including its responders.
        :type relationships: EscalationRelationships, optional

        :param type: Represents the resource type for individual steps in an escalation policy used during incident response.
        :type type: EscalationType
        """
        if id is not unset:
            kwargs["id"] = id
        if relationships is not unset:
            kwargs["relationships"] = relationships
        super().__init__(kwargs)

        self_.type = type
