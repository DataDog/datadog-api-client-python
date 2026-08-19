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
    from datadog_api_client.v2.model.execution_policy_attributes import ExecutionPolicyAttributes
    from datadog_api_client.v2.model.execution_policy_type import ExecutionPolicyType


class ExecutionPolicyResponseData(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.execution_policy_attributes import ExecutionPolicyAttributes
        from datadog_api_client.v2.model.execution_policy_type import ExecutionPolicyType

        return {
            "attributes": (ExecutionPolicyAttributes,),
            "id": (str,),
            "type": (ExecutionPolicyType,),
        }

    attribute_map = {
        "attributes": "attributes",
        "id": "id",
        "type": "type",
    }
    read_only_vars = {
        "id",
    }

    def __init__(self_, attributes: ExecutionPolicyAttributes, id: str, type: ExecutionPolicyType, **kwargs):
        """
        Object for a single execution policy.

        :param attributes: An execution policy.
        :type attributes: ExecutionPolicyAttributes

        :param id: The ID of the execution policy.
        :type id: str

        :param type: The type of the resource. The value should always be ``execution_policy``.
        :type type: ExecutionPolicyType
        """
        super().__init__(kwargs)

        self_.attributes = attributes
        self_.id = id
        self_.type = type
