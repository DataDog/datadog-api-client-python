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
    from datadog_api_client.v2.model.ai_prompt_response_attributes import AiPromptResponseAttributes
    from datadog_api_client.v2.model.ai_prompt_data_type import AiPromptDataType


class AiPromptResponseData(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.ai_prompt_response_attributes import AiPromptResponseAttributes
        from datadog_api_client.v2.model.ai_prompt_data_type import AiPromptDataType

        return {
            "attributes": (AiPromptResponseAttributes,),
            "id": (str,),
            "type": (AiPromptDataType,),
        }

    attribute_map = {
        "attributes": "attributes",
        "id": "id",
        "type": "type",
    }

    def __init__(self_, attributes: AiPromptResponseAttributes, id: str, type: AiPromptDataType, **kwargs):
        """
        Response data for an AI prompt.

        :param attributes: Response attributes of an AI prompt.
        :type attributes: AiPromptResponseAttributes

        :param id: The prompt identifier.
        :type id: str

        :param type: AI prompt resource type.
        :type type: AiPromptDataType
        """
        super().__init__(kwargs)

        self_.attributes = attributes
        self_.id = id
        self_.type = type
