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
    from datadog_api_client.v2.model.deployment_rule_response_data_attributes import (
        DeploymentRuleResponseDataAttributes,
    )
    from datadog_api_client.v2.model.deployment_rule_data_type import DeploymentRuleDataType


class DeploymentRuleResponseData(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.deployment_rule_response_data_attributes import (
            DeploymentRuleResponseDataAttributes,
        )
        from datadog_api_client.v2.model.deployment_rule_data_type import DeploymentRuleDataType

        return {
            "attributes": (DeploymentRuleResponseDataAttributes,),
            "id": (str,),
            "type": (DeploymentRuleDataType,),
        }

    attribute_map = {
        "attributes": "attributes",
        "id": "id",
        "type": "type",
    }

    def __init__(
        self_, attributes: DeploymentRuleResponseDataAttributes, id: str, type: DeploymentRuleDataType, **kwargs
    ):
        """
        Data for a deployment rule.

        :param attributes: Basic information about a deployment rule.
        :type attributes: DeploymentRuleResponseDataAttributes

        :param id: Unique identifier of the deployment rule.
        :type id: str

        :param type: Deployment rule resource type.
        :type type: DeploymentRuleDataType
        """
        super().__init__(kwargs)

        self_.attributes = attributes
        self_.id = id
        self_.type = type
