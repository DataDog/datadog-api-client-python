# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from dataclasses import dataclass
from typing import Union, TYPE_CHECKING

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    unset,
    UnsetType,
)


from datadog_api_client.v2.model.cloud_workload_security_agent_rule_creator_attributes import (
    CloudWorkloadSecurityAgentRuleCreatorAttributes,
)
from datadog_api_client.v2.model.cloud_workload_security_agent_rule_updater_attributes import (
    CloudWorkloadSecurityAgentRuleUpdaterAttributes,
)
from datadog_api_client.v2.model.cloud_workload_security_agent_rule_creator_attributes import (
    CloudWorkloadSecurityAgentRuleCreatorAttributes,
)
from datadog_api_client.v2.model.cloud_workload_security_agent_rule_updater_attributes import (
    CloudWorkloadSecurityAgentRuleUpdaterAttributes,
)

if TYPE_CHECKING:
    from datadog_api_client.v2.model.cloud_workload_security_agent_rule_data import CloudWorkloadSecurityAgentRuleData


@dataclass
class CloudWorkloadSecurityAgentRuleResponseJSON:
    id: str
    category: Union[str, UnsetType] = unset
    creation_date: Union[int, UnsetType] = unset
    creator: Union[CloudWorkloadSecurityAgentRuleCreatorAttributes, UnsetType] = unset
    default_rule: Union[bool, UnsetType] = unset
    description: Union[str, UnsetType] = unset
    enabled: Union[bool, UnsetType] = unset
    expression: Union[str, UnsetType] = unset
    name: Union[str, UnsetType] = unset
    updated_at: Union[int, UnsetType] = unset
    updater: Union[CloudWorkloadSecurityAgentRuleUpdaterAttributes, UnsetType] = unset
    version: Union[int, UnsetType] = unset


class CloudWorkloadSecurityAgentRuleResponse(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.cloud_workload_security_agent_rule_data import (
            CloudWorkloadSecurityAgentRuleData,
        )

        return {
            "data": (CloudWorkloadSecurityAgentRuleData,),
        }

    attribute_map = {
        "data": "data",
    }
    json_api_model = CloudWorkloadSecurityAgentRuleResponseJSON

    def __init__(self_, data: Union[CloudWorkloadSecurityAgentRuleData, UnsetType] = unset, **kwargs):
        """
        Response object that includes an Agent rule.

        :param data: Object for a single Agent rule.
        :type data: CloudWorkloadSecurityAgentRuleData, optional
        """
        if data is not unset:
            kwargs["data"] = data
        super().__init__(kwargs)
