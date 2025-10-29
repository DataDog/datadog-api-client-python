# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import Union, TYPE_CHECKING

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    datetime,
    unset,
    UnsetType,
)


if TYPE_CHECKING:
    from datadog_api_client.v2.model.deployment_rule_response_data_attributes_created_by import (
        DeploymentRuleResponseDataAttributesCreatedBy,
    )
    from datadog_api_client.v2.model.deployment_rules_options import DeploymentRulesOptions
    from datadog_api_client.v2.model.deployment_rule_response_data_attributes_type import (
        DeploymentRuleResponseDataAttributesType,
    )
    from datadog_api_client.v2.model.deployment_rule_response_data_attributes_updated_by import (
        DeploymentRuleResponseDataAttributesUpdatedBy,
    )
    from datadog_api_client.v2.model.deployment_rule_options_faulty_deployment_detection import (
        DeploymentRuleOptionsFaultyDeploymentDetection,
    )
    from datadog_api_client.v2.model.deployment_rule_options_monitor import DeploymentRuleOptionsMonitor


class DeploymentRuleResponseDataAttributes(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.deployment_rule_response_data_attributes_created_by import (
            DeploymentRuleResponseDataAttributesCreatedBy,
        )
        from datadog_api_client.v2.model.deployment_rules_options import DeploymentRulesOptions
        from datadog_api_client.v2.model.deployment_rule_response_data_attributes_type import (
            DeploymentRuleResponseDataAttributesType,
        )
        from datadog_api_client.v2.model.deployment_rule_response_data_attributes_updated_by import (
            DeploymentRuleResponseDataAttributesUpdatedBy,
        )

        return {
            "created_at": (datetime,),
            "created_by": (DeploymentRuleResponseDataAttributesCreatedBy,),
            "dry_run": (bool,),
            "gate_id": (str,),
            "name": (str,),
            "options": (DeploymentRulesOptions,),
            "type": (DeploymentRuleResponseDataAttributesType,),
            "updated_at": (datetime,),
            "updated_by": (DeploymentRuleResponseDataAttributesUpdatedBy,),
        }

    attribute_map = {
        "created_at": "created_at",
        "created_by": "created_by",
        "dry_run": "dry_run",
        "gate_id": "gate_id",
        "name": "name",
        "options": "options",
        "type": "type",
        "updated_at": "updated_at",
        "updated_by": "updated_by",
    }

    def __init__(
        self_,
        created_at: datetime,
        created_by: DeploymentRuleResponseDataAttributesCreatedBy,
        dry_run: bool,
        gate_id: str,
        name: str,
        options: Union[
            DeploymentRulesOptions, DeploymentRuleOptionsFaultyDeploymentDetection, DeploymentRuleOptionsMonitor
        ],
        type: DeploymentRuleResponseDataAttributesType,
        updated_at: Union[datetime, UnsetType] = unset,
        updated_by: Union[DeploymentRuleResponseDataAttributesUpdatedBy, UnsetType] = unset,
        **kwargs,
    ):
        """
        Basic information about a deployment rule.

        :param created_at: The timestamp when the deployment rule was created.
        :type created_at: datetime

        :param created_by: Information about the user who created the deployment rule.
        :type created_by: DeploymentRuleResponseDataAttributesCreatedBy

        :param dry_run: Whether this rule is run in dry-run mode.
        :type dry_run: bool

        :param gate_id: The ID of the deployment gate.
        :type gate_id: str

        :param name: The name of the deployment rule.
        :type name: str

        :param options: Options for deployment rule response representing either faulty deployment detection or monitor options.
        :type options: DeploymentRulesOptions

        :param type: The type of the deployment rule.
        :type type: DeploymentRuleResponseDataAttributesType

        :param updated_at: The timestamp when the deployment rule was last updated.
        :type updated_at: datetime, optional

        :param updated_by: Information about the user who updated the deployment rule.
        :type updated_by: DeploymentRuleResponseDataAttributesUpdatedBy, optional
        """
        if updated_at is not unset:
            kwargs["updated_at"] = updated_at
        if updated_by is not unset:
            kwargs["updated_by"] = updated_by
        super().__init__(kwargs)

        self_.created_at = created_at
        self_.created_by = created_by
        self_.dry_run = dry_run
        self_.gate_id = gate_id
        self_.name = name
        self_.options = options
        self_.type = type
