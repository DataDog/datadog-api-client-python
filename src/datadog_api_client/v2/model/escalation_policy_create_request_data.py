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
    from datadog_api_client.v2.model.escalation_policy_create_request_data_attributes import (
        EscalationPolicyCreateRequestDataAttributes,
    )
    from datadog_api_client.v2.model.escalation_policy_create_request_data_relationships import (
        EscalationPolicyCreateRequestDataRelationships,
    )
    from datadog_api_client.v2.model.escalation_policy_create_request_data_type import (
        EscalationPolicyCreateRequestDataType,
    )


class EscalationPolicyCreateRequestData(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.escalation_policy_create_request_data_attributes import (
            EscalationPolicyCreateRequestDataAttributes,
        )
        from datadog_api_client.v2.model.escalation_policy_create_request_data_relationships import (
            EscalationPolicyCreateRequestDataRelationships,
        )
        from datadog_api_client.v2.model.escalation_policy_create_request_data_type import (
            EscalationPolicyCreateRequestDataType,
        )

        return {
            "attributes": (EscalationPolicyCreateRequestDataAttributes,),
            "relationships": (EscalationPolicyCreateRequestDataRelationships,),
            "type": (EscalationPolicyCreateRequestDataType,),
        }

    attribute_map = {
        "attributes": "attributes",
        "relationships": "relationships",
        "type": "type",
    }

    def __init__(
        self_,
        attributes: EscalationPolicyCreateRequestDataAttributes,
        type: EscalationPolicyCreateRequestDataType,
        relationships: Union[EscalationPolicyCreateRequestDataRelationships, UnsetType] = unset,
        **kwargs,
    ):
        """
        Represents the data for creating an escalation policy, including its attributes, relationships, and resource type.

        :param attributes: Defines the attributes for creating an escalation policy, including its description, name, resolution behavior, retries, and steps.
        :type attributes: EscalationPolicyCreateRequestDataAttributes

        :param relationships: Represents relationships in an escalation policy creation request, including references to teams.
        :type relationships: EscalationPolicyCreateRequestDataRelationships, optional

        :param type: Indicates that the resource is of type ``policies``.
        :type type: EscalationPolicyCreateRequestDataType
        """
        if relationships is not unset:
            kwargs["relationships"] = relationships
        super().__init__(kwargs)

        self_.attributes = attributes
        self_.type = type
