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
    from datadog_api_client.v2.model.deployment_gates_bits_deployment_analysis_rule_options import (
        DeploymentGatesBitsDeploymentAnalysisRuleOptions,
    )
    from datadog_api_client.v2.model.deployment_gates_bits_deployment_analysis_rule_type import (
        DeploymentGatesBitsDeploymentAnalysisRuleType,
    )


class DeploymentGatesBitsDeploymentAnalysisRule(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.deployment_gates_bits_deployment_analysis_rule_options import (
            DeploymentGatesBitsDeploymentAnalysisRuleOptions,
        )
        from datadog_api_client.v2.model.deployment_gates_bits_deployment_analysis_rule_type import (
            DeploymentGatesBitsDeploymentAnalysisRuleType,
        )

        return {
            "dry_run": (bool,),
            "name": (str,),
            "options": (DeploymentGatesBitsDeploymentAnalysisRuleOptions,),
            "type": (DeploymentGatesBitsDeploymentAnalysisRuleType,),
        }

    attribute_map = {
        "dry_run": "dry_run",
        "name": "name",
        "options": "options",
        "type": "type",
    }

    def __init__(
        self_,
        name: str,
        type: DeploymentGatesBitsDeploymentAnalysisRuleType,
        dry_run: Union[bool, UnsetType] = unset,
        options: Union[DeploymentGatesBitsDeploymentAnalysisRuleOptions, UnsetType] = unset,
        **kwargs,
    ):
        """
        A Bits Deployment Analysis rule to evaluate as part of a deployment gate evaluation.

        :param dry_run: Rule-level dry run. When enabled, the rule is evaluated normally but it always returns ``pass``. The real result is visible in the Datadog UI.
        :type dry_run: bool, optional

        :param name: Human-readable name for this rule.
        :type name: str

        :param options: Options for a ``bits_deployment_analysis`` rule.
        :type options: DeploymentGatesBitsDeploymentAnalysisRuleOptions, optional

        :param type: The type identifier for a Bits Deployment Analysis rule.
        :type type: DeploymentGatesBitsDeploymentAnalysisRuleType
        """
        if dry_run is not unset:
            kwargs["dry_run"] = dry_run
        if options is not unset:
            kwargs["options"] = options
        super().__init__(kwargs)

        self_.name = name
        self_.type = type
