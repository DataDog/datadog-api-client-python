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
    from datadog_api_client.v2.model.escalation_policy_data_attributes import EscalationPolicyDataAttributes
    from datadog_api_client.v2.model.escalation_policy_data_relationships import EscalationPolicyDataRelationships
    from datadog_api_client.v2.model.escalation_policy_data_type import EscalationPolicyDataType


class EscalationPolicyData(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.escalation_policy_data_attributes import EscalationPolicyDataAttributes
        from datadog_api_client.v2.model.escalation_policy_data_relationships import EscalationPolicyDataRelationships
        from datadog_api_client.v2.model.escalation_policy_data_type import EscalationPolicyDataType

        return {
            "attributes": (EscalationPolicyDataAttributes,),
            "id": (str,),
            "relationships": (EscalationPolicyDataRelationships,),
            "type": (EscalationPolicyDataType,),
        }

    attribute_map = {
        "attributes": "attributes",
        "id": "id",
        "relationships": "relationships",
        "type": "type",
    }

    def __init__(
        self_,
        type: EscalationPolicyDataType,
        attributes: Union[EscalationPolicyDataAttributes, UnsetType] = unset,
        id: Union[str, UnsetType] = unset,
        relationships: Union[EscalationPolicyDataRelationships, UnsetType] = unset,
        **kwargs,
    ):
        """
        Represents the data for a single escalation policy, including its attributes, ID, relationships, and resource type.

        :param attributes: Defines the main attributes of an escalation policy, such as its name and behavior on policy end.
        :type attributes: EscalationPolicyDataAttributes, optional

        :param id: Specifies the unique identifier of the escalation policy.
        :type id: str, optional

        :param relationships: Represents the relationships for an escalation policy, including references to steps and teams.
        :type relationships: EscalationPolicyDataRelationships, optional

        :param type: Indicates that the resource is of type ``policies``.
        :type type: EscalationPolicyDataType
        """
        if attributes is not unset:
            kwargs["attributes"] = attributes
        if id is not unset:
            kwargs["id"] = id
        if relationships is not unset:
            kwargs["relationships"] = relationships
        super().__init__(kwargs)

        self_.type = type
