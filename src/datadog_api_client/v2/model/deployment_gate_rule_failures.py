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
    from datadog_api_client.v2.model.deployment_gate_rule_failure_monitor import DeploymentGateRuleFailureMonitor
    from datadog_api_client.v2.model.deployment_gate_rule_failure_narrative import DeploymentGateRuleFailureNarrative


class DeploymentGateRuleFailures(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.deployment_gate_rule_failure_monitor import DeploymentGateRuleFailureMonitor
        from datadog_api_client.v2.model.deployment_gate_rule_failure_narrative import (
            DeploymentGateRuleFailureNarrative,
        )

        return {
            "faulty_apm_resources": ([str],),
            "monitors": ([DeploymentGateRuleFailureMonitor],),
            "narratives": ([DeploymentGateRuleFailureNarrative],),
        }

    attribute_map = {
        "faulty_apm_resources": "faulty_apm_resources",
        "monitors": "monitors",
        "narratives": "narratives",
    }

    def __init__(
        self_,
        faulty_apm_resources: List[str],
        monitors: List[DeploymentGateRuleFailureMonitor],
        narratives: List[DeploymentGateRuleFailureNarrative],
        **kwargs,
    ):
        """
        Rule failure details.

        :param faulty_apm_resources: Names of faulty APM resources.
        :type faulty_apm_resources: [str]

        :param monitors:
        :type monitors: [DeploymentGateRuleFailureMonitor]

        :param narratives:
        :type narratives: [DeploymentGateRuleFailureNarrative]
        """
        super().__init__(kwargs)

        self_.faulty_apm_resources = faulty_apm_resources
        self_.monitors = monitors
        self_.narratives = narratives
