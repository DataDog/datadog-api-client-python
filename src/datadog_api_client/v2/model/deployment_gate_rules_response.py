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
    from datadog_api_client.v2.model.list_deployment_rule_response_data import ListDeploymentRuleResponseData


class DeploymentGateRulesResponse(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.list_deployment_rule_response_data import ListDeploymentRuleResponseData

        return {
            "data": (ListDeploymentRuleResponseData,),
        }

    attribute_map = {
        "data": "data",
    }

    def __init__(self_, data: Union[ListDeploymentRuleResponseData, UnsetType] = unset, **kwargs):
        """
        Response for a deployment gate rules.

        :param data: Data for a list of deployment rules.
        :type data: ListDeploymentRuleResponseData, optional
        """
        if data is not unset:
            kwargs["data"] = data
        super().__init__(kwargs)
