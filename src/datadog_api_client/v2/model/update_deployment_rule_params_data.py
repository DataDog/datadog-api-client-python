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
    from datadog_api_client.v2.model.update_deployment_rule_params_data_attributes import (
        UpdateDeploymentRuleParamsDataAttributes,
    )
    from datadog_api_client.v2.model.deployment_rule_data_type import DeploymentRuleDataType


class UpdateDeploymentRuleParamsData(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.update_deployment_rule_params_data_attributes import (
            UpdateDeploymentRuleParamsDataAttributes,
        )
        from datadog_api_client.v2.model.deployment_rule_data_type import DeploymentRuleDataType

        return {
            "attributes": (UpdateDeploymentRuleParamsDataAttributes,),
            "type": (DeploymentRuleDataType,),
        }

    attribute_map = {
        "attributes": "attributes",
        "type": "type",
    }

    def __init__(self_, attributes: UpdateDeploymentRuleParamsDataAttributes, type: DeploymentRuleDataType, **kwargs):
        """
        Parameters for updating a deployment rule.

        :param attributes: Parameters for updating a deployment rule.
        :type attributes: UpdateDeploymentRuleParamsDataAttributes

        :param type: Deployment rule resource type.
        :type type: DeploymentRuleDataType
        """
        super().__init__(kwargs)

        self_.attributes = attributes
        self_.type = type
