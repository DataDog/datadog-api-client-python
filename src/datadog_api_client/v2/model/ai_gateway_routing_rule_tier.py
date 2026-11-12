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
    from datadog_api_client.v2.model.ai_gateway_routing_classifier import AiGatewayRoutingClassifier
    from datadog_api_client.v2.model.ai_gateway_routing_rule_tier_ordering import AiGatewayRoutingRuleTierOrdering
    from datadog_api_client.v2.model.ai_gateway_routing_rule_tier_ordering_issue import (
        AiGatewayRoutingRuleTierOrderingIssue,
    )
    from datadog_api_client.v2.model.ai_gateway_routing_rule_target import AiGatewayRoutingRuleTarget


class AiGatewayRoutingRuleTier(ModelNormal):
    validations = {
        "targets": {
            "min_items": 1,
        },
    }

    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.ai_gateway_routing_classifier import AiGatewayRoutingClassifier
        from datadog_api_client.v2.model.ai_gateway_routing_rule_tier_ordering import AiGatewayRoutingRuleTierOrdering
        from datadog_api_client.v2.model.ai_gateway_routing_rule_tier_ordering_issue import (
            AiGatewayRoutingRuleTierOrderingIssue,
        )
        from datadog_api_client.v2.model.ai_gateway_routing_rule_target import AiGatewayRoutingRuleTarget

        return {
            "classifier": (AiGatewayRoutingClassifier,),
            "ordering": (AiGatewayRoutingRuleTierOrdering,),
            "ordering_issue": (AiGatewayRoutingRuleTierOrderingIssue,),
            "targets": ([AiGatewayRoutingRuleTarget],),
        }

    attribute_map = {
        "classifier": "classifier",
        "ordering": "ordering",
        "ordering_issue": "ordering_issue",
        "targets": "targets",
    }
    read_only_vars = {
        "ordering_issue",
    }

    def __init__(
        self_,
        ordering: AiGatewayRoutingRuleTierOrdering,
        targets: List[AiGatewayRoutingRuleTarget],
        classifier: Union[AiGatewayRoutingClassifier, UnsetType] = unset,
        ordering_issue: Union[AiGatewayRoutingRuleTierOrderingIssue, UnsetType] = unset,
        **kwargs,
    ):
        """
        Routing fallback tier containing targets and their effective ordering.

        :param classifier: Saved classified-tier settings. Provider and model are empty when the caller cannot view the provider.
        :type classifier: AiGatewayRoutingClassifier, optional

        :param ordering: How a tier orders its targets.
        :type ordering: AiGatewayRoutingRuleTierOrdering

        :param ordering_issue: Stored tier ordering is inconsistent. mixed means targets have different supported orderings, and unknown means a target has an unsupported ordering. The tier is reported as configured without weights. Replace the rule to repair it. Omitted for consistent tiers. A forced deletion cannot rewrite a surviving tier with an unknown issue.
        :type ordering_issue: AiGatewayRoutingRuleTierOrderingIssue, optional

        :param targets:
        :type targets: [AiGatewayRoutingRuleTarget]
        """
        if classifier is not unset:
            kwargs["classifier"] = classifier
        if ordering_issue is not unset:
            kwargs["ordering_issue"] = ordering_issue
        super().__init__(kwargs)

        self_.ordering = ordering
        self_.targets = targets
