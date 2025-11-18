# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import Union, TYPE_CHECKING

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
)


if TYPE_CHECKING:
    from datadog_api_client.v2.model.deployment_rules_options import DeploymentRulesOptions
    from datadog_api_client.v2.model.deployment_rule_options_faulty_deployment_detection import (
        DeploymentRuleOptionsFaultyDeploymentDetection,
    )
    from datadog_api_client.v2.model.deployment_rule_options_monitor import DeploymentRuleOptionsMonitor


class UpdateDeploymentRuleParamsDataAttributes(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.deployment_rules_options import DeploymentRulesOptions

        return {
            "dry_run": (bool,),
            "name": (str,),
            "options": (DeploymentRulesOptions,),
        }

    attribute_map = {
        "dry_run": "dry_run",
        "name": "name",
        "options": "options",
    }

    def __init__(
        self_,
        dry_run: bool,
        name: str,
        options: Union[
            DeploymentRulesOptions, DeploymentRuleOptionsFaultyDeploymentDetection, DeploymentRuleOptionsMonitor
        ],
        **kwargs,
    ):
        """
        Parameters for updating a deployment rule.

        :param dry_run: Whether to run this rule in dry-run mode.
        :type dry_run: bool

        :param name: The name of the deployment rule.
        :type name: str

        :param options: Options for deployment rule response representing either faulty deployment detection or monitor options.
        :type options: DeploymentRulesOptions
        """
        super().__init__(kwargs)

        self_.dry_run = dry_run
        self_.name = name
        self_.options = options
