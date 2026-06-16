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
    from datadog_api_client.v2.model.deployment_gates_fdd_rule_options import DeploymentGatesFDDRuleOptions
    from datadog_api_client.v2.model.deployment_gates_fdd_rule_type import DeploymentGatesFDDRuleType


class DeploymentGatesFDDRule(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.deployment_gates_fdd_rule_options import DeploymentGatesFDDRuleOptions
        from datadog_api_client.v2.model.deployment_gates_fdd_rule_type import DeploymentGatesFDDRuleType

        return {
            "dry_run": (bool,),
            "name": (str,),
            "options": (DeploymentGatesFDDRuleOptions,),
            "type": (DeploymentGatesFDDRuleType,),
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
        type: DeploymentGatesFDDRuleType,
        dry_run: Union[bool, UnsetType] = unset,
        options: Union[DeploymentGatesFDDRuleOptions, UnsetType] = unset,
        **kwargs,
    ):
        """
        A faulty deployment detection rule to evaluate as part of a deployment gate evaluation.

        :param dry_run: Rule-level dry run. When enabled, the rule is evaluated normally but it always returns ``pass``. The real result is visible in the Datadog UI.
        :type dry_run: bool, optional

        :param name: Human-readable name for this rule.
        :type name: str

        :param options: Options for a ``faulty_deployment_detection`` rule.
        :type options: DeploymentGatesFDDRuleOptions, optional

        :param type: The type identifier for a faulty deployment detection rule.
        :type type: DeploymentGatesFDDRuleType
        """
        if dry_run is not unset:
            kwargs["dry_run"] = dry_run
        if options is not unset:
            kwargs["options"] = options
        super().__init__(kwargs)

        self_.name = name
        self_.type = type
