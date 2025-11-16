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
    from datadog_api_client.v2.model.create_deployment_rule_params_data_attributes import (
        CreateDeploymentRuleParamsDataAttributes,
    )
    from datadog_api_client.v2.model.deployment_rule_data_type import DeploymentRuleDataType


class CreateDeploymentRuleParamsData(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.create_deployment_rule_params_data_attributes import (
            CreateDeploymentRuleParamsDataAttributes,
        )
        from datadog_api_client.v2.model.deployment_rule_data_type import DeploymentRuleDataType

        return {
            "attributes": (CreateDeploymentRuleParamsDataAttributes,),
            "type": (DeploymentRuleDataType,),
        }

    attribute_map = {
        "attributes": "attributes",
        "type": "type",
    }

    def __init__(self_, attributes: CreateDeploymentRuleParamsDataAttributes, type: DeploymentRuleDataType, **kwargs):
        """
        Parameters for creating a deployment rule.

        :param attributes: Parameters for creating a deployment rule.
        :type attributes: CreateDeploymentRuleParamsDataAttributes

        :param type: Deployment rule resource type.
        :type type: DeploymentRuleDataType
        """
        super().__init__(kwargs)

        self_.attributes = attributes
        self_.type = type
