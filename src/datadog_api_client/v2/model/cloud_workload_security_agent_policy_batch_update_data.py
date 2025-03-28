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
    from datadog_api_client.v2.model.cloud_workload_security_agent_policy_batch_update_attributes import (
        CloudWorkloadSecurityAgentPolicyBatchUpdateAttributes,
    )
    from datadog_api_client.v2.model.cloud_workload_security_agent_policy_batch_update_data_type import (
        CloudWorkloadSecurityAgentPolicyBatchUpdateDataType,
    )


class CloudWorkloadSecurityAgentPolicyBatchUpdateData(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.cloud_workload_security_agent_policy_batch_update_attributes import (
            CloudWorkloadSecurityAgentPolicyBatchUpdateAttributes,
        )
        from datadog_api_client.v2.model.cloud_workload_security_agent_policy_batch_update_data_type import (
            CloudWorkloadSecurityAgentPolicyBatchUpdateDataType,
        )

        return {
            "attributes": (CloudWorkloadSecurityAgentPolicyBatchUpdateAttributes,),
            "id": (str,),
            "type": (CloudWorkloadSecurityAgentPolicyBatchUpdateDataType,),
        }

    attribute_map = {
        "attributes": "attributes",
        "id": "id",
        "type": "type",
    }

    def __init__(
        self_,
        attributes: CloudWorkloadSecurityAgentPolicyBatchUpdateAttributes,
        id: str,
        type: CloudWorkloadSecurityAgentPolicyBatchUpdateDataType,
        **kwargs,
    ):
        """
        Object containing batch update data for multiple Agent policies

        :param attributes: Attributes for the batch update operation
        :type attributes: CloudWorkloadSecurityAgentPolicyBatchUpdateAttributes

        :param id: Identifier for the batch operation
        :type id: str

        :param type: Type of the batch update operation
        :type type: CloudWorkloadSecurityAgentPolicyBatchUpdateDataType
        """
        super().__init__(kwargs)

        self_.attributes = attributes
        self_.id = id
        self_.type = type
