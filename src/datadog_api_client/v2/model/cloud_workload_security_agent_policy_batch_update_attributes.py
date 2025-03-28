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
    from datadog_api_client.v2.model.cloud_workload_security_agent_policy_batch_update_attributes_policies_items import (
        CloudWorkloadSecurityAgentPolicyBatchUpdateAttributesPoliciesItems,
    )


class CloudWorkloadSecurityAgentPolicyBatchUpdateAttributes(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.cloud_workload_security_agent_policy_batch_update_attributes_policies_items import (
            CloudWorkloadSecurityAgentPolicyBatchUpdateAttributesPoliciesItems,
        )

        return {
            "policies": ([CloudWorkloadSecurityAgentPolicyBatchUpdateAttributesPoliciesItems],),
        }

    attribute_map = {
        "policies": "policies",
    }

    def __init__(
        self_,
        policies: Union[List[CloudWorkloadSecurityAgentPolicyBatchUpdateAttributesPoliciesItems], UnsetType] = unset,
        **kwargs,
    ):
        """
        Attributes for the batch update operation

        :param policies: List of policies to update in the batch
        :type policies: [CloudWorkloadSecurityAgentPolicyBatchUpdateAttributesPoliciesItems], optional
        """
        if policies is not unset:
            kwargs["policies"] = policies
        super().__init__(kwargs)
