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
    from datadog_api_client.v2.model.ai_memory_violation_result_request_data import AiMemoryViolationResultRequestData


class AiMemoryViolationResultRequest(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.ai_memory_violation_result_request_data import (
            AiMemoryViolationResultRequestData,
        )

        return {
            "data": (AiMemoryViolationResultRequestData,),
        }

    attribute_map = {
        "data": "data",
    }

    def __init__(self_, data: Union[AiMemoryViolationResultRequestData, UnsetType] = unset, **kwargs):
        """
        Request body for creating an AI memory violation result.

        :param data: Request data for creating an AI memory violation result.
        :type data: AiMemoryViolationResultRequestData, optional
        """
        if data is not unset:
            kwargs["data"] = data
        super().__init__(kwargs)
