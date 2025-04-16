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
    from datadog_api_client.v2.model.escalation_policy_update_request_data_attributes import (
        EscalationPolicyUpdateRequestDataAttributes,
    )
    from datadog_api_client.v2.model.escalation_policy_update_request_data_relationships import (
        EscalationPolicyUpdateRequestDataRelationships,
    )
    from datadog_api_client.v2.model.escalation_policy_update_request_data_type import (
        EscalationPolicyUpdateRequestDataType,
    )


class EscalationPolicyUpdateRequestData(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.escalation_policy_update_request_data_attributes import (
            EscalationPolicyUpdateRequestDataAttributes,
        )
        from datadog_api_client.v2.model.escalation_policy_update_request_data_relationships import (
            EscalationPolicyUpdateRequestDataRelationships,
        )
        from datadog_api_client.v2.model.escalation_policy_update_request_data_type import (
            EscalationPolicyUpdateRequestDataType,
        )

        return {
            "attributes": (EscalationPolicyUpdateRequestDataAttributes,),
            "id": (str,),
            "relationships": (EscalationPolicyUpdateRequestDataRelationships,),
            "type": (EscalationPolicyUpdateRequestDataType,),
        }

    attribute_map = {
        "attributes": "attributes",
        "id": "id",
        "relationships": "relationships",
        "type": "type",
    }

    def __init__(
        self_,
        attributes: EscalationPolicyUpdateRequestDataAttributes,
        id: str,
        type: EscalationPolicyUpdateRequestDataType,
        relationships: Union[EscalationPolicyUpdateRequestDataRelationships, UnsetType] = unset,
        **kwargs,
    ):
        """
        Represents the data for updating an existing escalation policy, including its ID, attributes, relationships, and resource type.

        :param attributes: Defines the attributes that can be updated for an escalation policy, such as description, name, resolution behavior, retries, and steps.
        :type attributes: EscalationPolicyUpdateRequestDataAttributes

        :param id: Specifies the unique identifier of the escalation policy being updated.
        :type id: str

        :param relationships: Represents relationships in an escalation policy update request, including references to teams.
        :type relationships: EscalationPolicyUpdateRequestDataRelationships, optional

        :param type: Indicates that the resource is of type ``policies``.
        :type type: EscalationPolicyUpdateRequestDataType
        """
        if relationships is not unset:
            kwargs["relationships"] = relationships
        super().__init__(kwargs)

        self_.attributes = attributes
        self_.id = id
        self_.type = type
