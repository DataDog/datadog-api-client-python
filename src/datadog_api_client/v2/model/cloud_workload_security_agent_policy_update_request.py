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
    from datadog_api_client.v2.model.cloud_workload_security_agent_policy_update_data import (
        CloudWorkloadSecurityAgentPolicyUpdateData,
    )


class CloudWorkloadSecurityAgentPolicyUpdateRequest(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.cloud_workload_security_agent_policy_update_data import (
            CloudWorkloadSecurityAgentPolicyUpdateData,
        )

        return {
            "data": (CloudWorkloadSecurityAgentPolicyUpdateData,),
        }

    attribute_map = {
        "data": "data",
    }

    def __init__(self_, data: CloudWorkloadSecurityAgentPolicyUpdateData, **kwargs):
        """
        Request object that includes the Agent policy with the attributes to update

        :param data: Object for a single Agent policy
        :type data: CloudWorkloadSecurityAgentPolicyUpdateData
        """
        super().__init__(kwargs)

        self_.data = data
