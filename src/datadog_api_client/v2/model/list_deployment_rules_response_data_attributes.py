# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import List, Union, TYPE_CHECKING

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    unset,
    UnsetType,
)


if TYPE_CHECKING:
    from datadog_api_client.v2.model.deployment_rule_response_data_attributes import (
        DeploymentRuleResponseDataAttributes,
    )


class ListDeploymentRulesResponseDataAttributes(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.deployment_rule_response_data_attributes import (
            DeploymentRuleResponseDataAttributes,
        )

        return {
            "rules": ([DeploymentRuleResponseDataAttributes],),
        }

    attribute_map = {
        "rules": "rules",
    }

    def __init__(self_, rules: Union[List[DeploymentRuleResponseDataAttributes], UnsetType] = unset, **kwargs):
        """


        :param rules:
        :type rules: [DeploymentRuleResponseDataAttributes], optional
        """
        if rules is not unset:
            kwargs["rules"] = rules
        super().__init__(kwargs)
