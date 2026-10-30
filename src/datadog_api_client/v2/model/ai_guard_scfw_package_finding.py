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
    from datadog_api_client.v2.model.ai_guard_scfw_matched_rule import AIGuardScfwMatchedRule
    from datadog_api_client.v2.model.ai_guard_scfw_outcome import AIGuardScfwOutcome


class AIGuardScfwPackageFinding(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.ai_guard_scfw_matched_rule import AIGuardScfwMatchedRule
        from datadog_api_client.v2.model.ai_guard_scfw_outcome import AIGuardScfwOutcome

        return {
            "ecosystem": (str,),
            "matched_rules": ([AIGuardScfwMatchedRule],),
            "name": (str,),
            "outcome": (AIGuardScfwOutcome,),
            "version": (str,),
        }

    attribute_map = {
        "ecosystem": "ecosystem",
        "matched_rules": "matched_rules",
        "name": "name",
        "outcome": "outcome",
        "version": "version",
    }

    def __init__(
        self_,
        ecosystem: str,
        name: str,
        outcome: AIGuardScfwOutcome,
        version: str,
        matched_rules: Union[List[AIGuardScfwMatchedRule], UnsetType] = unset,
        **kwargs,
    ):
        """
        One package the Supply Chain Firewall evaluated, with the outcome and every matched rule.

        :param ecosystem: The package ecosystem the firewall evaluated, such as ``PyPI`` , ``npm`` , or ``crates.io``.
        :type ecosystem: str

        :param matched_rules: Every rule the firewall matched on the package.
        :type matched_rules: [AIGuardScfwMatchedRule], optional

        :param name: The name of the package.
        :type name: str

        :param outcome: The Supply Chain Firewall outcome for a package, a matched rule, or the whole request.
        :type outcome: AIGuardScfwOutcome

        :param version: The version of the package.
        :type version: str
        """
        if matched_rules is not unset:
            kwargs["matched_rules"] = matched_rules
        super().__init__(kwargs)

        self_.ecosystem = ecosystem
        self_.name = name
        self_.outcome = outcome
        self_.version = version
