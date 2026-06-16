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
    from datadog_api_client.v2.model.deployment_gates_evaluation_rule import DeploymentGatesEvaluationRule
    from datadog_api_client.v2.model.deployment_gates_monitor_rule import DeploymentGatesMonitorRule
    from datadog_api_client.v2.model.deployment_gates_fdd_rule import DeploymentGatesFDDRule


class DeploymentGatesEvaluationConfiguration(ModelNormal):
    validations = {
        "rules": {
            "min_items": 1,
        },
    }

    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.deployment_gates_evaluation_rule import DeploymentGatesEvaluationRule

        return {
            "dry_run": (bool,),
            "rules": ([DeploymentGatesEvaluationRule],),
        }

    attribute_map = {
        "dry_run": "dry_run",
        "rules": "rules",
    }

    def __init__(
        self_,
        rules: List[Union[DeploymentGatesEvaluationRule, DeploymentGatesMonitorRule, DeploymentGatesFDDRule]],
        dry_run: Union[bool, UnsetType] = unset,
        **kwargs,
    ):
        """
        Inline rule definitions for a deployment gate evaluation. When provided, rules are evaluated
        directly from this configuration instead of using the preconfigured gate rules.
        At least one rule is required.

        :param dry_run: Gate-level dry run. When enabled, the rules are evaluated normally but the gate always returns ``pass``. The real result is visible in the Datadog UI.
        :type dry_run: bool, optional

        :param rules: The list of rules to evaluate. At least one rule is required.
        :type rules: [DeploymentGatesEvaluationRule]
        """
        if dry_run is not unset:
            kwargs["dry_run"] = dry_run
        super().__init__(kwargs)

        self_.rules = rules
