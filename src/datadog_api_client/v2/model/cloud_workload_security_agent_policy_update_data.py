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
    from datadog_api_client.v2.model.cloud_workload_security_agent_policy_update_attributes import (
        CloudWorkloadSecurityAgentPolicyUpdateAttributes,
    )
    from datadog_api_client.v2.model.cloud_workload_security_agent_policy_type import (
        CloudWorkloadSecurityAgentPolicyType,
    )


class CloudWorkloadSecurityAgentPolicyUpdateData(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.cloud_workload_security_agent_policy_update_attributes import (
            CloudWorkloadSecurityAgentPolicyUpdateAttributes,
        )
        from datadog_api_client.v2.model.cloud_workload_security_agent_policy_type import (
            CloudWorkloadSecurityAgentPolicyType,
        )

        return {
            "attributes": (CloudWorkloadSecurityAgentPolicyUpdateAttributes,),
            "id": (str,),
            "type": (CloudWorkloadSecurityAgentPolicyType,),
        }

    attribute_map = {
        "attributes": "attributes",
        "id": "id",
        "type": "type",
    }

    def __init__(
        self_,
        attributes: CloudWorkloadSecurityAgentPolicyUpdateAttributes,
        type: CloudWorkloadSecurityAgentPolicyType,
        id: Union[str, UnsetType] = unset,
        **kwargs,
    ):
        """
        Object for a single Agent policy

        :param attributes: Update an existing Cloud Workload Security Agent policy
        :type attributes: CloudWorkloadSecurityAgentPolicyUpdateAttributes

        :param id: The ID of the Agent policy
        :type id: str, optional

        :param type: The type of the resource, must always be ``policy``
        :type type: CloudWorkloadSecurityAgentPolicyType
        """
        if id is not unset:
            kwargs["id"] = id
        super().__init__(kwargs)

        self_.attributes = attributes
        self_.type = type
