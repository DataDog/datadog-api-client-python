# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelComposed,
    cached_property,
)


class DeploymentGatesEvaluationRule(ModelComposed):
    def __init__(self, **kwargs):
        """
        A rule to evaluate as part of a deployment gate evaluation.

        :param dry_run: Rule-level dry run. When enabled, the rule is evaluated normally but always returns `pass`. The real result is visible in the Datadog UI.
        :type dry_run: bool, optional

        :param name: Human-readable name for this rule.
        :type name: str

        :param options: Options for a `monitor` rule.
        :type options: DeploymentGatesMonitorRuleOptions, optional

        :param type: The type identifier for a monitor rule.
        :type type: DeploymentGatesMonitorRuleType
        """
        super().__init__(kwargs)

    @cached_property
    def _composed_schemas(_):
        # we need this here to make our import statements work
        # we must store _composed_schemas in here so the code is only run
        # when we invoke this method. If we kept this at the class
        # level we would get an error because the class level
        # code would be run when this module is imported, and these composed
        # classes don't exist yet because their module has not finished
        # loading
        from datadog_api_client.v2.model.deployment_gates_monitor_rule import DeploymentGatesMonitorRule
        from datadog_api_client.v2.model.deployment_gates_fdd_rule import DeploymentGatesFDDRule

        return {
            "oneOf": [
                DeploymentGatesMonitorRule,
                DeploymentGatesFDDRule,
            ],
        }
