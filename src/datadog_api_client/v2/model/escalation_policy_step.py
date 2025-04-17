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
    from datadog_api_client.v2.model.escalation_policy_step_attributes import EscalationPolicyStepAttributes
    from datadog_api_client.v2.model.escalation_policy_step_relationships import EscalationPolicyStepRelationships
    from datadog_api_client.v2.model.escalation_policy_step_type import EscalationPolicyStepType


class EscalationPolicyStep(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.escalation_policy_step_attributes import EscalationPolicyStepAttributes
        from datadog_api_client.v2.model.escalation_policy_step_relationships import EscalationPolicyStepRelationships
        from datadog_api_client.v2.model.escalation_policy_step_type import EscalationPolicyStepType

        return {
            "attributes": (EscalationPolicyStepAttributes,),
            "id": (str,),
            "relationships": (EscalationPolicyStepRelationships,),
            "type": (EscalationPolicyStepType,),
        }

    attribute_map = {
        "attributes": "attributes",
        "id": "id",
        "relationships": "relationships",
        "type": "type",
    }

    def __init__(
        self_,
        type: EscalationPolicyStepType,
        attributes: Union[EscalationPolicyStepAttributes, UnsetType] = unset,
        id: Union[str, UnsetType] = unset,
        relationships: Union[EscalationPolicyStepRelationships, UnsetType] = unset,
        **kwargs,
    ):
        """
        Represents a single step in an escalation policy, including its attributes, relationships, and resource type.

        :param attributes: Defines attributes for an escalation policy step, such as assignment strategy and escalation timeout.
        :type attributes: EscalationPolicyStepAttributes, optional

        :param id: Specifies the unique identifier of this escalation policy step.
        :type id: str, optional

        :param relationships: Represents the relationship of an escalation policy step to its targets.
        :type relationships: EscalationPolicyStepRelationships, optional

        :param type: Indicates that the resource is of type ``steps``.
        :type type: EscalationPolicyStepType
        """
        if attributes is not unset:
            kwargs["attributes"] = attributes
        if id is not unset:
            kwargs["id"] = id
        if relationships is not unset:
            kwargs["relationships"] = relationships
        super().__init__(kwargs)

        self_.type = type
