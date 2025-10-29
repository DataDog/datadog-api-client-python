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
    from datadog_api_client.v2.model.deployment_rules_options import DeploymentRulesOptions
    from datadog_api_client.v2.model.deployment_rule_options_faulty_deployment_detection import (
        DeploymentRuleOptionsFaultyDeploymentDetection,
    )
    from datadog_api_client.v2.model.deployment_rule_options_monitor import DeploymentRuleOptionsMonitor


class CreateDeploymentRuleParamsDataAttributes(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.deployment_rules_options import DeploymentRulesOptions

        return {
            "dry_run": (bool,),
            "name": (str,),
            "options": (DeploymentRulesOptions,),
            "type": (str,),
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
        options: Union[
            DeploymentRulesOptions, DeploymentRuleOptionsFaultyDeploymentDetection, DeploymentRuleOptionsMonitor
        ],
        type: str,
        dry_run: Union[bool, UnsetType] = unset,
        **kwargs,
    ):
        """
        Parameters for creating a deployment rule.

        :param dry_run: Whether this rule is run in dry-run mode.
        :type dry_run: bool, optional

        :param name: The name of the deployment rule.
        :type name: str

        :param options: Options for deployment rule response representing either faulty deployment detection or monitor options.
        :type options: DeploymentRulesOptions

        :param type: The type of the deployment rule (faulty_deployment_detection or monitor).
        :type type: str
        """
        if dry_run is not unset:
            kwargs["dry_run"] = dry_run
        super().__init__(kwargs)

        self_.name = name
        self_.options = options
        self_.type = type
