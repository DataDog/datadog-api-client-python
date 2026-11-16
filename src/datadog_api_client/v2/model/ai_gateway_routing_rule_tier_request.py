# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import List, Union, TYPE_CHECKING

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    none_type,
    unset,
    UnsetType,
)


if TYPE_CHECKING:
    from datadog_api_client.v2.model.ai_gateway_routing_classifier_request import AiGatewayRoutingClassifierRequest
    from datadog_api_client.v2.model.ai_gateway_nullable_routing_rule_tier_ordering import (
        AiGatewayNullableRoutingRuleTierOrdering,
    )
    from datadog_api_client.v2.model.ai_gateway_routing_rule_target_request import AiGatewayRoutingRuleTargetRequest


class AiGatewayRoutingRuleTierRequest(ModelNormal):
    validations = {
        "targets": {
            "min_items": 1,
        },
    }

    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.ai_gateway_routing_classifier_request import AiGatewayRoutingClassifierRequest
        from datadog_api_client.v2.model.ai_gateway_nullable_routing_rule_tier_ordering import (
            AiGatewayNullableRoutingRuleTierOrdering,
        )
        from datadog_api_client.v2.model.ai_gateway_routing_rule_target_request import AiGatewayRoutingRuleTargetRequest

        return {
            "classifier": (AiGatewayRoutingClassifierRequest,),
            "ordering": (AiGatewayNullableRoutingRuleTierOrdering,),
            "targets": ([AiGatewayRoutingRuleTargetRequest],),
        }

    attribute_map = {
        "classifier": "classifier",
        "ordering": "ordering",
        "targets": "targets",
    }

    def __init__(
        self_,
        targets: List[AiGatewayRoutingRuleTargetRequest],
        classifier: Union[AiGatewayRoutingClassifierRequest, none_type, UnsetType] = unset,
        ordering: Union[AiGatewayNullableRoutingRuleTierOrdering, none_type, UnsetType] = unset,
        **kwargs,
    ):
        """
        Routing fallback tier used to create or replace a rule.

        :param classifier: Decision model and settings for a classified tier. Omission preserves the saved classifier; null clears it. Newly selected models require provider View.
        :type classifier: AiGatewayRoutingClassifierRequest, none_type, optional

        :param ordering: How a tier orders its targets. Omission preserves the saved same-position tier on update; null resets to configured. New tiers default to configured. The weighted_affinity ordering distributes first-choice assignments by relative target weights and accepts only model targets with an explicit provider, without repeated provider and model pairs in the same tier. The ``classified`` ordering is allowed only in the first tier and requires a classifier, destination rubrics, and one default destination. Its targets are model targets that each name one provider, not "*". Besides the default, it needs 1 to 9 destinations, each with a different rubric. Classified routing is in Preview: saving a classified tier returns 403 Forbidden unless the feature is enabled for the organization.
        :type ordering: AiGatewayNullableRoutingRuleTierOrdering, none_type, optional

        :param targets:
        :type targets: [AiGatewayRoutingRuleTargetRequest]
        """
        if classifier is not unset:
            kwargs["classifier"] = classifier
        if ordering is not unset:
            kwargs["ordering"] = ordering
        super().__init__(kwargs)

        self_.targets = targets
