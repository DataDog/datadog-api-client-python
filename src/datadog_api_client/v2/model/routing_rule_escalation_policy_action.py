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
    from datadog_api_client.v2.model.routing_rule_escalation_policy_action_support_hours import (
        RoutingRuleEscalationPolicyActionSupportHours,
    )
    from datadog_api_client.v2.model.routing_rule_escalation_policy_action_type import (
        RoutingRuleEscalationPolicyActionType,
    )
    from datadog_api_client.v2.model.urgency import Urgency


class RoutingRuleEscalationPolicyAction(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.routing_rule_escalation_policy_action_support_hours import (
            RoutingRuleEscalationPolicyActionSupportHours,
        )
        from datadog_api_client.v2.model.routing_rule_escalation_policy_action_type import (
            RoutingRuleEscalationPolicyActionType,
        )
        from datadog_api_client.v2.model.urgency import Urgency

        return {
            "ack_timeout_minutes": (int,),
            "policy_id": (str,),
            "support_hours": (RoutingRuleEscalationPolicyActionSupportHours,),
            "type": (RoutingRuleEscalationPolicyActionType,),
            "urgency": (Urgency,),
        }

    attribute_map = {
        "ack_timeout_minutes": "ack_timeout_minutes",
        "policy_id": "policy_id",
        "support_hours": "support_hours",
        "type": "type",
        "urgency": "urgency",
    }

    def __init__(
        self_,
        policy_id: str,
        type: RoutingRuleEscalationPolicyActionType,
        ack_timeout_minutes: Union[int, UnsetType] = unset,
        support_hours: Union[RoutingRuleEscalationPolicyActionSupportHours, UnsetType] = unset,
        urgency: Union[Urgency, UnsetType] = unset,
        **kwargs,
    ):
        """
        Triggers an escalation policy.

        :param ack_timeout_minutes: The number of minutes before an acknowledged page is re-triggered.
        :type ack_timeout_minutes: int, optional

        :param policy_id: The ID of the escalation policy to route to.
        :type policy_id: str

        :param support_hours: Support hours during which the escalation policy will be executed. Outside of these hours, the escalation policy will be on hold and triggered once the next support hours window starts. This is mutually exclusive with the top-level ``time_restriction`` field on the routing rule.
        :type support_hours: RoutingRuleEscalationPolicyActionSupportHours, optional

        :param type: Indicates that the action pages an escalation policy. This action can be set once per routing rule item, and is mutually exclusive with the top-level ``policy_id`` field on the routing rule.
        :type type: RoutingRuleEscalationPolicyActionType

        :param urgency: Specifies the level of urgency for a routing rule (low, high, or dynamic).
        :type urgency: Urgency, optional
        """
        if ack_timeout_minutes is not unset:
            kwargs["ack_timeout_minutes"] = ack_timeout_minutes
        if support_hours is not unset:
            kwargs["support_hours"] = support_hours
        if urgency is not unset:
            kwargs["urgency"] = urgency
        super().__init__(kwargs)

        self_.policy_id = policy_id
        self_.type = type
