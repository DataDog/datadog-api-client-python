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
    from datadog_api_client.v2.model.routing_rule_escalation_policy_action_type import (
        RoutingRuleEscalationPolicyActionType,
    )
    from datadog_api_client.v2.model.urgency import Urgency


class RoutingRuleEscalationPolicyAction(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.time_restrictions import TimeRestrictions
        from datadog_api_client.v2.model.routing_rule_escalation_policy_action_type import (
            RoutingRuleEscalationPolicyActionType,
        )
        from datadog_api_client.v2.model.urgency import Urgency

        return {
            "ack_timeout_minutes": (int,),
            "policy_id": (str,),
            "support_hours": (TimeRestrictions,),
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
        support_hours: Union[TimeRestrictions, UnsetType] = unset,
        urgency: Union[Urgency, UnsetType] = unset,
        **kwargs,
    ):
        """
        Routes the page to an escalation policy, optionally restricted to business hours.

        :param ack_timeout_minutes: The number of minutes before an unacknowledged page is re-escalated.
        :type ack_timeout_minutes: int, optional

        :param policy_id: The ID of the escalation policy to route to.
        :type policy_id: str

        :param support_hours: Holds time zone information and a list of time restrictions for a routing rule.
        :type support_hours: TimeRestrictions, optional

        :param type: Indicates that the action routes to an escalation policy.
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
