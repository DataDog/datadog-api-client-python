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
    from datadog_api_client.v2.model.execution_policy_create_request_data import ExecutionPolicyCreateRequestData


class ExecutionPolicyCreateRequest(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.execution_policy_create_request_data import ExecutionPolicyCreateRequestData

        return {
            "data": (ExecutionPolicyCreateRequestData,),
        }

    attribute_map = {
        "data": "data",
    }

    def __init__(self_, data: ExecutionPolicyCreateRequestData, **kwargs):
        """
        Request object that includes the execution policy to create.

        :param data: Object for a single execution policy.
        :type data: ExecutionPolicyCreateRequestData
        """
        super().__init__(kwargs)

        self_.data = data
