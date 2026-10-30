# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import TYPE_CHECKING

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
)


if TYPE_CHECKING:
    from datadog_api_client.v2.model.ai_guard_scfw_outcome import AIGuardScfwOutcome


class AIGuardScfwMatchedRule(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.ai_guard_scfw_outcome import AIGuardScfwOutcome

        return {
            "outcome": (AIGuardScfwOutcome,),
            "rule": (str,),
        }

    attribute_map = {
        "outcome": "outcome",
        "rule": "rule",
    }

    def __init__(self_, outcome: AIGuardScfwOutcome, rule: str, **kwargs):
        """
        One rule the Supply Chain Firewall matched on a package, with the outcome the rule reached.

        :param outcome: The Supply Chain Firewall outcome for a package, a matched rule, or the whole request.
        :type outcome: AIGuardScfwOutcome

        :param rule: The rule text the firewall reported, or the policy type when no text was reported.
        :type rule: str
        """
        super().__init__(kwargs)

        self_.outcome = outcome
        self_.rule = rule
