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
    from datadog_api_client.v2.model.ai_memory_violation_result_response_attributes import (
        AiMemoryViolationResultResponseAttributes,
    )
    from datadog_api_client.v2.model.ai_memory_violation_result_data_type import AiMemoryViolationResultDataType


class AiMemoryViolationResultResponseData(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.ai_memory_violation_result_response_attributes import (
            AiMemoryViolationResultResponseAttributes,
        )
        from datadog_api_client.v2.model.ai_memory_violation_result_data_type import AiMemoryViolationResultDataType

        return {
            "attributes": (AiMemoryViolationResultResponseAttributes,),
            "id": (str,),
            "type": (AiMemoryViolationResultDataType,),
        }

    attribute_map = {
        "attributes": "attributes",
        "id": "id",
        "type": "type",
    }

    def __init__(
        self_,
        attributes: AiMemoryViolationResultResponseAttributes,
        id: str,
        type: AiMemoryViolationResultDataType,
        **kwargs,
    ):
        """
        Response data for an AI memory violation result.

        :param attributes: Response attributes of an AI memory violation result.
        :type attributes: AiMemoryViolationResultResponseAttributes

        :param id: The numeric identifier of the violation result.
        :type id: str

        :param type: AI memory violation result resource type.
        :type type: AiMemoryViolationResultDataType
        """
        super().__init__(kwargs)

        self_.attributes = attributes
        self_.id = id
        self_.type = type
