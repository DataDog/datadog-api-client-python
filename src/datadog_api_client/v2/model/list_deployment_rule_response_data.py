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
    from datadog_api_client.v2.model.list_deployment_rules_response_data_attributes import (
        ListDeploymentRulesResponseDataAttributes,
    )
    from datadog_api_client.v2.model.list_deployment_rules_data_type import ListDeploymentRulesDataType


class ListDeploymentRuleResponseData(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.list_deployment_rules_response_data_attributes import (
            ListDeploymentRulesResponseDataAttributes,
        )
        from datadog_api_client.v2.model.list_deployment_rules_data_type import ListDeploymentRulesDataType

        return {
            "attributes": (ListDeploymentRulesResponseDataAttributes,),
            "id": (str,),
            "type": (ListDeploymentRulesDataType,),
        }

    attribute_map = {
        "attributes": "attributes",
        "id": "id",
        "type": "type",
    }

    def __init__(
        self_,
        attributes: ListDeploymentRulesResponseDataAttributes,
        id: str,
        type: ListDeploymentRulesDataType,
        **kwargs,
    ):
        """
        Data for a list of deployment rules.

        :param attributes:
        :type attributes: ListDeploymentRulesResponseDataAttributes

        :param id: Unique identifier of the deployment rule.
        :type id: str

        :param type: List deployment rule resource type.
        :type type: ListDeploymentRulesDataType
        """
        super().__init__(kwargs)

        self_.attributes = attributes
        self_.id = id
        self_.type = type
