# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import List, TYPE_CHECKING

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
)


if TYPE_CHECKING:
    from datadog_api_client.v2.model.execution_policy_response_data import ExecutionPolicyResponseData
    from datadog_api_client.v2.model.execution_policy_list_response_meta import ExecutionPolicyListResponseMeta


class ExecutionPolicyListResponse(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.execution_policy_response_data import ExecutionPolicyResponseData
        from datadog_api_client.v2.model.execution_policy_list_response_meta import ExecutionPolicyListResponseMeta

        return {
            "data": ([ExecutionPolicyResponseData],),
            "meta": (ExecutionPolicyListResponseMeta,),
        }

    attribute_map = {
        "data": "data",
        "meta": "meta",
    }

    def __init__(self_, data: List[ExecutionPolicyResponseData], meta: ExecutionPolicyListResponseMeta, **kwargs):
        """
        Response object that includes a list of execution policies.

        :param data: The execution policies.
        :type data: [ExecutionPolicyResponseData]

        :param meta: Pagination metadata for the list of execution policies.
        :type meta: ExecutionPolicyListResponseMeta
        """
        super().__init__(kwargs)

        self_.data = data
        self_.meta = meta
