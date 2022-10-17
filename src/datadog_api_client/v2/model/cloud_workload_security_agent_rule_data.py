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
from datadog_api_client.v2.model.cloud_workload_security_agent_rule_attributes import (
    CloudWorkloadSecurityAgentRuleAttributes,
)
from datadog_api_client.v2.model.cloud_workload_security_agent_rule_creator_attributes import (
    CloudWorkloadSecurityAgentRuleCreatorAttributes,
)
from datadog_api_client.v2.model.cloud_workload_security_agent_rule_updater_attributes import (
    CloudWorkloadSecurityAgentRuleUpdaterAttributes,
)

if TYPE_CHECKING:
    from datadog_api_client.v2.model.cloud_workload_security_agent_rule_type import CloudWorkloadSecurityAgentRuleType


@dataclass
class CloudWorkloadSecurityAgentRuleDataJSON:
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


class CloudWorkloadSecurityAgentRuleData(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.cloud_workload_security_agent_rule_type import (
            CloudWorkloadSecurityAgentRuleType,
        )

        return {
            "attributes": (CloudWorkloadSecurityAgentRuleAttributes,),
            "id": (str,),
            "type": (CloudWorkloadSecurityAgentRuleType,),
        }

    attribute_map = {
        "attributes": "attributes",
        "id": "id",
        "type": "type",
    }
    json_api_model = CloudWorkloadSecurityAgentRuleDataJSON

    def __init__(
        self_,
        attributes: Union[CloudWorkloadSecurityAgentRuleAttributes, UnsetType] = unset,
        id: Union[str, UnsetType] = unset,
        type: Union[CloudWorkloadSecurityAgentRuleType, UnsetType] = unset,
        **kwargs,
    ):
        """
        Object for a single Agent rule.

        :param attributes: A Cloud Workload Security Agent rule returned by the API.
        :type attributes: CloudWorkloadSecurityAgentRuleAttributes, optional

        :param id: The ID of the Agent rule.
        :type id: str, optional

        :param type: The type of the resource. The value should always be ``agent_rule``.
        :type type: CloudWorkloadSecurityAgentRuleType, optional
        """
        if attributes is not unset:
            kwargs["attributes"] = attributes
        if id is not unset:
            kwargs["id"] = id
        if type is not unset:
            kwargs["type"] = type
        super().__init__(kwargs)
