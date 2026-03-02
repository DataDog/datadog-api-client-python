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
    from datadog_api_client.v2.model.time_restrictions import TimeRestrictions
    from datadog_api_client.v2.model.escalation_policy_action_type import EscalationPolicyActionType
    from datadog_api_client.v2.model.urgency import Urgency


class EscalationPolicyAction(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.time_restrictions import TimeRestrictions
        from datadog_api_client.v2.model.escalation_policy_action_type import EscalationPolicyActionType
        from datadog_api_client.v2.model.urgency import Urgency

        return {
            "policy_id": (str,),
            "support_hours": (TimeRestrictions,),
            "type": (EscalationPolicyActionType,),
            "urgency": (Urgency,),
        }

    attribute_map = {
        "policy_id": "policy_id",
        "support_hours": "support_hours",
        "type": "type",
        "urgency": "urgency",
    }

    def __init__(
        self_,
        policy_id: str,
        type: EscalationPolicyActionType,
        support_hours: Union[TimeRestrictions, UnsetType] = unset,
        urgency: Union[Urgency, UnsetType] = unset,
        **kwargs,
    ):
        """
        Triggers an escalation policy when the routing rule matches.

        :param policy_id: The ID of the escalation policy to trigger.
        :type policy_id: str

        :param support_hours: Holds time zone information and a list of time restrictions for a routing rule.
        :type support_hours: TimeRestrictions, optional

        :param type: Indicates that the action is an escalation policy action.
        :type type: EscalationPolicyActionType

        :param urgency: Specifies the level of urgency for a routing rule (low, high, or dynamic).
        :type urgency: Urgency, optional
        """
        if support_hours is not unset:
            kwargs["support_hours"] = support_hours
        if urgency is not unset:
            kwargs["urgency"] = urgency
        super().__init__(kwargs)

        self_.policy_id = policy_id
        self_.type = type
