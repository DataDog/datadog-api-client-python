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
    from datadog_api_client.v2.model.cloud_workload_security_agent_policy_create_data import (
        CloudWorkloadSecurityAgentPolicyCreateData,
    )


class CloudWorkloadSecurityAgentPolicyCreateRequest(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.cloud_workload_security_agent_policy_create_data import (
            CloudWorkloadSecurityAgentPolicyCreateData,
        )

        return {
            "data": (CloudWorkloadSecurityAgentPolicyCreateData,),
        }

    attribute_map = {
        "data": "data",
    }

    def __init__(self_, data: CloudWorkloadSecurityAgentPolicyCreateData, **kwargs):
        """
        Request object that includes the Agent policy to create

        :param data: Object for a single Agent rule
        :type data: CloudWorkloadSecurityAgentPolicyCreateData
        """
        super().__init__(kwargs)

        self_.data = data
