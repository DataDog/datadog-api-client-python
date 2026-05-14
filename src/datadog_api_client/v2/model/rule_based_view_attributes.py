# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import List, TYPE_CHECKING

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
)


if TYPE_CHECKING:
    from datadog_api_client.v2.model.rule_based_view_rule import RuleBasedViewRule


class RuleBasedViewAttributes(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.rule_based_view_rule import RuleBasedViewRule

        return {
            "count": (int,),
            "rules": ([RuleBasedViewRule],),
        }

    attribute_map = {
        "count": "count",
        "rules": "rules",
    }

    def __init__(self_, count: int, rules: List[RuleBasedViewRule], **kwargs):
        """
        Attributes of the rule-based view.

        :param count: Total number of rules in the view.
        :type count: int

        :param rules: List of rules in the rule-based view.
        :type rules: [RuleBasedViewRule]
        """
        super().__init__(kwargs)

        self_.count = count
        self_.rules = rules
