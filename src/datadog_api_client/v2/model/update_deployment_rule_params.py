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
    from datadog_api_client.v2.model.update_deployment_rule_params_data import UpdateDeploymentRuleParamsData


class UpdateDeploymentRuleParams(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.update_deployment_rule_params_data import UpdateDeploymentRuleParamsData

        return {
            "data": (UpdateDeploymentRuleParamsData,),
        }

    attribute_map = {
        "data": "data",
    }

    def __init__(self_, data: UpdateDeploymentRuleParamsData, **kwargs):
        """
        Parameters for updating a deployment rule.

        :param data: Parameters for updating a deployment rule.
        :type data: UpdateDeploymentRuleParamsData
        """
        super().__init__(kwargs)

        self_.data = data
