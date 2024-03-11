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
    from datadog_api_client.v2.model.cloud_workload_security_agent_rule_update_attributes import (
        CloudWorkloadSecurityAgentRuleUpdateAttributes,
    )
    from datadog_api_client.v2.model.cloud_workload_security_agent_rule_type import CloudWorkloadSecurityAgentRuleType


class CloudWorkloadSecurityAgentRuleUpdateData(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.cloud_workload_security_agent_rule_update_attributes import (
            CloudWorkloadSecurityAgentRuleUpdateAttributes,
        )
        from datadog_api_client.v2.model.cloud_workload_security_agent_rule_type import (
            CloudWorkloadSecurityAgentRuleType,
        )

        return {
            "attributes": (CloudWorkloadSecurityAgentRuleUpdateAttributes,),
            "id": (str,),
            "type": (CloudWorkloadSecurityAgentRuleType,),
        }

    attribute_map = {
        "attributes": "attributes",
        "id": "id",
        "type": "type",
    }

    def __init__(
        self_,
        attributes: CloudWorkloadSecurityAgentRuleUpdateAttributes,
        type: CloudWorkloadSecurityAgentRuleType,
        id: Union[str, UnsetType] = unset,
        **kwargs,
    ):
        """
        Object for a single Agent rule.

        :param attributes: Update an existing Cloud Workload Security Agent rule.
        :type attributes: CloudWorkloadSecurityAgentRuleUpdateAttributes

        :param id: The ID of the agent rule.
        :type id: str, optional

        :param type: The type of the resource. The value should always be ``agent_rule``.
        :type type: CloudWorkloadSecurityAgentRuleType
        """
        if id is not unset:
            kwargs["id"] = id
        super().__init__(kwargs)

        self_.attributes = attributes
        self_.type = type
