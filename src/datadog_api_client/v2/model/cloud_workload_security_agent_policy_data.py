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
    from datadog_api_client.v2.model.cloud_workload_security_agent_policy_attributes import (
        CloudWorkloadSecurityAgentPolicyAttributes,
    )
    from datadog_api_client.v2.model.cloud_workload_security_agent_policy_type import (
        CloudWorkloadSecurityAgentPolicyType,
    )


class CloudWorkloadSecurityAgentPolicyData(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.cloud_workload_security_agent_policy_attributes import (
            CloudWorkloadSecurityAgentPolicyAttributes,
        )
        from datadog_api_client.v2.model.cloud_workload_security_agent_policy_type import (
            CloudWorkloadSecurityAgentPolicyType,
        )

        return {
            "attributes": (CloudWorkloadSecurityAgentPolicyAttributes,),
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
        attributes: Union[CloudWorkloadSecurityAgentPolicyAttributes, UnsetType] = unset,
        id: Union[str, UnsetType] = unset,
        type: Union[CloudWorkloadSecurityAgentPolicyType, UnsetType] = unset,
        **kwargs,
    ):
        """
        Object for a single Agent policy

        :param attributes: A Cloud Workload Security Agent policy returned by the API
        :type attributes: CloudWorkloadSecurityAgentPolicyAttributes, optional

        :param id: The ID of the Agent policy
        :type id: str, optional

        :param type: The type of the resource, must always be ``policy``
        :type type: CloudWorkloadSecurityAgentPolicyType, optional
        """
        if attributes is not unset:
            kwargs["attributes"] = attributes
        if id is not unset:
            kwargs["id"] = id
        if type is not unset:
            kwargs["type"] = type
        super().__init__(kwargs)
