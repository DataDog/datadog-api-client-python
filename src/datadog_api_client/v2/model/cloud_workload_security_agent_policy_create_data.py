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
    from datadog_api_client.v2.model.cloud_workload_security_agent_policy_create_attributes import (
        CloudWorkloadSecurityAgentPolicyCreateAttributes,
    )
    from datadog_api_client.v2.model.cloud_workload_security_agent_policy_type import (
        CloudWorkloadSecurityAgentPolicyType,
    )


class CloudWorkloadSecurityAgentPolicyCreateData(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.cloud_workload_security_agent_policy_create_attributes import (
            CloudWorkloadSecurityAgentPolicyCreateAttributes,
        )
        from datadog_api_client.v2.model.cloud_workload_security_agent_policy_type import (
            CloudWorkloadSecurityAgentPolicyType,
        )

        return {
            "attributes": (CloudWorkloadSecurityAgentPolicyCreateAttributes,),
            "type": (CloudWorkloadSecurityAgentPolicyType,),
        }

    attribute_map = {
        "attributes": "attributes",
        "type": "type",
    }

    def __init__(
        self_,
        attributes: CloudWorkloadSecurityAgentPolicyCreateAttributes,
        type: CloudWorkloadSecurityAgentPolicyType,
        **kwargs,
    ):
        """
        Object for a single Agent rule

        :param attributes: Create a new Cloud Workload Security Agent policy
        :type attributes: CloudWorkloadSecurityAgentPolicyCreateAttributes

        :param type: The type of the resource, must always be ``policy``
        :type type: CloudWorkloadSecurityAgentPolicyType
        """
        super().__init__(kwargs)

        self_.attributes = attributes
        self_.type = type
