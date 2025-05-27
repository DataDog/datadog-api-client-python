# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import List, Union, TYPE_CHECKING

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    unset,
    UnsetType,
)


if TYPE_CHECKING:
    from datadog_api_client.v2.model.routing_rule_action import RoutingRuleAction
    from datadog_api_client.v2.model.time_restrictions import TimeRestrictions
    from datadog_api_client.v2.model.urgency import Urgency
    from datadog_api_client.v2.model.send_slack_message_action import SendSlackMessageAction
    from datadog_api_client.v2.model.send_teams_message_action import SendTeamsMessageAction


class RoutingRuleAttributes(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.routing_rule_action import RoutingRuleAction
        from datadog_api_client.v2.model.time_restrictions import TimeRestrictions
        from datadog_api_client.v2.model.urgency import Urgency

        return {
            "actions": ([RoutingRuleAction],),
            "query": (str,),
            "time_restriction": (TimeRestrictions,),
            "urgency": (Urgency,),
        }

    attribute_map = {
        "actions": "actions",
        "query": "query",
        "time_restriction": "time_restriction",
        "urgency": "urgency",
    }

    def __init__(
        self_,
        actions: Union[
            List[Union[RoutingRuleAction, SendSlackMessageAction, SendTeamsMessageAction]], UnsetType
        ] = unset,
        query: Union[str, UnsetType] = unset,
        time_restriction: Union[TimeRestrictions, UnsetType] = unset,
        urgency: Union[Urgency, UnsetType] = unset,
        **kwargs,
    ):
        """
        Defines the configurable attributes of a routing rule, such as actions, query, time restriction, and urgency.

        :param actions: Specifies the list of actions to perform when the routing rule matches.
        :type actions: [RoutingRuleAction], optional

        :param query: Defines the query or condition that triggers this routing rule.
        :type query: str, optional

        :param time_restriction: Holds time zone information and a list of time restrictions for a routing rule.
        :type time_restriction: TimeRestrictions, optional

        :param urgency: Specifies the level of urgency for a routing rule (low, high, or dynamic).
        :type urgency: Urgency, optional
        """
        if actions is not unset:
            kwargs["actions"] = actions
        if query is not unset:
            kwargs["query"] = query
        if time_restriction is not unset:
            kwargs["time_restriction"] = time_restriction
        if urgency is not unset:
            kwargs["urgency"] = urgency
        super().__init__(kwargs)
