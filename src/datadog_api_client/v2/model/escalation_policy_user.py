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
    from datadog_api_client.v2.model.escalation_policy_user_attributes import EscalationPolicyUserAttributes
    from datadog_api_client.v2.model.escalation_policy_user_type import EscalationPolicyUserType


class EscalationPolicyUser(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.escalation_policy_user_attributes import EscalationPolicyUserAttributes
        from datadog_api_client.v2.model.escalation_policy_user_type import EscalationPolicyUserType

        return {
            "attributes": (EscalationPolicyUserAttributes,),
            "id": (str,),
            "type": (EscalationPolicyUserType,),
        }

    attribute_map = {
        "attributes": "attributes",
        "id": "id",
        "type": "type",
    }

    def __init__(
        self_,
        type: EscalationPolicyUserType,
        attributes: Union[EscalationPolicyUserAttributes, UnsetType] = unset,
        id: Union[str, UnsetType] = unset,
        **kwargs,
    ):
        """
        Represents a user object in the context of an escalation policy, including their ``id`` , type, and basic attributes.

        :param attributes: Provides basic user information for an escalation policy, including a name and email address.
        :type attributes: EscalationPolicyUserAttributes, optional

        :param id: The unique user identifier.
        :type id: str, optional

        :param type: Users resource type.
        :type type: EscalationPolicyUserType
        """
        if attributes is not unset:
            kwargs["attributes"] = attributes
        if id is not unset:
            kwargs["id"] = id
        super().__init__(kwargs)

        self_.type = type
